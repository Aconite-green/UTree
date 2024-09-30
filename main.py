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

paths = [
    os.path.join(root_dir, 'modules'),
    os.path.join(root_dir, 'config_can'),
    os.path.join(root_dir, 'config_uds'),
    os.path.join(root_dir, 'config_dll'),
    os.path.join(root_dir, 'config_user_info')
]

for path in paths:
    if path not in sys.path:
        sys.path.append(path)


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
        self.uds_manager = UdsManager('./config_uds', "./config_dll",self.error_handler, self.can_manager)
        self.service_manager = ServiceManager('./config_user_info')
        self.read_record = False 
        self.record_values = None
        self.user_sent = False
        self.error_for_timer = False
        
        # Timer
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.check_can_communication)
        
        
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        widgets.stackedWidget.setCurrentWidget(widgets.widgets_workspace)
        widgets.groupBox_pannel.setVisible(False)
        self.populateComboBoxes()
        if not self.service_manager.get_user_status():
            widgets.plainTextEdit_log.setPlainText(UIFunctions.menual_info())
 

    # CAN Mangement
    # ///////////////////////////////////////////////////////////////
    def check_can_communication(self):
        
        try:
            is_ok = self.uds_manager.check_can_device()
            if is_ok:
                pass
            else:
                # CAN Managemet
                self.timer.stop()
                self.can_manager.stop_communication()
                # For GUI
                widgets.btn_connect.setChecked(False)
                error_msg = f"The communication was disconnected"
                UIFunctions.update_log(widgets.plainTextEdit_log, 
                                   is_ok, error_msg, None, None, 'connection')
                
                widgets.groupBox_pannel.setVisible(False)
                widgets.stackedWidget.setCurrentWidget(widgets.widgets_workspace)
                widgets.pagesContainer.setStyleSheet(UIFunctions.show_utree_logo())
                 # ComboBox 활성화 및 스타일 복구
                widgets.comboBox_uds.setEnabled(True)
                widgets.comboBox_can.setEnabled(True)
                widgets.comboBox_dll.setEnabled(True)
                widgets.comboBox_uds.setStyleSheet(StyleSheets.CONFIGUATION_STYLE_SHEET_DEACTIVE)
                widgets.comboBox_can.setStyleSheet(StyleSheets.CONFIGUATION_STYLE_SHEET_DEACTIVE)
                widgets.comboBox_dll.setStyleSheet(StyleSheets.CONFIGUATION_STYLE_SHEET_DEACTIVE)
                widgets.btn_connect.setText("Connect")
                widgets.lineEdit_search.setEnabled(False)
        except Exception as e:
            self.error_handler.handle_error(f"CAN 통신 체크 중 에러 발생: {str(e)}")
    
    # BUTTONS CLICK
    # ///////////////////////////////////////////////////////////////
    def handle_connect(self):
        current_text = widgets.btn_connect.text()
        
        if current_text == "Connected":  # CAN STOP
            try:
                if hasattr(self, 'can_manager'):
                    
                    # UDS MANAGEMENT
                    # ///////////////////////////////////////////////////////////////
                    self.timer.stop()
                    self.can_manager.stop_communication()

                    # GUI MANAGEMENT
                    # ///////////////////////////////////////////////////////////////

                    # Pannel
                    widgets.groupBox_pannel.setVisible(False)
                    widgets.stackedWidget.setCurrentWidget(widgets.widgets_workspace)
                    widgets.pagesContainer.setStyleSheet(UIFunctions.show_utree_logo())
                    
                    # Connect button
                    widgets.btn_connect.setText("Connect")
                    widgets.btn_connect.setStyleSheet(StyleSheets.CONNECT_BUTTEN_STYLE_SHEET_DEACTIVE)

                    # Configuation Combobox
                    widgets.comboBox_uds.setEnabled(True)
                    widgets.comboBox_can.setEnabled(True)
                    widgets.comboBox_dll.setEnabled(True)

                    widgets.comboBox_uds.setStyleSheet(StyleSheets.CONFIGUATION_STYLE_SHEET_DEACTIVE)
                    widgets.comboBox_can.setStyleSheet(StyleSheets.CONFIGUATION_STYLE_SHEET_DEACTIVE)
                    widgets.comboBox_dll.setStyleSheet(StyleSheets.CONFIGUATION_STYLE_SHEET_DEACTIVE)
                    
                    # Report Log Text Edit
                    self.error_handler.clear_log()
                    if not self.service_manager.get_user_status():    
                        widgets.plainTextEdit_log.setPlainText(UIFunctions.menual_info())
                    
                    # Search Line Edit
                    widgets.lineEdit_search.setEnabled(False)

            except Exception as e:
                self.error_handler.handle_error(str(e))
        else:  # CAN START
            try:
                
                # UDS MANAGEMENT
                # ///////////////////////////////////////////////////////////////

                # CAN
                selected_can_file = widgets.comboBox_can.currentText()               
                self.can_manager.get_selected_can_yml(selected_can_file)
                
                is_ok, error_msg = self.can_manager.setup_can()
                if not is_ok:
                    UIFunctions.update_log(widgets.plainTextEdit_log, 
                                       is_ok, error_msg, None, None, 'connection')
                is_ok, error_msg = self.can_manager.start_communication()
                if not is_ok:
                    UIFunctions.update_log(widgets.plainTextEdit_log, 
                                       is_ok, error_msg, None, None, 'connection')
                
                if is_ok:
                    
                    # Service MANAGEMENT
                    # ///////////////////////////////////////////////////////////////
                    selected_project_file = widgets.comboBox_uds.currentText()
                    selected_dll_file = widgets.comboBox_dll.currentText()
                    selected_can_file = widgets.comboBox_can.currentText()

                    self.service_manager.update_recent_project(selected_project_file)
                    self.service_manager.update_recent_dll(selected_dll_file)
                    self.service_manager.update_recent_can(selected_can_file)

                    # UDS MANAGEMENT
                    # ///////////////////////////////////////////////////////////////
                    
                    # Timer start
                    self.timer.start()
                    
                    # ASK Settings
                    selected_dll_file = widgets.comboBox_dll.currentText()
                    self.uds_manager.set_dll(selected_dll_file)

                    # GUI MANAGEMENT
                    # ///////////////////////////////////////////////////////////////
                    
                    # Pannel
                    widgets.stackedWidget.setCurrentWidget(widgets.widgets_workspace)
                    widgets.groupBox_pannel.setVisible(True)
                    widgets.pagesContainer.setStyleSheet(UIFunctions.erase_background())

                    # Connect button
                    widgets.btn_connect.setText("Connected")
                    widgets.btn_connect.setStyleSheet(StyleSheets.CONNECT_BUTTEN_STYLE_SHEET_ACTIVE)
                    
                    # Configuation Combobox
                    widgets.comboBox_uds.setEnabled(False)
                    widgets.comboBox_can.setEnabled(False)
                    widgets.comboBox_dll.setEnabled(False)

                    widgets.comboBox_uds.setStyleSheet(StyleSheets.CONFIGUATION_STYLE_SHEET_ACTIVE)
                    widgets.comboBox_can.setStyleSheet(StyleSheets.CONFIGUATION_STYLE_SHEET_ACTIVE)
                    widgets.comboBox_dll.setStyleSheet(StyleSheets.CONFIGUATION_STYLE_SHEET_ACTIVE)

                    # Report Log Text Edit
                    self.error_handler.clear_log()
                    if not self.service_manager.get_user_status() and not self.user_sent:
                        widgets.plainTextEdit_log.setPlainText(UIFunctions.menual_info())

                    # DID Combobox
                    selected_uds_file = widgets.comboBox_uds.currentText()
                    self.uds_manager.load_module_classes(selected_uds_file)
                    did_names = self.uds_manager.get_did_names()
                    widgets.comboBox_did.clear()
                    widgets.comboBox_did.addItems(did_names)

                    
                    # Search Line Edit
                    self.init_search_completer()

                    # Init DID
                    self.uds_manager.select_did(did_names[0])

                else: # CAN Error State 
                    self.can_manager.stop_communication()
                    widgets.btn_connect.setChecked(False)
            
            
            except Exception as e:
                self.error_handler.handle_error(str(e))
    
    def handle_send(self):
        if widgets.radioButton_read.isChecked() or widgets.radioButton_write.isChecked():
            is_read = widgets.radioButton_read.isChecked()
            self.user_sent = True
            if is_read:
                is_ok, send_data, recv_data, error_msg=self.uds_manager.process_uds_cmd_read(self.record_values)
                UIFunctions.update_log(widgets.plainTextEdit_log, 
                                       is_ok, error_msg, send_data, recv_data, 'read')
                
                if is_ok:
                    self.populate_grid(self.record_values, is_read=is_read)
                    self.read_record = True
                    
                    # Service MANAGEMENT
                    # ///////////////////////////////////////////////////////////////
                    self.service_manager.update_user_status(True)

                else:
                    pass
            else: # write
                is_valid, msg = self.uds_manager.validate_value()
                if is_valid:
                    is_ok, send_data, recv_data, error_msg = self.uds_manager.process_uds_cmd_write(self.record_values)
                    UIFunctions.update_log(widgets.plainTextEdit_log, 
                                       is_ok, error_msg, send_data, recv_data, 'write')
                    
                    if is_ok:
                        self.uds_manager.copy_write_to_read()
                        self.populate_grid(self.record_values, is_read=is_read)
                        
                    else:
                        pass
                else:
                    is_ok, send_data, recv_data, error_msg = is_valid, None, None, msg
                    UIFunctions.update_log(widgets.plainTextEdit_log, 
                                       is_ok, error_msg, send_data, recv_data, 'write')               
        else:
            self.error_handler.log_message("please select Write or Read Button")
        
    def handle_read(self, checked):
        
        if checked:
            selected_did = widgets.comboBox_did.currentText()
            self.uds_manager.select_did(selected_did)
            self.record_values = self.uds_manager.get_record_values()
            widgets.comboBox_did.setStyleSheet(StyleSheets.CONFIGUATION_STYLE_SHEET_ACTIVE)
            if self.record_values is not None:
                self.uds_manager.auto_set()
                self.populate_grid(self.record_values, is_read=True)
                self.uds_manager.make_uds_cmd(is_read=True, record_values=self.record_values)
                data = self.uds_manager.get_uds_cmd()
                widgets.lineEdit_cancmd.setText(data)
                
        else:
            pass
    
    def handle_write(self, checked):

        if self.read_record:
            self.uds_manager.copy_read_to_write()
        else:
            self.uds_manager.init_write_val()  
        
        self.record_values = self.uds_manager.get_record_values()
        if checked:
            widgets.comboBox_did.setStyleSheet(StyleSheets.CONFIGUATION_STYLE_SHEET_ACTIVE)
            if self.record_values is not None:
                self.uds_manager.auto_set()
                self.populate_grid(self.record_values, is_read=False)
                self.uds_manager.make_uds_cmd(is_read=False, record_values=self.record_values)
                data = self.uds_manager.get_uds_cmd()
                widgets.lineEdit_cancmd.setText(data)
               
    # COMBOBOX
    # ///////////////////////////////////////////////////////////////
    def handle_did_change(self):
        if self.user_sent:
            self.error_handler.clear_log()
        self.read_record = False
        widgets.comboBox_did.setStyleSheet(StyleSheets.CONFIGUATION_STYLE_SHEET_DEACTIVE)
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
    
    def populateComboBoxes(self):
        # CAN 관련 처리
        self.can_manager.load_yml_files()
        can_file_names = self.can_manager.get_can_file_names()
        widgets.comboBox_can.clear()
        widgets.comboBox_can.addItems(can_file_names)

        # YML 파일의 'can' 값이 있으면 해당 값을 선택
        recent_can_file = self.service_manager.get_recent_can()
        if recent_can_file and recent_can_file in can_file_names:
            widgets.comboBox_can.setCurrentText(recent_can_file)

        # UDS 관련 처리 (project 영역과 매핑)
        uds_file_names = self.uds_manager.get_uds_file_names()
        widgets.comboBox_uds.clear()
        widgets.comboBox_uds.addItems(uds_file_names)

        # YML 파일의 'project' 값이 있으면 해당 값을 선택
        recent_project_file = self.service_manager.get_recent_project()
        if recent_project_file and recent_project_file in uds_file_names:
            widgets.comboBox_uds.setCurrentText(recent_project_file)

        # DLL 관련 처리
        dll_file_names = self.uds_manager.get_dll_file_names()
        widgets.comboBox_dll.clear()
        widgets.comboBox_dll.addItems(dll_file_names)

        # YML 파일의 'dll' 값이 있으면 해당 값을 선택
        recent_dll_file = self.service_manager.get_recent_dll()
        if recent_dll_file and recent_dll_file in dll_file_names:
            widgets.comboBox_dll.setCurrentText(recent_dll_file)

    
    # PANNEL
    # ///////////////////////////////////////////////////////////////
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
                widget = UIFunctions.create_widget(col_type, options, is_read, read_val, write_val)

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
        if self.user_sent:
            self.error_handler.clear_log()

    def line_edit_changed(self, text, row, col, col_type, widget):
        self.apply_styles(widget, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, text, col_type), col_type)
        self.uds_manager.update_record_value(
            self.record_values, row, col, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, text, col_type)
        )
        self.uds_manager.make_uds_cmd(is_read=False, record_values=self.record_values)
        widgets.lineEdit_cancmd.setText(self.uds_manager.get_uds_cmd())
        if self.user_sent:
            self.error_handler.clear_log()

    def button_clicked(self, checked, row, col, col_type, widget):
        value = 0 if checked else 1
        self.apply_styles(widget, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, value, col_type), col_type)
        widget.setText('Disable' if checked else 'Enable')
        self.uds_manager.update_record_value(
            self.record_values, row, col, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, value, col_type)
        )
        self.uds_manager.make_uds_cmd(is_read=False, record_values=self.record_values)
        widgets.lineEdit_cancmd.setText(self.uds_manager.get_uds_cmd())
        if self.user_sent:
            self.error_handler.clear_log()

    def calendar_changed(self, date, row, col, col_type, widget):
        date_str = date.toString("yyyyMMdd")
        self.apply_styles(widget, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, date_str, col_type), col_type)
        self.uds_manager.update_record_value(
            self.record_values, row, col, self.uds_manager.get_val_for_style_sheet(self.record_values, row, col, date_str, col_type)
        )
        self.uds_manager.make_uds_cmd(is_read=False, record_values=self.record_values)
        widgets.lineEdit_cancmd.setText(self.uds_manager.get_uds_cmd())
        if self.user_sent:
            self.error_handler.clear_log()

    # SEARCH Line Edit
    # ///////////////////////////////////////////////////////////////
    def init_search_completer(self):
        # 검색 데이터 준비: did_map의 클래스 이름과 각 클래스의 record_values 키 및 coloms 키 추가
        self.search_data = self.get_search_data()

        # search_data에서 키와 값들을 한 리스트로 평탄화(flatten)하고 중복 제거
        flattened_search_data = list(set([key for key in self.search_data.keys()] + [item for sublist in self.search_data.values() for item in sublist]))

        # QCompleter 생성 및 설정
        self.completer = QCompleter(flattened_search_data, self)
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
        self.completer.activated.connect(self.handle_search)


    def get_search_data(self):
        search_data = {}

        # 1. did_map의 클래스 이름들 추가
        did_names = self.uds_manager.get_did_names()

        # 딕셔너리로 저장하여 col_key에 해당하는 did_name도 매핑 가능하게 만듦
        for did_name in did_names:
            search_data[did_name] = [did_name]

            self.uds_manager.select_did(did_name)
            record_values = self.uds_manager.get_record_values()

            for data_key, data_info in record_values.items():
                for col_key in data_info['coloms']:
                    if col_key in search_data:
                        # 키가 이미 존재하면 값 리스트에 추가
                        search_data[col_key].append(did_name)
                    else:
                        # 새로운 키를 리스트로 생성
                        search_data[col_key] = [did_name]

        return search_data


    def handle_search(self, search_text):
        # search_text와 매칭되는 DID 이름이나 col_key 찾기
        matching_items = [key for key in self.search_data if search_text.lower() in key.lower()]

        if matching_items:
            matched_did_name = self.search_data[matching_items[0]]

            # matched_did_name이 리스트인 경우 첫 번째 요소를 선택
            if isinstance(matched_did_name, list):
                matched_did_name = matched_did_name[0]

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

            for path in paths:
                if path in sys.path:
                    sys.path.remove(path)
            

        except Exception as e:
            self.error_handler.handle_error(f"Error during application shutdown: {str(e)}")
        
        event.accept()  # 프로그램 종료 허용

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("UTree_80.ico"))
    window = MainWindow()
    sys.exit(app.exec())

    
