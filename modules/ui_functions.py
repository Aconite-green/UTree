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
# ///////////////////////////////////////////////////////////////

# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *
import re
# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class StyleSheets:
    STYLE_SHEET_DEACTIVE = """
        font-size: 12pt;
        border: 1px solid rgb(220, 220, 220);
        background-color: rgb(27, 29, 35);
        padding: 2px;
        text-align: center;  /* 가로 중앙 정렬 */
        vertical-align: middle;
        color: rgb(220, 220, 220); 
    """
    STYLE_SHEET_ACTIVE = """
        font-size: 12pt;
        border: 1px solid  rgb(61, 70, 86);
        background-color: rgb(27, 29, 35);
        color: rgb(135, 206, 250); 
        padding: 2px;
        text-align: center;  /* 가로 중앙 정렬 */
        vertical-align: middle;
        color: rgb(135, 206, 250);
    """


    PUSHBUTTON_STYLE_SHEET_DEACTIVE = """
        QPushButton {
            font-size: 10pt;
            border: 1px solid rgb(220, 220, 220);
            background-color: rgb(61, 70, 86);
            padding: 2px;
        }
        QPushButton:hover {
            background-color: rgb(27, 29, 35);
        }
        QPushButton:pressed {
            background-color: rgb(27, 29, 35);
        }
        QPushButton:checked {
            background-color: rgb(27, 29, 35);
        }
    """

    PUSHBUTTON_DISABLE_0 = """
        QPushButton:disabled { 
            border: 1px solid rgb(61, 70, 86);
            background-color: rgb(27, 29, 35);
        }
    """
    PUSHBUTTON_DISABLE_1 = """
        QPushButton:disabled { 
            border: 1px solid rgb(61, 70, 86);
            background-color: rgb(61, 70, 86); 
        }
    """
    PUSHBUTTON_STYLE_SHEET_ACTIVE = """
        QPushButton {
            font-size: 10pt;
            border: 1px solid rgb(61, 70, 86);
            background-color: rgb(61, 70, 86);
            color: rgb(135, 206, 250);
            padding: 2px;
        }
        QPushButton:hover {
            background-color: rgb(27, 29, 35);
        }
        QPushButton:pressed {
            background-color: rgb(27, 29, 35);
        }
        QPushButton:checked {
            background-color: rgb(27, 29, 35);
        }
    """

    CONNECT_BUTTEN_STYLE_SHEET_ACTIVE = """
        QPushButton {
            background-image: url(:/icons/images/icons/cil-equalizer.png);
            font: 600 12pt "Segoe UI Semibold";
        }
        QPushButton:hover {
            background-color: rgb(27, 29, 35);
        }
        QPushButton:pressed {
            background-color: rgb(27, 29, 35);
        }
        QPushButton:checked {
            background-color: rgb(102, 163, 255);
        }
    """

    CONNECT_BUTTEN_STYLE_SHEET_DEACTIVE = """
        QPushButton {
            background-image: url(:/icons/images/icons/cil-equalizer.png);
            font: 600 12pt "Segoe UI Semibold";
        }
        QPushButton:hover {
            background-color: rgb(27, 29, 35);
        }
        QPushButton:pressed {
            background-color: rgb(27, 29, 35);
        }
        QPushButton:checked {
            background-color: transparent;
        }
    """

    CONFIGUATION_STYLE_SHEET_ACTIVE = """
                        QComboBox {
                            color: rgb(135, 206, 250);
                            background-color: rgb(33, 37, 43);

                        }
                        QComboBox QAbstractItemView {
                            color: rgb(135, 206, 250);
                            background-color: rgb(33, 37, 43);
                        }
                    """
    CONFIGUATION_STYLE_SHEET_DEACTIVE = """
                        QComboBox {
                            color: rgb(221, 221, 221);
                            background-color: rgb(33, 37, 43);
                            border: 1px solid rgb(220, 220, 220);
                        }
                        QComboBox QAbstractItemView {
                            color: rgb(135, 206, 250);
                            background-color: rgb(33, 37, 43);
                        }
                    """

class UIFunctions:
    # MAXIMIZE/RESTORE
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
    def returStatus(self):
        return GLOBAL_STATE

    # SET STATUS
    # ///////////////////////////////////////////////////////////////
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # TOGGLE LEFT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleLeftBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraLeftBox.width()
            widthRightBox = self.ui.extraRightBox.width()
            maxExtend = Settings.LEFT_BOX_WIDTH
            color = Settings.BTN_LEFT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.toggleLeftBox.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.toggleLeftBox.setStyleSheet(style + color)
                # if widthRightBox != 0:
                #     style = self.ui.settingsTopBtn.styleSheet()
                #     self.ui.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))
                
        UIFunctions.start_box_animation(self, width, widthRightBox, "left")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0 

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0       

        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        # self.group.addAnimation(self.right_box)
        self.group.start()

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    # IMPORT THEMES FILES QSS/CSS
    # ///////////////////////////////////////////////////////////////
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.ui.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            #STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

            # CUSTOM GRIPS
            self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        # self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        # self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        # self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    def resize_grips(self):
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    def erase_background():
        result = "background: none;"
        return result
    
    def show_utree_logo():
        result = "background-image: url(:/images/images/images/UTree_1024.png); background-position: center; background-repeat: no-repeat;"
        return result
    
    def menual_info():
        result =  "1. Set Configuration of\n" \
              "   - Project\n" \
              "   - Project Seed Key file\n" \
              "   - CAN\n\n" \
              "2. Click 'Connect'\n\n" \
              "3. Select 'DID'\n" \
              "   e.g) EOL_Coding_R/W\n\n" \
              "4. Select Read or Write\n\n" \
              "5. If 'Write', set values.\n" \
              "   If 'Read', no values needed.\n\n" \
              "6. Click 'Send'\n\n"
        return result

    
    # ///////////////////////////////////////////////////////////////
    # END - GUI DEFINITIONS
        # QComboBox 드롭다운 자동 열림
    
    
    def create_widget(col_type, options, is_read, read_val, write_val):
        widget = None
        current_val = read_val if is_read else write_val

        if col_type == 'combobox':
            widget = QComboBox()
            widget.addItems(list(options.keys()))
            widget.setStyleSheet(StyleSheets.STYLE_SHEET_ACTIVE if read_val is not None and write_val is not None else StyleSheets.STYLE_SHEET_DEACTIVE)
            widget.setEnabled(not is_read)
            if is_read:
                if current_val is not None :
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE 
                elif current_val is not None :
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE
                else:
                    style_sheet = StyleSheets.STYLE_SHEET_DEACTIVE
            else:
                if read_val is not None and write_val is not None : 
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE
                elif read_val is not None and write_val is not None :
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE
                else:
                    style_sheet = StyleSheets.STYLE_SHEET_DEACTIVE
            
            widget.setStyleSheet(style_sheet)
            
            if current_val is not None:
                key = next((k for k, v in options.items() if v == current_val), None)
                if key:
                    widget.setCurrentText(key)

            widget.setEditable(True) 
            widget.lineEdit().setAlignment(Qt.AlignCenter)
            line_edit = widget.lineEdit()
            line_edit.setAlignment(Qt.AlignCenter)
            line_edit.setReadOnly(True)

        elif col_type == 'line_edit':
            widget = QLineEdit()
            widget.setText(str(current_val))
            if is_read:
                if current_val is not None :
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE 
                elif current_val is not None :
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE
                else:
                    style_sheet = StyleSheets.STYLE_SHEET_DEACTIVE
            else:
                if read_val is not None and write_val is not None : 
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE
                elif read_val is not None and write_val is not None :
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE
                else:
                    style_sheet = StyleSheets.STYLE_SHEET_DEACTIVE
            widget.setStyleSheet(style_sheet)
            
            if is_read or options == 'auto':
                widget.setEnabled(False)
            else:
                widget.setEnabled(True)
            widget.setAlignment(Qt.AlignCenter)

        elif col_type == 'text_edit':
            widget = QTextEdit()
            widget.setText(str(current_val))
            if is_read:
                if current_val is not None :
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE 
                elif current_val is not None :
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE
                else:
                    style_sheet = StyleSheets.STYLE_SHEET_DEACTIVE
            else:
                if read_val is not None and write_val is not None : 
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE
                elif read_val is not None and write_val is not None :
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE
                else:
                    style_sheet = StyleSheets.STYLE_SHEET_DEACTIVE
            widget.setStyleSheet(style_sheet)
            widget.setReadOnly(is_read)
            # widget.setEnabled(not is_read)

        elif col_type == 'button':
            widget = QPushButton()
            widget.setEnabled(not is_read)
            widget.setText('Enable' if current_val and current_val == 1 else 'Disable')
            widget.setCheckable(True)
            widget.setMouseTracking(False)

            if is_read:
                if current_val is not None and current_val == 1:
                    style_sheet = StyleSheets.PUSHBUTTON_STYLE_SHEET_ACTIVE + StyleSheets.PUSHBUTTON_DISABLE_1
                elif current_val is not None and current_val == 0:
                    style_sheet = StyleSheets.PUSHBUTTON_STYLE_SHEET_ACTIVE + StyleSheets.PUSHBUTTON_DISABLE_0
                else:
                    style_sheet = StyleSheets.PUSHBUTTON_STYLE_SHEET_DEACTIVE
            else:
                if read_val is not None and write_val is not None and current_val == 1: 
                    style_sheet = StyleSheets.PUSHBUTTON_STYLE_SHEET_ACTIVE + StyleSheets.PUSHBUTTON_DISABLE_1
                elif read_val is not None and write_val is not None and current_val == 0:
                    style_sheet = StyleSheets.PUSHBUTTON_STYLE_SHEET_ACTIVE + StyleSheets.PUSHBUTTON_DISABLE_0
                else:
                    style_sheet = StyleSheets.PUSHBUTTON_STYLE_SHEET_DEACTIVE
            
            widget.setStyleSheet(style_sheet)
            widget.setChecked(False if current_val and current_val == 1 else True)

        elif col_type == 'calendar':
            # QDateEdit 위젯 생성
            date_edit = QDateEdit()
            date_edit.setCalendarPopup(True)
            date_edit.setDisplayFormat("yyyyMMdd")
            date_edit.setAlignment(Qt.AlignCenter)
            date_edit.setEnabled(not is_read)
            date_edit.lineEdit().setReadOnly(True)
            
            # is read & current_val 
            if current_val and isinstance(current_val, str):
                try:
                    # 문자열을 QDate로 변환 (YYYYMMDD 형식)
                    year = int(current_val[:4])
                    month = int(current_val[4:6])
                    day = int(current_val[6:8])
                    qdate = QDate(year, month, day)
                    date_edit.setDate(qdate)
                except ValueError:
                    print(f"Invalid date format: {current_val}")
            else: 
                date_edit.setDate(QDate())

            # 스타일 적용
            
            if is_read:
                if current_val is not None :
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE 
                elif current_val is not None :
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE
                else:
                    style_sheet = StyleSheets.STYLE_SHEET_DEACTIVE
            else:
                if read_val is not None and write_val is not None : 
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE
                elif read_val is not None and write_val is not None :
                    style_sheet = StyleSheets.STYLE_SHEET_ACTIVE
                else:
                    style_sheet = StyleSheets.STYLE_SHEET_DEACTIVE
            date_edit.setStyleSheet(style_sheet)
            
        
            widget = date_edit
        
        if widget:
            widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        return widget

    def update_log(log_widget, is_ok, error_msg, send_msg, recv_msg, type):
        """
        Update the log in plainTextEdit_log with formatted messages.
        """
        def format_message_with_hyphens(msg):
            return '-'.join(re.findall('..', msg.hex().upper()))
        # clear previous log
        log_widget.clear()
         
        # OK 또는 NG 메시지 출력
        if is_ok:
            if type == 'read':
                log_widget.appendHtml(f"""
                <p style="background-color: rgb(33, 37, 43); color: rgb(135, 206, 250); text-align: center; font-size: 16pt; line-height: 1;">
                -------------------------<br>
                |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;OK&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                -------------------------
                </p>
                """)
            elif type == 'write':
                log_widget.appendHtml(f"""
                <p style="background-color: rgb(33, 37, 43); color: rgb(135, 206, 250); text-align: center; font-size: 16pt; line-height: 1;">
                -------------------------<br>
                |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;OK&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                -------------------------
                </p>
                """)
        else:
            if type == 'read':
                log_widget.appendHtml(f"""
                <p style="background-color: rgb(33, 37, 43); color: rgb(255, 0, 0); text-align: center; font-size: 16pt; line-height: 1;">
                -------------------------<br>
                |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;NG&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                -------------------------
                </p>
                """)
            elif type == 'write':
                log_widget.appendHtml(f"""
                <p style="background-color: rgb(33, 37, 43); color: rgb(255, 0, 0); text-align: center; font-size: 16pt; line-height: 1;">
                -------------------------<br>
                |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;NG&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                -------------------------
                </p>
                """)
            elif type == 'connection':
                log_widget.appendHtml(f"""
                <p style="background-color: rgb(33, 37, 43); color: rgb(255, 0, 0); text-align: center; font-size: 16pt; line-height: 1;">
                -------------------------<br>
                |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Connect&nbsp;NG&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                -------------------------
                </p>
                """)
        
        # Error message 출력
        if error_msg:
            log_widget.appendHtml(f"""
                <p style="color: rgb(220, 220, 220); font-size: 12pt;"><b>Error Message</b><br>{error_msg}</p>
            """)
        else:
            log_widget.appendHtml(f"""
                <p style="color: rgb(220, 220, 220); font-size: 12pt;"><b>Error Message</b><br>No Error </p>
            """)

        # Send message 출력
        if send_msg:
            formatted_send_msg = format_message_with_hyphens(send_msg)
            log_widget.appendHtml(f"""
                <p style="color: rgb(220, 220, 220); font-size: 12pt;"><br><b>Sent Message</b><br>{formatted_send_msg}</p>
            """)

        # Receive message 출력
        if recv_msg:
            formatted_recv_msg = format_message_with_hyphens(recv_msg)
            log_widget.appendHtml(f"""
                <p style="color: rgb(220, 220, 220); font-size: 12pt;"><br><b>Received Message</b><br>{formatted_recv_msg}<br><br></p>
            """)








