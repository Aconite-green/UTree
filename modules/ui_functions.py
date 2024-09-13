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
import math
# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class StyleSheets:
    STYLE_SHEET_DEACTIVE = """
        font-size: 10pt;
        border: 1px solid rgb(220, 220, 220);
        background-color: rgb(27, 29, 35);
        padding: 2px;
        text-align: center;  /* 가로 중앙 정렬 */
        vertical-align: middle;
    """
    STYLE_SHEET_ACTIVE = """
        font-size: 10pt;
        border: 2px solid  rgb(61, 70, 86);
        background-color: rgb(27, 29, 35);
        color: rgb(135, 206, 250); 
        padding: 2px;
        text-align: center;  /* 가로 중앙 정렬 */
        vertical-align: middle;
    """

    CALENDAR_STYLE_SHEET_DEACTIVE = """
    /* 달력 위쪽 네비게이션 바의 배경색 */
    QCalendarWidget QWidget#qt_calendar_navigationbar { 
        background-color: rgb(27, 29, 35);  /* 달력 위쪽 배경색 */

    }

    QCalendarWidget QWidget#qt_calendar_calendarview{
        border-left: 1px solid rgb(220, 220, 220);
        border-right: 1px solid rgb(220, 220, 220);
    }

    QCalendarWidget QToolButton::hover {
        color: lightblue; /* 마우스 오버시 색상 */
    }

    /* 날짜 셀의 기본 배경색과 선택된 날짜의 배경색 */
    QCalendarWidget QAbstractItemView {
        background-color: rgb(27, 29, 35);  /* 모든 날짜 셀의 배경색 */
        selection-background-color: rgb(27, 29, 35);  /* 선택한 날짜의 배경색 */
        selection-color: white;
        gridline-color: rgb(27, 29, 35); /* Grid 선 색상 */
    }


    /* 선택된 날짜의 테두리를 하얀색으로 설정 */
    QCalendarWidget QAbstractItemView::item:selected {
        border: 1px solid rgb(220, 220, 220);  /* 선택된 날짜 셀의 테두리만 흰색 */
        background-color: rgb(27, 29, 35);  /* 배경색은 유지 */
    }
"""

    CALENDAR_STYLE_SHEET_ACTIVE = """
    /* 달력 위쪽 네비게이션 바의 배경색 */
    QCalendarWidget QWidget#qt_calendar_navigationbar { 
        background-color: rgb(27, 29, 35);  /* 달력 위쪽 배경색 */
    }

    QCalendarWidget QToolButton::hover {
        color: lightblue; /* 마우스 오버시 색상 */
    }

    /* 날짜 셀의 기본 배경색과 선택된 날짜의 배경색 */
    QCalendarWidget QAbstractItemView {
        background-color: rgb(27, 29, 35);  /* 모든 날짜 셀의 배경색 */
        selection-background-color: rgb(27, 29, 35);  /* 선택한 날짜의 배경색 */
        selection-color: rgb(135, 206, 250);
    }

    /* 날짜 간 구분선(Grid)의 색상 */
    QCalendarWidget QAbstractItemView::item {
        gridline-color: grey;  /* 날짜 간 구분선 색상 설정 */
    }

   
    QCalendarWidget QAbstractItemView::item:selected {
        border: 1px solid rgb(135, 206, 250);  /* 선택된 날짜 셀의 테두리만*/
        background-color: rgb(27, 29, 35);  /* 배경색은 유지 */
        color: rgb(135, 206, 250);
    }
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
            border: 2px solid rgb(61, 70, 86);
            background-color: rgb(27, 29, 35);
        }
    """
    PUSHBUTTON_DISABLE_1 = """
        QPushButton:disabled { 
            border: 2px solid rgb(61, 70, 86);
            background-color: rgb(61, 70, 86); 
        }
    """
    PUSHBUTTON_STYLE_SHEET_ACTIVE = """
        QPushButton {
            font-size: 10pt;
            border: 2px solid rgb(61, 70, 86);
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

class UIFunctions(MainWindow):
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
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

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
    
    # ///////////////////////////////////////////////////////////////
    # END - GUI DEFINITIONS
    def create_widget(col_type, options, is_read, current_val):
        widget = None

        if col_type == 'combobox':
            widget = QComboBox()
            widget.addItems(list(options.keys()))
            widget.setStyleSheet(StyleSheets.STYLE_SHEET_ACTIVE if current_val is not None else StyleSheets.STYLE_SHEET_DEACTIVE)
            widget.setEnabled(not is_read)

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
            widget.setStyleSheet(StyleSheets.STYLE_SHEET_ACTIVE if current_val else StyleSheets.STYLE_SHEET_DEACTIVE)
            if is_read or options == 'auto':
                widget.setEnabled(False)
            else:
                widget.setEnabled(True)
            widget.setAlignment(Qt.AlignCenter)

        elif col_type == 'text_edit':
            widget = QTextEdit()
            widget.setText(str(current_val))
            widget.setStyleSheet(StyleSheets.STYLE_SHEET_ACTIVE if current_val else StyleSheets.STYLE_SHEET_DEACTIVE)
            widget.setEnabled(not is_read)

        elif col_type == 'button':
            widget = QPushButton()
            widget.setEnabled(not is_read)
            widget.setText('1' if current_val is not None and current_val == 1 else '0')
            widget.setCheckable(True)
            widget.setMouseTracking(False)
            if current_val is not None and current_val == 1:
                style_sheet = StyleSheets.PUSHBUTTON_STYLE_SHEET_ACTIVE + StyleSheets.PUSHBUTTON_DISABLE_1
            elif current_val is not None and current_val == 0:
                style_sheet = StyleSheets.PUSHBUTTON_STYLE_SHEET_ACTIVE + StyleSheets.PUSHBUTTON_DISABLE_0
            else:
                style_sheet = StyleSheets.PUSHBUTTON_STYLE_SHEET_DEACTIVE
            widget.setStyleSheet(style_sheet)
            widget.setChecked(True if current_val is not None and current_val == 0 else False)

        elif col_type == 'calendar':
            # 달력 위젯 추가
            calendar_widget = CustomCalendarWidget()
            calendar_widget.setHorizontalHeaderFormat(QCalendarWidget.NoHorizontalHeader)
            calendar_widget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
            calendar_widget.setNavigationBarVisible(True)
            calendar_widget.setGridVisible(False)

            next_month_button = calendar_widget.findChild(QToolButton, 'qt_calendar_nextmonth')
            previous_month_button = calendar_widget.findChild(QToolButton, 'qt_calendar_prevmonth')

            # 버튼을 숨기는 코드 추가
            if next_month_button:
                next_month_button.hide()
            if previous_month_button:
                previous_month_button.hide()
            calendar_widget.setEnabled(not is_read)

            if current_val and isinstance(current_val, str):
                # current_val이 None이 아니고 문자열일 경우 날짜 설정
                calendar_widget.set_active(True)
                try:
                    # 문자열을 QDate로 변환 (YYYYMMDD 형식)
                    year = int(current_val[:4])
                    month = int(current_val[4:6])
                    day = int(current_val[6:8])
                    qdate = QDate(year, month, day)
                    # QDate로 변환한 값을 사용하여 날짜 설정
                    calendar_widget.setSelectedDate(qdate)
                except ValueError:
                    print(f"Invalid date format: {current_val}")
            else:
                calendar_widget.setSelectedDate(QDate())
                calendar_widget.set_active(False)

            calendar_widget.setStyleSheet(StyleSheets.CALENDAR_STYLE_SHEET_ACTIVE if current_val else StyleSheets.CALENDAR_STYLE_SHEET_DEACTIVE)

            widget = calendar_widget  # QFrame을 최종 위젯으로 반환

        if widget:
            widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        return widget

    
class CustomCalendarWidget(QCalendarWidget):
    def __init__(self, *args, **kwargs):
        super(CustomCalendarWidget, self).__init__(*args, **kwargs)
        
        # 현재 월을 저장
        self.current_month = QDate.currentDate().month()
        self.is_active = True  # 기본값으로 활성 상태 설정
        
        # 달이나 연도가 바뀔 때 current_month 업데이트
        self.currentPageChanged.connect(self.update_month)
        self.selectionChanged.connect(lambda: self.handle_date_change(self))
    
    def update_month(self, year, month):
        self.current_month = month

    def paintCell(self, painter, rect, date):
        # 현재 월의 날짜만 표기, 다른 날짜는 상태에 따라 색상 설정
        if date.month() == self.current_month:
            super(CustomCalendarWidget, self).paintCell(painter, rect, date)
        else:
            painter.fillRect(rect, QColor(27, 29, 35))

    def handle_date_change(self, widget):
        # 선택된 날짜를 가져와 yyyyMMdd 형식으로 변환
        selected_date = widget.selectedDate()
        formatted_date = selected_date.toString("yyyyMMdd")
        return formatted_date

    # 활성 상태 설정 메서드
    def set_active(self, active):
        self.is_active = active
        self.update()  # 다시 그리기 요청


