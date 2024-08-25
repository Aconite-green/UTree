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
            except Exception as e:
                self.error_handler.handle_error(str(e))
        else:
            # CHECK 시: CAN 통신 시작
            try:
                # CAN MANAGEMENT
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
            self.update_grid_based_on_selection(is_read=True)

    def handle_write(self, checked):
        if checked:
            widgets.radioButton_read.setChecked(False)
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
        for row_index, (key, sub_items) in enumerate(record_values.items()):
            # 각 행의 맨 왼쪽에 Label 추가
            label = QLabel(key)
            label.setStyleSheet("font-size: 12pt; font-weight: bold;")
            widgets.gridLayout_pannel_main.addWidget(label, row_index, 0)

            if isinstance(sub_items, dict) and isinstance(list(sub_items.values())[0], dict):
                # 1번 형태의 데이터 처리
                for col_index, sub_key in enumerate(sub_items.keys(), start=1):
                    button = QPushButton(sub_key)

                    # 버튼 스타일 설정
                    button.setStyleSheet(f"""
                        QPushButton {{
                            border: 2px solid rgb(52, 59, 72);
                            border-radius: 5px;
                            background-color: rgb(52, 59, 72);
                            font-weight: bold;
                            font-size: 15pt;
                        }}
                        QPushButton:hover {{
                            background-color: rgb(57, 65, 80);
                            border: 2px solid rgb(61, 70, 86);
                        }}
                        QPushButton:pressed {{
                            background-color: rgb(35, 40, 49);
                            border: 2px solid rgb(43, 50, 61);
                        }}
                        QPushButton:checked {{
                            background-color: rgb(35, 40, 49);
                            border: 2px solid rgb(61, 70, 86);
                        }}
                    """)
                    # rgb(35, 40, 49) : button pressend collor
                    # rgb(102, 163, 255) : sky color

                    size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    button.setSizePolicy(size_policy)

                    # 버튼이 체크 가능하게 설정
                    

                    # is_read 값에 따라 체크된 상태 설정
                    if is_read:
                        if sub_items[sub_key]['r'] != 0:
                            button.setChecked(True)
                        button.setCheckable(False)
                    else:
                        button.setCheckable(True)
                        if sub_items[sub_key]['w'] != 0:
                            button.setChecked(True)

                    # 버튼을 그리드 레이아웃에 추가
                    widgets.gridLayout_pannel_main.addWidget(button, row_index, col_index)
                    
            else:
                # 2번 형태의 데이터 처리
                if is_read:
                    # is_read가 True인 경우 값을 표시할 라벨을 추가
                    value_label = QLabel(f"{sub_items['r']:02X}")
                    value_label.setStyleSheet("""
                        font-size: 20pt; 
                        font-weight: bold;
                        border-radius: 10px;
                        border: 2px solid rgb(61, 70, 86);
                        background-color: rgb(35, 40, 49);
                    """)
                    value_label.setAlignment(Qt.AlignCenter)

                    size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    value_label.setSizePolicy(size_policy)
                    widgets.gridLayout_pannel_main.addWidget(value_label, row_index, 1)
                else:
                    # is_read가 False인 경우, "w" 값을 표시할 라벨 추가
                    value_label = QLabel(f"{sub_items['w']:02X}")
                    value_label.setStyleSheet("""
                        font-size: 20pt; 
                        font-weight: bold;
                        border-radius: 10px;
                        border: 2px solid rgb(61, 70, 86);
                        background-color: rgb(35, 40, 49);
                    """)
                    value_label.setAlignment(Qt.AlignCenter)
                    size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    value_label.setSizePolicy(size_policy)
                    #
                    #  값을 입력할 수 있는 LineEdit 추가
                    line_edit = QLineEdit()
                    size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    line_edit.setSizePolicy(size_policy)
                    line_edit.setStyleSheet("font-size: 20pt;")
                    
                    # 레이아웃에 추가
                    widgets.gridLayout_pannel_main.addWidget(value_label, row_index, 1)
                    widgets.gridLayout_pannel_main.addWidget(line_edit, row_index, 2)


    def handle_did_change(self):
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
