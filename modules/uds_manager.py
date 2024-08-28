
import logging
import os
import importlib
import sys
from . can_manager import *
from msl.loadlib import Client64, Server32

class MyClient(Client64):
    def __init__(self):
        try:
            print("Initializing MyClient...")
            super(MyClient, self).__init__(module32='my_server')
            print("MyClient initialized successfully.")
        except Exception as e:
            print(f"An error occurred in MyClient initialization: {e}")
            raise

    def generate_key(self, seed):
        return self.request32('generate_key', seed)

class UdsManager:
    def __init__(self ,uds_directory, error_handler, can_manager):
        self.uds_directory = os.path.abspath(uds_directory)
        self.error_handler = error_handler
        self.can_manager = can_manager
        self.did_map = None
        self.process_data = bytearray()
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
    
    def copy_read_to_write(self):
        if self.current_instance:
            for data_key, data_info in self.current_instance.record_values.items():
                for col_key, col_info in data_info['coloms'].items():
                    read_val = col_info['current_val'][1]  # 읽기 영역 값
                    col_info['current_val'][2] = read_val  # 쓰기 영역에 복사
        else:
            self.error_handler.handle_error("No current_instance available to copy values.")

    def update_record_value(self, row, col, value, is_read):
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

                # print(self.current_instance.record_values[record_key]['coloms'][col_key]['current_val'])
            except KeyError as e:
                self.error_handler.handle_error(f"Error updating record value: {str(e)}")
        else:
            self.error_handler.handle_error("No DID selected or instance not created.")

    def make_uds_cmd(self, is_read):
        self.process_data.clear()

        
        if is_read:
            self.process_data.extend(self.current_instance.read_service_id)
            self.process_data.extend(self.current_instance.identifier)
        else:
            self.process_data.extend(self.current_instance.write_service_id)
            self.process_data.extend(self.current_instance.identifier)
            # 여기에 record_value 추가하는 함수 작성
        
        return True

    def _ssesion_change_seed_reaquest(self):
        
        # change session
        session_change_request = bytearray([0x10, 0x03])
        self.can_manager.send_message(session_change_request)
        self.can_manager.receive_message()

        # seed request
        seed_request = bytearray([0x27, 0x11])
        self.can_manager.send_message(seed_request)
        msg = self.can_manager.receive_message()
        response_seed = bytearray(msg[-8:])

        # generate key value using the 32-bit server
        client = MyClient()
        response_seed_bytes = bytes.fromhex(response_seed.hex())
        key = client.generate_key(response_seed_bytes)
        send_key = bytearray([0x27, 0x12])
        send_key.extend(key)
        self.can_manager.send_message(session_change_request)
        self.can_manager.receive_message()
        client.shutdown_server32()
    
    def process_uds_cmd(self, is_read, record_values):
        try:
            
            self.can_manager.send_message(self.process_data)
            response = self.can_manager.receive_message()
            if is_read:
                self.current_instance.read_parse(response, record_values)
            return True

        except Exception as e:
            self.error_handler.handle_error(f"Error processing UDS command: {str(e)}")
            return False
    
    
    def get_uds_cmd(self):
        data = [f'0x{b:02x}' for b in self.process_data]
        formatted_data = ', '.join(data)
        return formatted_data
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