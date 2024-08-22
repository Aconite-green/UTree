class ErrorHandler:
    def __init__(self):
        # 초기화 코드
        pass

    def log_error(self, error_message):
        print(f"Error logged: {error_message}")

    def display_error(self, error_message):
        # GUI에 에러 메시지 표시
        pass

    def handle_critical_error(self, error_message):
        # 치명적인 에러 처리
        self.log_error(error_message)
        self.display_error(error_message)
        # 추가 조치 (예: 통신 중지 등)
