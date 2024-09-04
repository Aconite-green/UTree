import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
# 프로젝트 루트에 있는 중요한 파일들을 포함
files = ['UTree_80.ico', 'main.ui', 'resources.qrc', 'images/', 'modules/', 'config_can/', 'config_uds/']

# TARGET
target = Executable(
    script="main.py",  # main.py가 실행 파일 대상
    base="Win32GUI",   # GUI 프로그램인 경우 Win32GUI를 사용
    icon="UTree_80.ico"  # 아이콘 파일 경로 지정
)

# SETUP CX FREEZE
setup(
    name = "UTree Tool",
    version = "1.0",
    description = "Diagnostic Tool for UTree",
    author = "Your Name",
    options = {'build_exe' : {'include_files' : files}},  # 추가 파일 설정
    executables = [target]
)
