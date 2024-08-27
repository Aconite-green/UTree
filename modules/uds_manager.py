
import logging
import os
import importlib
import sys
from . can_manager import *

class UdsManager:
    def __init__(self ,uds_directory, error_handler, can_manager):
        self.uds_directory = os.path.abspath(uds_directory)
        self.error_handler = error_handler
        self.did_map = None
        self.can_manager = can_manager
        self.current_instance = None  



    # DID Utility
    # ///////////////////////////////////////////////////////////////
    def select_did(self, did_name):
        if self.did_map and did_name in self.did_map:
            cls = self.did_map[did_name]
            self.current_instance = cls()  # 인스턴스 생성
        else:
            self.error_handler.handle_error(f"DID '{did_name}' not found in did_map.")   
    
    def get_record_values(self):
        if self.current_instance:
            return self.current_instance.get_record_values()
        else:
            self.error_handler.handle_error("No DID selected or instance not created.")
            return {}
    
    def update_record_value(self, row, col, value, is_read):
        """현재 선택된 DID 클래스의 record_values를 업데이트"""
        if self.current_instance:
            try:
                # record_values의 key와 col에 해당하는 current_val을 업데이트
                record_key = list(self.current_instance.record_values.keys())[row]
                col_key = col

                # 읽기 모드인지 쓰기 모드인지에 따라 current_val의 위치를 변경
                if is_read:
                    # 읽기 모드인 경우, current_val의 첫 번째 인자(인덱스 1)를 업데이트
                    self.current_instance.record_values[record_key]['coloms'][col_key]['current_val'][1] = value
                else:
                    # 쓰기 모드인 경우, current_val의 두 번째 인자(인덱스 2)를 업데이트
                    self.current_instance.record_values[record_key]['coloms'][col_key]['current_val'][2] = value

                print(f"Updated {record_key} - {col_key}: {value} (is_read={is_read})")
            except KeyError as e:
                self.error_handler.handle_error(f"Error updating record value: {str(e)}")
        else:
            self.error_handler.handle_error("No DID selected or instance not created.")



    # INIT CONFIG UDS FILES
    # ///////////////////////////////////////////////////////////////
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