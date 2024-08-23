class ErrorHandler:
    def __init__(self, log_widget=None):
        """
        ErrorHandler 초기화 함수. 
        log_widget은 QPlainTextEdit와 같은 로그를 출력할 위젯입니다.
        """
        self.log_widget = log_widget

    def handle_error(self, error_message):
        """
        오류를 처리하고, 메시지를 log_widget에 표시합니다.
        """
        if self.log_widget:
            self.log_widget.appendPlainText(f"[Error] {error_message}")
        else:
            print(f"Error: {error_message}")

    def log_message(self, message):
        self.log_widget.appendPlainText(f"{message}")