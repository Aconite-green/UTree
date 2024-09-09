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

root_dir = os.path.dirname(os.path.abspath(__file__))
modules_path = os.path.join(root_dir, 'modules')
if modules_path not in sys.path:
    sys.path.append(modules_path)

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
        self.uds_manager = UdsManager('./config_uds', self.error_handler, self.can_manager)
        self.read_record = False 
        self.record_values = None

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
    
    def print_record_values(self, record_values, is_read):
        for row_key, data_info in record_values.items():
            print(f"Row: {row_key}")
            for col_key, col_info in data_info['coloms'].items():
                if is_read:
                    current_val = col_info['current_val'][1]  # 읽기 모드의 current_val
                    mode = "Read"
                else:
                    current_val = col_info['current_val'][2]  # 쓰기 모드의 current_val
                    mode = "Write"

                print(f"  Column: {col_key} | {mode} Value: {current_val}")
            print()  # 행 간에 빈 줄 추가

    def handle_send(self):

        if widgets.radioButton_read.isChecked() or widgets.radioButton_write.isChecked():
            is_read = widgets.radioButton_read.isChecked()
            self.uds_manager.process_uds_cmd(is_read, self.record_values)
            self.populate_grid(self.record_values, is_read=is_read)

            if not is_read:
                self.uds_manager.copy_write_to_read()
            else:
                self.read_record = True
        else:
            self.error_handler.log_message("please select Write or Read Button")
        
    def handle_read(self, checked):
        
        if checked:
            selected_did = widgets.comboBox_did.currentText()
            self.uds_manager.select_did(selected_did)
            self.record_values = self.uds_manager.get_record_values()
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
            if self.record_values is not None:
                self.populate_grid(self.record_values, is_read=True)
                self.uds_manager.make_uds_cmd(is_read=True, record_values=self.record_values)
                data = self.uds_manager.get_uds_cmd()
                widgets.lineEdit_cancmd.setText(data)
    
    def handle_write(self, checked):

        if self.read_record: 
                self.uds_manager.copy_read_to_write()
        else:
            pass  

        if checked:
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
            if self.record_values is not None:
                self.populate_grid(self.record_values, is_read=False)
                self.uds_manager.make_uds_cmd(is_read=False, record_values=self.record_values)
                data = self.uds_manager.get_uds_cmd()
                widgets.lineEdit_cancmd.setText(data)

    def populate_grid(self, record_values, is_read):
        # 기존 버튼들 삭제
        while widgets.gridLayout_pannel_main.count():
            child = widgets.gridLayout_pannel_main.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for row_index, (key, data_info) in enumerate(record_values.items()):
            label = QLabel(key)
            label.setStyleSheet("font-size: 12pt; font-weight: bold;border: 2px solid rgb(61, 70, 86);")
            label.setAlignment(Qt.AlignCenter)
            widgets.gridLayout_pannel_main.addWidget(label, row_index, 0)

            total_bits = sum(col['bit'] for col in data_info['coloms'].values())
            col_start_index = 1

            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']
                col_type, options = col_info['type']
                max_digit, read_val, write_val = col_info['current_val']

                current_val = read_val if is_read else write_val

                # 공통적인 라벨 설정
                name_label = QLabel(col_key)
                name_label.setStyleSheet("""
                    font-size: 9pt; 
                    padding: 1px;
                    color: rgb(221, 221, 221);
                    border: 1px solid rgb(61, 70, 86);
                    background-color: transparent;
                """)
                name_label.setAlignment(Qt.AlignCenter)
                name_label.setFixedHeight(25)
                
                # 위젯 생성 및 설정
                widget = UIFunctions.create_widget(col_type, options, is_read, current_val, max_digit)
                
                if widget and not is_read:
                    def apply_styles(widget, val, col_type):
                        new_value, read_value = val[0], val[1]
                        if new_value != read_value:
                            if col_type == 'button':
                                widget.setStyleSheet(StyleSheets.PUSHBUTTON_STYLE_SHEET_DEACTIVE)
                            elif col_type == 'combobox':
                                widget.setStyleSheet(StyleSheets.STYLE_SHEET_DEACTIVE)
                            elif col_type == "line_edit":
                                widget.setStyleSheet(StyleSheets.STYLE_SHEET_DEACTIVE)
                        else:
                            if col_type == 'button':
                                widget.setStyleSheet(StyleSheets.PUSHBUTTON_STYLE_SHEET_ACTIVE)
                            else:
                                widget.setStyleSheet(StyleSheets.STYLE_SHEET_ACTIVE)
                    
                    if col_type == 'combobox':
                        widget.currentIndexChanged.connect(
                            lambda idx, row=row_index, col=col_key, col_type=col_type,widget=widget: (
        
                                self.uds_manager.update_record_value(self.record_values, row, col,self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, widget.currentText(), col_type)),
                                apply_styles(widget, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, widget.currentText(), col_type), col_type),
                                self.uds_manager.make_uds_cmd(is_read=False, record_values=self.record_values), 
                                widgets.lineEdit_cancmd.setText(self.uds_manager.get_uds_cmd())
                            )
                        )
                    elif col_type == 'line_edit':
                        widget.textChanged.connect(
                            lambda text, row=row_index, col=col_key, col_type=col_type, widget=widget: (
                            apply_styles(widget, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, widget.text(), col_type), col_type),
                            self.uds_manager.update_record_value(self.record_values, row, col, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, widget.text(), col_type)),
                            self.uds_manager.make_uds_cmd(is_read=False, record_values=self.record_values), 
                            widgets.lineEdit_cancmd.setText(self.uds_manager.get_uds_cmd())
                            )
                        )
                    elif col_type == 'button':
                        widget.clicked.connect(
                            lambda checked, row=row_index, col=col_key,col_type=col_type, widget=widget: 
                            (   apply_styles(widget, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, 0 if checked else 1, col_type), col_type),
                                widget.setText('0' if checked else '1'),  
                                self.uds_manager.update_record_value(self.record_values, row, col, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, 0 if checked else 1, col_type)),
                                self.uds_manager.make_uds_cmd(is_read=False, record_values=self.record_values), 
                                widgets.lineEdit_cancmd.setText(self.uds_manager.get_uds_cmd())
                            )
                        )

                if widget:
                    bit_ratio = bit_size / total_bits
                    col_span = max(1, int(bit_ratio * 8))  # 최소 1, 최대 8의 크기

                    vertical_layout = QVBoxLayout()
                    vertical_layout.addWidget(name_label)
                    vertical_layout.addWidget(widget)

                    container_widget = QWidget()
                    container_widget.setLayout(vertical_layout)

                    widgets.gridLayout_pannel_main.addWidget(container_widget, row_index, col_start_index, 1, col_span)
                    col_start_index += col_span

    def handle_did_change(self):
        
        self.read_record = False
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

        selected_did = widgets.comboBox_did.currentText()
        self.uds_manager.select_did(selected_did)
        self.record_values = self.uds_manager.get_record_values()

        if 'r' not in self.uds_manager.get_method():
            widgets.radioButton_read.setEnabled(False)
        else:
            widgets.radioButton_read.setEnabled(True)
        
        if 'w' not in self.uds_manager.get_method():
            widgets.radioButton_write.setEnabled(False)
        else:
            widgets.radioButton_write.setEnabled(True)

        widgets.radioButton_read.setAutoExclusive(True)
        widgets.radioButton_write.setAutoExclusive(True)

        # 패널 지우기
        while widgets.gridLayout_pannel_main.count():
            child = widgets.gridLayout_pannel_main.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        widgets.lineEdit_cancmd.clear()
    
    def print_record_values(self, record_values, is_read):
        for row_key, data_info in record_values.items():
            print(f"Row: {row_key}")
            for col_key, col_info in data_info['coloms'].items():
                current_val = col_info['current_val'][1] if is_read else col_info['current_val'][2]
                print(f"  Column: {col_key} | Current Value: {current_val}")
            print()  # 행 간에 빈 줄 추가
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

            if hasattr(self, 'uds_manager'):
                self.uds_manager.shutdown()  # UdsManager 자원 해제

            self.error_handler.log_message("Application resources were successfully cleaned up.")
        except Exception as e:
            self.error_handler.handle_error(f"Error during application shutdown: {str(e)}")
        
        event.accept()  # 프로그램 종료 허용

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("UTree_80.ico"))
    window = MainWindow()
    sys.exit(app.exec())
