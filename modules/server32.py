import os
import ctypes
import sys
from msl.loadlib import Server32

class MyServer(Server32):
    """Wrapper around a 32-bit C++ library that dynamically loads DLLs."""

    def __init__(self, host, port, **kwargs):
        try:
            # Get the directory of the current file
            root_dir = os.path.dirname(os.path.abspath(__file__))

            # Construct the path to the config_dll folder
            self.dll_dir = os.path.join(root_dir, '..', 'config_dll')

            # List all files in config_dll and find the first DLL file
            dll_files = [f for f in os.listdir(self.dll_dir) if f.endswith('.dll')]

            if not dll_files:
                raise FileNotFoundError(f"No DLL files found in {self.dll_dir}")

            # Use the first DLL file found
            selected_dll = dll_files[0]
            selected_dll_path = os.path.join(self.dll_dir, selected_dll)

            # Initialize the server with the selected DLL
            super(MyServer, self).__init__(selected_dll_path, 'cdll', host, port)

        except Exception as e:
            raise  # 에러 발생 시 다시 발생시켜 에러 추적 가능하게 함

    def generate_key(self, seed, dll_name):
        try:
            selected_dll_path = os.path.join(self.dll_dir, dll_name + ".dll")
            lib = ctypes.CDLL(selected_dll_path)
            lib.ASK_KeyGenerate.restype = ctypes.c_uint
            lib.ASK_KeyGenerate.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

            key = ctypes.create_string_buffer(8)
            lib.ASK_KeyGenerate(seed, key)

        except Exception as e:
            return None, None, f"Error during generate_key: {e}"

        return key.raw, selected_dll_path, None
