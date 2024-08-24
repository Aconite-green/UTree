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

        # LOAD YML FILES
        # ///////////////////////////////////////////////////////////////
        
        
        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # CONNECT BUTTON
        widgets.btn_connect.clicked.connect(self.handle_connect)
        widgets.btn_send.clicked.connect(self.send_connect)
        
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # Initialize Modules
        self.error_handler = ErrorHandler(log_widget=widgets.plainTextEdit_log)
        self.can_manager = CanManager('./config_can', self.error_handler)

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
                selected_can_file = widgets.comboBox_can.currentText()               
                self.can_manager.get_selected_can_yml(selected_can_file)
                self.can_manager.setup_can()
                self.can_manager.start_communication()

                widgets.stackedWidget.setCurrentWidget(widgets.widgets_workspace)
                widgets.groupBox_pannel.setVisible(True)
                widgets.pagesContainer.setStyleSheet(UIFunctions.erase_background())
            except Exception as e:
                self.error_handler.handle_error(str(e))
    
    def send_connect(self):
        # btn = self.sender()
        try:
            test_msg = bytearray([0x22, 0x00, 0x80])
            self.can_manager.send_message(test_msg)
            self.can_manager.receive_message()
        except Exception as e:
                self.error_handler.handle_error(str(e))
        
    # INIT YML
    # ///////////////////////////////////////////////////////////////
    def populateComboBoxes(self):
        self.can_manager.load_yml_files()
        
        # Populate comboBox_can with CAN YML file names
        can_file_names = self.can_manager.get_can_file_names()
        widgets.comboBox_can.clear()
        widgets.comboBox_can.addItems(can_file_names)

        # 필요에 따라 UDS 관련 comboBox도 추가 가능
        # uds_file_names = self.loader.get_uds_file_names()
        # widgets.comboBox_uds.clear()
        # widgets.comboBox_uds.addItems(uds_file_names)

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
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
