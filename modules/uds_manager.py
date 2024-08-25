
import logging
import os
import importlib
import sys
class UdsManager:
    def __init__(self, uds_directory, error_handler):
        self.uds_directory = os.path.abspath(uds_directory)
        self.error_handler = error_handler
        self.did_map = None
    
    def load_module_classes(self, module_name):
            try:
                # 모듈 경로 설정
                module_path = os.path.join(self.uds_directory, f"{module_name}.py")
                if not os.path.exists(module_path):
                    self.error_handler.handle_error(f"Module file '{module_name}.py' not found in {self.uds_directory}")
                    return None

                # 모듈을 동적으로 로드
                sys.path.insert(0, self.uds_directory)  # 모듈 경로를 sys.path에 추가
                module  = importlib.import_module(module_name)
                sys.path.pop(0)  # 로드 후 경로를 제거
                
                if hasattr(module, 'did_map'):
                    self.did_map = module.did_map  # class_map을 UdsManager의 속성으로 설정
                else:
                    self.error_handler.handle_error(f"Module '{module_name}' does not contain a 'class_map'")
                    self.did_map = None
            except Exception as e:
                self.error_handler.handle_error(f"Failed to load module: {module_name}, Error: {str(e)}")
                return None

    def get_did_names(self):
        if self.did_map is not None:
            return list(self.did_map.keys())
        else:
            self.error_handler.handle_error("DID map is not loaded.")
            return []


    def get_uds_file_names(self):
        try:
            uds_files = [f for f in os.listdir(self.uds_directory) if f.endswith('.py') and f != 'uds_base.py']
            return [os.path.splitext(filename)[0] for filename in uds_files]
        except Exception as e:
            self.error_handler.handle_error(f"Error getting UDS file names: {str(e)}")
            return []