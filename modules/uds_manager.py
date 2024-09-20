
import logging
import os
import importlib
import sys
from . can_manager import *
from . my_server import *
from msl.loadlib import Client64, Server32
import atexit
import threading

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
        self.error_codes = None
        self.client = None
        self.initialized = False
        self.server_thread = threading.Thread(target=self.initialize_client)
        self.server_thread.start()
        
        # atexit.register(self.client.shutdown_server32)

    # Seed Server
    # ///////////////////////////////////////////////////////////////
    def initialize_client(self):
        try:
            self.client = MyClient()
            self.initialized = True
            atexit.register(self.shutdown)
        except Exception as e:
            self.error_handler.handle_error(f"Failed to initialize MyClient: {str(e)}")

    def shutdown(self):
        if self.client:
            self.client.shutdown_server32()
        if self.server_thread.is_alive():
            self.server_thread.join()

    def generate_key_with_background_init(self, seed):
        if not self.initialized:
            self.server_thread.join()  # 초기화가 끝날 때까지 기다림
        return self.client.generate_key(seed)
    # DID Utility
    # ///////////////////////////////////////////////////////////////
    def get_method(self):
        return self.current_instance.get_method()

    def select_did(self, did_name):
        if self.did_map and did_name in self.did_map:
            cls = self.did_map[did_name]
            self.current_instance = cls()  # 인스턴스 생성
        else:
            # self.error_handler.handle_error(f"DID '{did_name}' not found in did_map.")   
            pass
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
                    read_val = col_info['r_val']  # 읽기 영역 값
                    col_info['w_val'] = read_val  # 쓰기 영역에 복사
        else:
            self.error_handler.handle_error("No current_instance available to copy values.")

    def copy_write_to_read(self):
        if self.current_instance:
            for data_key, data_info in self.current_instance.record_values.items():
                for col_key, col_info in data_info['coloms'].items():
                    write_val = col_info['w_val']  # 쓰기 영역 값
                    col_info['r_val'] = write_val  # 읽기 영역에 복사
        else:
            self.error_handler.handle_error("No current_instance available to copy values.")
    
    def auto_set(self):
        if self.current_instance:
            for data_key, data_info in self.current_instance.record_values.items():
                for col_key, col_info in data_info['coloms'].items():
                    if not isinstance(col_info['options'], dict) and col_info['options'] == 'auto':
                        col_info['w_val'], col_info['r_val'] = 'auto', 'auto'
        else:
            self.error_handler.handle_error("No current_instance available to set auto.")

    def update_record_value(self, record_values, row, col, value):
        if self.current_instance:
            try:
                # record_values의 key와 col에 해당하는 current_val을 업데이트
                record_key = list(record_values.keys())[row]
                col_key = col

                
                record_values[record_key]['coloms'][col_key]['w_val'] = value[0]

                print(record_values[record_key]['coloms'][col_key]['w_val'])
            except KeyError as e:
                self.error_handler.handle_error(f"Error updating record value: {str(e)}")
        else:
            self.error_handler.handle_error("No DID selected or instance not created.")

        return record_values
    
    def get_val_for_style_sheet(self, record_values, row, col, value, col_type):
        if not record_values:
            self.error_handler.handle_error("Record values are empty or None.")
            return None

        try:
            # record_values의 key와 col에 해당하는 current_val을 업데이트
            record_key = list(record_values.keys())[row]
            col_key = col
            if col_type == "combobox":
                col_info = record_values.get(record_key, {}).get('coloms', {}).get(col_key, None)
                options_dict = col_info['options']
                val = options_dict.get(value, None)
            else:
                val = value
            
            read_val = record_values[record_key]['coloms'][col_key]['r_val']
            
            return [val, read_val]

        except Exception as e:
            self.error_handler.handle_error(f"An unexpected error occurred: {str(e)}")
            return None

    def make_uds_cmd(self, is_read, record_values):
        self.process_data.clear()

        
        if is_read:
            self.process_data.extend(self.current_instance.read_service_id)
            self.process_data.extend(self.current_instance.identifier)
        else:
            self.process_data.extend(self.current_instance.write_service_id)
            self.process_data.extend(self.current_instance.identifier)
            self.process_data.extend(self.current_instance.send_parse(record_values))
        
        return True

    def _ssesion_change_seed_reaquest(self):
        # change session
        session_change_request = bytearray([0x10, 0x03])
        self.can_manager.send_message(session_change_request)
        msg = self.can_manager.receive_message()

        if msg is None:
            self.error_handler.handle_error("Timeout during session change request.")
            return False

        # seed request
        seed_request = bytearray([0x27, 0x11])
        self.can_manager.send_message(seed_request)
        msg = self.can_manager.receive_message()

        if msg is None:
            self.error_handler.handle_error("Timeout during seed request.")
            return False

        response_seed = bytearray(msg[-8:])

        # generate key value using the 32-bit server
        response_seed_bytes = bytes.fromhex(response_seed.hex())
        key = self.generate_key_with_background_init(response_seed_bytes)
        send_key = bytearray([0x27, 0x12])
        send_key.extend(key)
        self.can_manager.send_message(send_key)
        msg = self.can_manager.receive_message()

        if msg is None:
            self.error_handler.handle_error("Timeout during key send.")
            return False

        return True

    def process_uds_cmd_read(self, record_values):
        """
        UDS command processing function for read operations.
        """
        self.can_manager.clear_can_buffer()
        is_ok = False
        recv_msg = None
        error_msg = None

        try:
            read_id = self.current_instance.read_service_id
            self.can_manager.send_message(self.process_data)

            response = self.can_manager.receive_message()
            if response:

                if response[0] == (read_id[0] + 0x40):

                    is_ok = True
                    recv_msg = response
                    self.error_handler.log_message(response.hex().upper())
                else:
                    # 부정 응답 처리
                    is_ok = False
                    recv_msg = response
                    error_code = response[2]  # NRC는 보통 응답 메시지의 세 번째 바이트에 있음
                    error_msg = self.error_codes.get(error_code)

            else:
                # Timeout 발생 시 처리
                is_ok = False
                error_msg = "No message recieved, please check HW conection"

            self.current_instance.read_parse(response, record_values)

        except Exception as e:
            self.error_handler.handle_error(f"Error processing UDS read command: {str(e)}")

        return is_ok, self.process_data, recv_msg, error_msg

    def process_uds_cmd_write(self, record_values):
        """
        UDS command processing function for write operations.
        """
        self.can_manager.clear_can_buffer()
        is_ok = False
        recv_msg = None
        error_msg = None
    
        try:
            write_id = self.current_instance.write_service_id
            self._ssesion_change_seed_reaquest()  # 시드 요청 후 키 전송 과정 진행
            self.can_manager.send_message(self.process_data)
    
            response = self.can_manager.receive_message()
    
            if response:
                # 긍정 응답 확인: 첫 번째 바이트가 write_id + 0x40인지 확인
                if response[0] == (write_id[0] + 0x40):
                    is_ok = True
                    recv_msg = response
                    self.error_handler.log_message(response.hex().upper())
                else:
                    # 부정 응답 처리
                    is_ok = False
                    error_code = response[2]  # NRC는 보통 응답 메시지의 세 번째 바이트에 있음
                    recv_msg = response
                    error_msg = self.error_codes.get(error_code)
    
                    
            else:
                # Timeout 발생 시 처리
                is_ok = False
                error_msg = "No message recieved, please check HW conection"
    
        except Exception as e:
            self.error_handler.handle_error(f"Error processing UDS write command: {str(e)}")
    
        return is_ok, self.process_data, recv_msg, error_msg

  
    def get_uds_cmd(self):
        print(self.process_data.hex().upper())
        data = [f'{b:02X}' for b in self.process_data]
        formatted_data = '-'.join(data)
        return formatted_data
    
    def map_combobox_value(self, widget, record_values,col_key):
        # 선택된 텍스트에 해당하는 값을 반환하는 함수
        selected_text = widget.currentText()
        for data_key, data_info in record_values.items():
            if col_key in data_info['coloms']:
                col_info = data_info['coloms'][col_key]
                if col_info['col_type'] == 'combobox':
                    options = col_info['options']
                    return options.get(selected_text, None)
        return None
    
    def validate_value(self):
        return self.current_instance.validate_record_values()
    
    def get_did_method(self):
        return self.current_instance.method
    
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
                    self.did_map = module.did_map
                else:
                    self.error_handler.handle_error(f"Module '{module_name}' does not contain a 'class_map'")
                    self.did_map = None
                
                if hasattr(module, 'negative_response_codes'):
                    self.error_codes = module.negative_response_codes
                else:
                    self.error_handler.handle_error(f"Module '{module_name}' does not contain a 'negative_response_codes'")
                    self.error_codes = None
                
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

        