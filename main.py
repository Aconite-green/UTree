# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# pyrcc6 -o resource_rc.py resource.qrc
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
import importlib

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "UTree"
        description = "UTree APP - GUI Program for UDS Management."

        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                
        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # CONNECT BUTTON
        widgets.btn_connect.clicked.connect(self.handle_connect)
        widgets.btn_send.clicked.connect(self.handle_send)
        widgets.radioButton_read.toggled.connect(self.handle_read)
        widgets.radioButton_write.toggled.connect(self.handle_write)

        # CONNECT COMBOBOX
        widgets.comboBox_did.currentIndexChanged.connect(self.handle_did_change)
        
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # Initialize Modules
        self.error_handler = ErrorHandler(log_widget=widgets.plainTextEdit_log)
        self.can_manager = CanManager('./config_can', self.error_handler)
        self.uds_manager = UdsManager('./config_uds', self.error_handler)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        widgets.stackedWidget.setCurrentWidget(widgets.widgets_workspace)
        widgets.groupBox_pannel.setVisible(False)
        self.populateComboBoxes()

    # BUTTONS CLICK
    # ///////////////////////////////////////////////////////////////
    def handle_connect(self):
        btn = self.sender()
        if not btn.isChecked():
            # CHECK 해제 시: CAN 통신 중지
            try:
                if hasattr(self, 'can_manager'):
                    self.error_handler.clear_log()
                    self.can_manager.stop_communication()

                    widgets.groupBox_pannel.setVisible(False)
                    widgets.stackedWidget.setCurrentWidget(widgets.widgets_workspace)
                    widgets.pagesContainer.setStyleSheet(UIFunctions.show_utree_logo())
                     # ComboBox 활성화 및 스타일 복구
                    widgets.comboBox_uds.setEnabled(True)
                    widgets.comboBox_can.setEnabled(True)

                    widgets.comboBox_uds.setStyleSheet("""
                        QComboBox {
                            color: rgb(221, 221, 221);
                            background-color: rgb(33, 37, 43);
                        }
                        QComboBox QAbstractItemView {
                            color: rgb(135, 206, 250);
                            background-color: rgb(33, 37, 43);
                        }
                    """)

                    widgets.comboBox_can.setStyleSheet("""
                        QComboBox {
                            color: rgb(221, 221, 221);
                            background-color: rgb(33, 37, 43);
                        }
                        QComboBox QAbstractItemView {
                            color: rgb(135, 206, 250);
                            background-color: rgb(33, 37, 43);
                        }
                    """)
            except Exception as e:
                self.error_handler.handle_error(str(e))
        else:
            # CHECK 시: CAN 통신 시작
            try:
                # CAN MANAGEMENT
                self.error_handler.clear_log()
                selected_can_file = widgets.comboBox_can.currentText()               
                self.can_manager.get_selected_can_yml(selected_can_file)
                self.can_manager.setup_can()
                self.can_manager.start_communication()

                # UDS MANAGEMENT
                selected_uds_file = widgets.comboBox_uds.currentText()
                self.uds_manager.load_module_classes(selected_uds_file)

                did_names = self.uds_manager.get_did_names()
                widgets.comboBox_did.clear()
                widgets.comboBox_did.addItems(did_names)
                
                # GUI MANAGEMENT
                widgets.stackedWidget.setCurrentWidget(widgets.widgets_workspace)
                widgets.groupBox_pannel.setVisible(True)
                widgets.pagesContainer.setStyleSheet(UIFunctions.erase_background())
                 # ComboBox 비활성화 및 스타일 변경
                widgets.comboBox_uds.setEnabled(False)
                widgets.comboBox_can.setEnabled(False)

                widgets.comboBox_uds.setStyleSheet("""
                    QComboBox {
                        color: rgb(135, 206, 250);
                        background-color: rgb(33, 37, 43);
                    }
                    QComboBox QAbstractItemView {
                        color: rgb(135, 206, 250);
                        background-color: rgb(33, 37, 43);
                    }
                """)

                widgets.comboBox_can.setStyleSheet("""
                    QComboBox {
                        color: rgb(135, 206, 250);
                        background-color: rgb(33, 37, 43);
                    }
                    QComboBox QAbstractItemView {
                        color: rgb(135, 206, 250);
                        background-color: rgb(33, 37, 43);
                    }
                """)
            except Exception as e:
                self.error_handler.handle_error(str(e))
    
    def handle_send(self):
        # btn = self.sender()
        try:
            test_msg = bytearray([0x22, 0x00, 0x80])
            self.can_manager.send_message(test_msg)
            self.can_manager.receive_message()
        except Exception as e:
                self.error_handler.handle_error(str(e))
    
    def handle_read(self, checked):
        if checked:
            widgets.radioButton_write.setChecked(False)
            widgets.comboBox_did.setStyleSheet("""
                    QComboBox {
                        color: rgb(135, 206, 250);
                        background-color: rgb(33, 37, 43);
                    }
                    QComboBox QAbstractItemView {
                        color: rgb(135, 206, 250);
                        background-color: rgb(33, 37, 43);
                    }
                """)
            
            self.update_grid_based_on_selection(is_read=True)

    def handle_write(self, checked):
        if checked:
            widgets.radioButton_read.setChecked(False)
            widgets.comboBox_did.setStyleSheet("""
                    QComboBox {
                        color: rgb(135, 206, 250);
                        background-color: rgb(33, 37, 43);
                    }
                    QComboBox QAbstractItemView {
                        color: rgb(135, 206, 250);
                        background-color: rgb(33, 37, 43);
                    }
                """)
            self.update_grid_based_on_selection(is_read=False)
    
    def update_grid_based_on_selection(self, is_read):
        # 현재 선택된 DID와 관련된 데이터를 불러오기
        selected_did = widgets.comboBox_did.currentText()
        uds_class = self.uds_manager.did_map.get(selected_did)

        if uds_class:
            record_values = uds_class().get_record_values()
        
            # 행, 열 계산 후 버튼 생성
            self.populate_grid_with_buttons(record_values, is_read)

    def populate_grid_with_buttons(self, record_values, is_read):

        # 기존 버튼들 삭제
        while widgets.gridLayout_pannel_main.count():
            child = widgets.gridLayout_pannel_main.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        if is_read:
            selected_data = record_values['r']

            for row_index, (key, data_info) in enumerate(selected_data.items()):
                # 1. 행의 이름을 나타내는 Label 추가
                label = QLabel(key)
                label.setStyleSheet("font-size: 12pt; font-weight: bold;border: 2px solid rgb(61, 70, 86);")
                widgets.gridLayout_pannel_main.addWidget(label, row_index, 0)

                # 전체 비트수 계산
                total_bits = sum(col['bit'] for col in data_info['coloms'].values())

                col_start_index = 1  # 첫 번째 열 인덱스 (0은 행의 이름이 들어감)
                for col_key, col_info in data_info['coloms'].items():
                    bit_size = col_info['bit']
                    val_type, val_value = col_info['val']

                    # 2. 메인 키 이름을 표시하는 Label 생성 (위쪽)
                    name_label = QLabel(col_key)
                    name_label.setStyleSheet("""
                        font-size: 12pt; 
                        padding: 5px;
                        color: rgb(221, 221, 221);
                        border: 2px solid rgb(61, 70, 86);
                        background-color: transparent;
                    """)
                    name_label.setAlignment(Qt.AlignCenter)
                    name_label.setFixedHeight(35)
                    # 3. val 값을 표시하는 Label 생성 (아래쪽)
                    if val_value is not None:
                        value_label = QLabel(f"{val_value}")
                    else:
                        value_label = QLabel("")  # val_value가 None인 경우 비워둠

                    value_label.setStyleSheet("""
                        font-size: 10pt; 
                        font-weight: bold;
                        border: 2px solid rgb(61, 70, 86);
                        background-color: rgb(35, 40, 49);
                        margin-top: 0px;  
                        padding: 2px; 
                    """)
                    value_label.setAlignment(Qt.AlignCenter)

                    # 각 열의 비율에 따른 너비 설정
                    bit_ratio = bit_size / total_bits
                    col_span = max(1, int(bit_ratio * 7))  # 최소 1, 최대 7의 크기

                    # 수직 레이아웃을 사용하여 두 Label을 합침
                    vertical_layout = QVBoxLayout()
                    vertical_layout.setSpacing(0)  # 위젯 간의 간격 최소화
                    vertical_layout.setContentsMargins(0, 0, 0, 0)  # 레이아웃의 여백 제거
                    vertical_layout.addWidget(name_label)
                    vertical_layout.addWidget(value_label)

                    # QWidget을 사용하여 레이아웃을 담음
                    container_widget = QWidget()
                    container_widget.setLayout(vertical_layout)

                    # 컨테이너 위젯을 그리드 레이아웃에 추가
                    widgets.gridLayout_pannel_main.addWidget(container_widget, row_index, col_start_index, 1, col_span)
                    col_start_index += col_span  # 다음 열의 시작 위치 업데이트

        else:
            selected_data = record_values['w']
            for row_index, (key, data_info) in enumerate(selected_data.items()):
                # 1. 행의 이름을 나타내는 Label 추가
                label = QLabel(key)
                label.setStyleSheet("font-size: 12pt; font-weight: bold;border: 2px solid rgb(61, 70, 86);")
                widgets.gridLayout_pannel_main.addWidget(label, row_index, 0)

                # 전체 비트수 계산
                total_bits = sum(col['bit'] for col in data_info['coloms'].values())

                col_start_index = 1  # 첫 번째 열 인덱스 (0은 행의 이름이 들어감)
                for col_key, col_info in data_info['coloms'].items():
                    bit_size = col_info['bit']
                    col_type = col_info['type']
                    val_value = col_info['val']

                    # 2. 메인 키 이름을 표시하는 Label 생성 (위쪽)
                    name_label = QLabel(col_key)
                    name_label.setStyleSheet("""
                        font-size: 12pt; 
                        padding: 5px;
                        color: rgb(221, 221, 221);
                        border: 2px solid rgb(61, 70, 86);
                        background-color: transparent;
                    """)
                    name_label.setAlignment(Qt.AlignCenter)
                    name_label.setFixedHeight(35)
                   
                    # 3. 각 유형에 따른 위젯 생성
                    if col_type == 'button':
                        widget = QPushButton(val_value or "")
                        widget.setStyleSheet("""
                            QPushButton {
                                font-size: 10pt;
                                font-weight: bold;
                                border: 2px solid rgb(61, 70, 86);
                                background-color: rgb(52, 59, 72);
                                padding:2px;
                            }
                            QPushButton:hover {
                                background-color: rgb(57, 65, 80);
                            }
                        """)
                        widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
                    elif col_type == 'combobox':
                        widget = QComboBox()
                        widget.addItems(col_info.get('menu', {}).keys())
                        widget.setStyleSheet("""
                            QComboBox {
                                font-size: 10pt;
                                border: 2px solid rgb(61, 70, 86);
                                background-color: rgb(52, 59, 72);
                                padding: 2px;
                            }
                            QComboBox QAbstractItemView {
                                background-color: rgb(52, 59, 72);
                                selection-background-color: rgb(57, 65, 80);
                            }
                        """)
                        widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
                    elif col_type == 'edit':
                        widget = QLineEdit()
                        widget.setText(val_value or "")
                        widget.setStyleSheet("""
                            QLineEdit {
                                font-size: 10pt;
                                border: 2px solid rgb(61, 70, 86);
                                background-color: rgb(52, 59, 72);
                                padding: 2px;
                            }
                        """)
                        widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
                    # 각 열의 비율에 따른 너비 설정
                    bit_ratio = bit_size / total_bits
                    col_span = max(1, int(bit_ratio * 7))  # 최소 1, 최대 7의 크기

                    # 수직 레이아웃을 사용하여 두 Label을 합침
                    vertical_layout = QVBoxLayout()
                    vertical_layout.addWidget(name_label)
                    vertical_layout.addWidget(widget)

                    # QWidget을 사용하여 레이아웃을 담음
                    container_widget = QWidget()
                    container_widget.setLayout(vertical_layout)

                    # 컨테이너 위젯을 그리드 레이아웃에 추가
                    widgets.gridLayout_pannel_main.addWidget(container_widget, row_index, col_start_index, 1, col_span)
                    col_start_index += col_span  # 다음 열의 시작 위치 업데이트

    def handle_did_change(self):

        widgets.comboBox_did.setStyleSheet("""
                        QComboBox {
                            color: rgb(221, 221, 221);
                            background-color: rgb(33, 37, 43);
                        }
                        QComboBox QAbstractItemView {
                            color: rgb(135, 206, 250);
                            background-color: rgb(33, 37, 43);
                        }
                    """)
        # 라디오 버튼의 autoExclusive 속성 비활성화
        widgets.radioButton_read.setAutoExclusive(False)
        widgets.radioButton_write.setAutoExclusive(False)

        # 라디오 버튼 초기화
        widgets.radioButton_read.setChecked(False)
        widgets.radioButton_write.setChecked(False)

        # 다시 autoExclusive 활성화
        widgets.radioButton_read.setAutoExclusive(True)
        widgets.radioButton_write.setAutoExclusive(True)

        # 패널 지우기
        while widgets.gridLayout_pannel_main.count():
            child = widgets.gridLayout_pannel_main.takeAt(0)
            if child.widget():
                child.widget().deleteLater()


    
    # INIT CONFIG COMBOBOX
    # ///////////////////////////////////////////////////////////////
    def populateComboBoxes(self):
        self.can_manager.load_yml_files()
        
        # Populate comboBox_can with CAN YML file names
        can_file_names = self.can_manager.get_can_file_names()
        widgets.comboBox_can.clear()
        widgets.comboBox_can.addItems(can_file_names)

        # 필요에 따라 UDS 관련 comboBox도 추가 가능
        uds_file_names = self.uds_manager.get_uds_file_names()
        widgets.comboBox_uds.clear()
        widgets.comboBox_uds.addItems(uds_file_names)
    
       

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    # CLOSE EVENT HANDLER
    # ///////////////////////////////////////////////////////////////
    def closeEvent(self, event):
        try:
            if hasattr(self, 'can_manager'):
                self.can_manager.stop_communication()
                self.error_handler.log_message("CAN bus and layer were successfully shut down before closing.")
        except Exception as e:
            self.error_handler.handle_error(f"Error during application shutdown: {str(e)}")
        # Accept the event to close the application
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("UTree_80.ico"))
    window = MainWindow()
    sys.exit(app.exec())
