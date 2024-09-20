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
        
        if not widgets.btn_connect.isChecked():
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
                            border: 1px solid rgb(220, 220, 220);
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
                            border: 1px solid rgb(220, 220, 220);
                        }
                        QComboBox QAbstractItemView {
                            color: rgb(135, 206, 250);
                            background-color: rgb(33, 37, 43);
                        }
                    """)

                    widgets.lineEdit_search.setEnabled(False)
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
                self.init_search_completer()

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
        if widgets.radioButton_read.isChecked() or widgets.radioButton_write.isChecked():
            is_read = widgets.radioButton_read.isChecked()
            if is_read:
                is_ok, send_data, recv_data, error_msg=self.uds_manager.process_uds_cmd_read(self.record_values)
                UIFunctions.update_log(widgets.plainTextEdit_log, 
                                       is_ok, error_msg, send_data, recv_data, is_read)
                
                if is_ok:
                    self.populate_grid(self.record_values, is_read=is_read)
                    self.read_record = True
                else:
                    pass
            else: # write
                is_valid = self.uds_manager.validate_value()
                if is_valid:
                    is_ok, send_data, recv_data, error_msg = self.uds_manager.process_uds_cmd_write(self.record_values)
                    UIFunctions.update_log(widgets.plainTextEdit_log, 
                                       is_ok, error_msg, send_data, recv_data, is_read)
                    
                    if is_ok:
                        self.populate_grid(self.record_values, is_read=is_read)
                        self.uds_manager.copy_write_to_read()
                    else:
                        pass
                else:
                    self.error_handler.log_message("not a valid write value")                
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
                self.uds_manager.auto_set()
                self.populate_grid(self.record_values, is_read=True)
                self.uds_manager.make_uds_cmd(is_read=True, record_values=self.record_values)
                data = self.uds_manager.get_uds_cmd()
                widgets.lineEdit_cancmd.setText(data)
                self.error_handler.clear_log()
        else:
            print("not set")
    
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
                self.uds_manager.auto_set()
                self.populate_grid(self.record_values, is_read=False)
                self.uds_manager.make_uds_cmd(is_read=False, record_values=self.record_values)
                data = self.uds_manager.get_uds_cmd()
                widgets.lineEdit_cancmd.setText(data)
                self.error_handler.clear_log()

    def populate_grid(self, record_values, is_read):
        # 기존 버튼들 삭제
        while widgets.gridLayout_pannel_main.count():
            child = widgets.gridLayout_pannel_main.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for row_index, (key, data_info) in enumerate(record_values.items()):
            # coloms 항목을 가져옴
            coloms = data_info.get('coloms', {})

            # coloms에 key가 1개만 있을 경우, coloms의 key를 label에 표시
            if len(coloms) == 1:
                colom_key = next(iter(coloms))  # coloms의 첫 번째(유일한) key 값 가져오기
                label_text = colom_key
            else:
                label_text = key

            label = QLabel(label_text)
            label.setStyleSheet("font-size: 12pt; font-weight: bold;border: 2px solid rgb(61, 70, 86);")
            label.setAlignment(Qt.AlignCenter)
            widgets.gridLayout_pannel_main.addWidget(label, row_index, 0)

            total_bits = sum(col['bit'] for col in coloms.values())
            col_start_index = 1

            for col_key, col_info in coloms.items():
                bit_size = col_info['bit']
                col_type = col_info['col_type']
                options = col_info['options']
                read_val, write_val = col_info['r_val'], col_info['w_val']

                current_val = read_val if is_read else write_val

                # coloms의 key가 1개일 경우 name_label을 생략하고 바로 위젯 추가
                if len(coloms) > 1:
                    name_label = QLabel(col_key)
                    name_label.setStyleSheet("""
                        font-size: 10pt; 
                        padding: 1px;
                        color: rgb(221, 221, 221);
                        border: 1px solid rgb(61, 70, 86);
                        background-color: transparent;
                    """)
                    name_label.setAlignment(Qt.AlignCenter)
                    name_label.setFixedHeight(25)

                # 위젯 생성 및 설정
                widget = UIFunctions.create_widget(col_type, options, is_read, current_val)

                if widget and not is_read:
                    

                    if col_type == 'combobox':
                        widget.currentIndexChanged.connect(
                            lambda idx, row=row_index, col=col_key, col_type=col_type, widget=widget: self.combobox_changed(idx, row, col, col_type, widget)
                        )
                    elif col_type == 'line_edit':
                        widget.textChanged.connect(
                            lambda text, row=row_index, col=col_key, col_type=col_type, widget=widget: self.line_edit_changed(text, row, col, col_type, widget)
                        )
                    elif col_type == 'button':
                        widget.clicked.connect(
                            lambda checked, row=row_index, col=col_key, col_type=col_type, widget=widget: self.button_clicked(checked, row, col, col_type, widget)
                        )
                    elif col_type == 'calendar':
                        widget.dateChanged.connect(
                            lambda date, row=row_index, col=col_key, col_type=col_type, widget=widget: self.calendar_changed(date, row, col, col_type, widget)
                        )

                if widget:
                    bit_ratio = bit_size / total_bits
                    col_span = max(1, int(bit_ratio * 8))  # 최소 1, 최대 8의 크기

                    vertical_layout = QVBoxLayout()

                    # coloms의 key가 1개가 아닐 때만 name_label 추가
                    if len(coloms) > 1:
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
                            border: 1px solid rgb(220, 220, 220);
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
        method = self.uds_manager.get_did_method()
        if len(method) == 2: # both r,w
            pass
        else:
            if 'r' in method:
                widgets.radioButton_read.click()
                pass
            else:
                widgets.radioButton_write.click()
                pass
    
    def print_record_values(self, record_values, is_read):
        for row_key, data_info in record_values.items():
            print(f"Row: {row_key}")
            for col_key, col_info in data_info['coloms'].items():
                current_val = col_info['current_val'][1] if is_read else col_info['current_val'][2]
                print(f"  Column: {col_key} | Current Value: {current_val}")
            print()  # 행 간에 빈 줄 추가
    
    def apply_styles(self, widget, val, col_type):
                        new_value, read_value = val[0], val[1]
                        print(f"input : {new_value}, read_val : {read_value}")
                        if new_value != read_value:
                            
                            if col_type == 'button':
                                widget.setStyleSheet(StyleSheets.PUSHBUTTON_STYLE_SHEET_DEACTIVE)
                            elif col_type == 'combobox':
                                widget.setStyleSheet(StyleSheets.STYLE_SHEET_DEACTIVE)
                            elif col_type == "line_edit":
                                widget.setStyleSheet(StyleSheets.STYLE_SHEET_DEACTIVE)
                            elif col_type == "calendar":
                                widget.setStyleSheet(StyleSheets.STYLE_SHEET_DEACTIVE)
                                
                        else:
                            if col_type == 'button':
                                widget.setStyleSheet(StyleSheets.PUSHBUTTON_STYLE_SHEET_ACTIVE)
                            elif col_type == "calendar":
                                widget.setStyleSheet(StyleSheets.STYLE_SHEET_ACTIVE)
                            else:
                                widget.setStyleSheet(StyleSheets.STYLE_SHEET_ACTIVE)

    def combobox_changed(self, idx, row, col, col_type, widget):
        value = widget.currentText()
        self.uds_manager.update_record_value(
            self.record_values, row, col, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, value, col_type)
        )
        self.apply_styles(widget, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, value, col_type), col_type)
        self.uds_manager.make_uds_cmd(is_read=False, record_values=self.record_values)
        widgets.lineEdit_cancmd.setText(self.uds_manager.get_uds_cmd())
        self.error_handler.clear_log()

    def line_edit_changed(self, text, row, col, col_type, widget):
        self.apply_styles(widget, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, text, col_type), col_type)
        self.uds_manager.update_record_value(
            self.record_values, row, col, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, text, col_type)
        )
        self.uds_manager.make_uds_cmd(is_read=False, record_values=self.record_values)
        widgets.lineEdit_cancmd.setText(self.uds_manager.get_uds_cmd())
        self.error_handler.clear_log()

    def button_clicked(self, checked, row, col, col_type, widget):
        value = 0 if checked else 1
        self.apply_styles(widget, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, value, col_type), col_type)
        widget.setText('0' if checked else '1')
        self.uds_manager.update_record_value(
            self.record_values, row, col, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, value, col_type)
        )
        self.uds_manager.make_uds_cmd(is_read=False, record_values=self.record_values)
        widgets.lineEdit_cancmd.setText(self.uds_manager.get_uds_cmd())
        self.error_handler.clear_log()

    def calendar_changed(self, date, row, col, col_type, widget):
        date_str = date.toString("yyyyMMdd")
        self.apply_styles(widget, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, date_str, col_type), col_type)
        self.uds_manager.update_record_value(
            self.record_values, row, col, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, date_str, col_type)
        )
        self.uds_manager.make_uds_cmd(is_read=False, record_values=self.record_values)
        widgets.lineEdit_cancmd.setText(self.uds_manager.get_uds_cmd())
        self.error_handler.clear_log()

    # INIT SEARCH FUNCTION
    # ///////////////////////////////////////////////////////////////
    def init_search_completer(self):
        # 검색 데이터 준비: did_map의 클래스 이름과 각 클래스의 record_values 키 및 coloms 키 추가
        self.search_data = self.get_search_data()

        # QCompleter 생성 및 설정
        self.completer = QCompleter(list(self.search_data.keys()), self)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)  # 대소문자 구분 없이 검색

        # 스타일시트 설정 (자동완성 팝업의 배경색과 글자색 변경)
        self.completer.popup().setStyleSheet("""
            QAbstractItemView {
                background-color: rgb(27, 29, 35);
                color: rgb(135, 206, 250);
                border: 1px solid rgb(61, 70, 86);
            }
        """)

        # lineEdit_search에 completer 연결
        widgets.lineEdit_search.setEnabled(True)
        widgets.lineEdit_search.setCompleter(self.completer)

        # lineEdit_search에서 입력된 검색어 처리
        widgets.lineEdit_search.textChanged.connect(self.handle_search)

# search_data 목록 생성 함수
    def get_search_data(self):
        search_data = {}

        # 1. did_map의 클래스 이름들 추가
        did_names = self.uds_manager.get_did_names()

        # 딕셔너리로 저장하여 col_key에 해당하는 did_name도 매핑 가능하게 만듦
        for did_name in did_names:
            search_data[did_name] = did_name

            
            self.uds_manager.select_did(did_name)
            record_values = self.uds_manager.get_record_values()

            for data_key, data_info in record_values.items():
                for col_key in data_info['coloms']:
                    search_data[col_key] = did_name  # col_key를 해당하는 did_name에 매핑

        return search_data

    # 검색어 처리 함수
    def handle_search(self):
        search_text = widgets.lineEdit_search.text().strip()

        if not search_text:
            # 빈 검색어일 경우 패널을 비움
            while widgets.gridLayout_pannel_main.count():
                child = widgets.gridLayout_pannel_main.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

            # ComboBox 초기화
            widgets.comboBox_did.setCurrentIndex(0)  # 아무 것도 선택되지 않도록 초기화
            widgets.lineEdit_cancmd.clear()  # 검색어 초기화 시 커맨드 라인도 초기화
            self.handle_did_change()
            return

        # 검색어와 매칭되는 DID 이름이나 col_key 찾기
        matching_items = [key for key in self.search_data if search_text.lower() in key.lower()]

        if matching_items:
            matched_did_name = self.search_data[matching_items[0]]
            widgets.comboBox_did.setCurrentText(matched_did_name)

            # 해당 DID를 선택하여 로드
            self.handle_did_change()  # 직접 handle_did_change 함수 호출

            # method 확인 ('r'과 'w' 둘 다 있는지 확인)
            method = self.uds_manager.get_method()

            # 'r'과 'w'가 모두 존재하면 'r'을 선택하고 radioButton_read를 클릭
            if 'r' in method and 'w' in method:
                widgets.radioButton_read.setChecked(True)  # 'r' 유형 자동 선택
            else:
                if 'r' in method:
                    widgets.radioButton_read.setChecked(True)  # 'r' 유형만 있을 경우 선택
                elif 'w' in method:
                    widgets.radioButton_write.setChecked(True)  # 'w' 유형만 있을 경우 선택
        else:
            # 해당 DID가 없을 때 처리
            widgets.lineEdit_search.setCompleter(QCompleter(["Cannot find DID"], self))

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
