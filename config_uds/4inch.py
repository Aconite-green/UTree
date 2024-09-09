from uds_base import UDSBase

class EOLCoding(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [0x2E]
        identifier = [0x00, 0x60]
        method = ('r', 'w')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': {'coloms':{'ECO':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'EPB':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'AHLS':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'MDPS':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'ESC':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'TPMS':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'NORMAL':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'ECS':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]}}
            },
            'data2': {'coloms':{'ABS':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'AIRBAG':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'PSB':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'AFL':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                '4WD':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'AT':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'SPORT':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'eCall':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]}}
            },
            'data3': {'coloms':{'FuelType':{'bit':2, 'type':['combobox', {'GSL':0b00,'DSL':0b01,'LPI':0b10,'OTHERS':0b11}],'current_val': ['bool',None, None]},
                                'Speedometer Type':{'bit':2, 'type':['combobox', {'KPH':0b00,'KMPH':0b01,'MKPH':0b10}],'current_val': ['bool',None, None]},
                                'Area':{'bit':4, 'type':['combobox', {'DOM': 0b0000, 'GEN': 0b0001, 'MID': 0b0010, 'EEC': 0b0011, 'AUS': 0b0100, 'CAN': 0b0101, 'USA': 0b0110, 'CHINA': 0b0111, 
                                                                      'RUSSIA': 0b1000, 'INDIA': 0b1001, 'BRAZIL': 0b1010, 'MEX': 0b1011, 'INDONESIA': 0b1100, 'JAPAN ': 0b1101}],
                                        'current_val': ['bool',None, None]}}
            },
            'data4': {'coloms':{'Multifunction Type2':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'Power Type': {'bit': 3, 'type': ['combobox', {'ICV': 0b000, 'HEV': 0b001, 'PHEV': 0b010, 'EV': 0b011, 'FCEV': 0b100}], 'current_val': ['bool', None, None]},
                                'High Performance Type':{'bit':2, 'type':['combobox', {'OFF': 0b00, 'HIGH_PERFORMANCE': 0b01, 'N': 0b10}],'current_val': ['bool',None, None]},
                                'reserved':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'Autolight':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]}}
            },
            'data5': {'coloms':{'Multifunction Type':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                               'Maximum Indicated Speed': {'bit': 3, 'type': ['combobox', {'KPH_260': 0b000, 'KPH_160': 0b001, 'KPH_220': 0b010, 'KPH_300': 0b011}], 'current_val': ['bool', None, None]},
                                'HUD':{'bit':1, 'type':['button',0],'current_val': ['bool',None, None]},
                                'Fuel Tank Size': {'bit': 2, 'type': ['combobox', {'TANK_A': 0b00, 'TANK_B': 0b01, 'TANK_C': 0b10, 'TANK_D': 0b11}], 'current_val': ['bool', None, None]},
                                'ICC':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]}}
            },
            'data6': {'coloms':{'RSBR': {'bit': 3, 'type': ['combobox', {'NONE': 0b000, 'R2_P2': 0b001, 'R2_P3': 0b010, 'R2_P2_R3_P2': 0b011, 'R2_P3_R3_P2': 0b100,'R2_P2_R3_P3': 0b101, 'R2_P3_R3_P3': 0b110}], 'current_val': ['bool', None, None]},
                                'Body Type': {'bit': 3, 'type': ['combobox', {'SEDAN': 0b000, 'SUV': 0b001, 'MPV': 0b010, 'WAGON': 0b011, 'HATCHBACK': 0b100, 'PICKUP_TRUCK': 0b101, 'TYPE_G': 0b110, 'TYPE_H': 0b111}], 'current_val': ['bool', None, None]},
                                'reserved':{'bit':2, 'type':['button', 0],'current_val': ['bool',None, None]}}
            },
            'data7': {'coloms':{'FCA':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'FCA2':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'LKA':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'ISLA':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'DAW':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'SCC':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'LFA':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'HDA':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]}}
            },
            'data8': {'coloms':{'HDA2':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'HDP':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'Emergency Stop':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'PDW':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'reserved':{'bit':4, 'type':['button', 0],'current_val': ['bool',None, None]}}        
            }
            
            }
        
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray) or len(can_message) < 2:
            raise ValueError("Invalid CAN message")

        # Service ID와 Identifier 길이를 계산
        header_length = len(self.read_service_id) + len(self.identifier)

        # 데이터 페이로드 시작 부분을 설정
        payload_start = header_length

        # 실제 데이터 페이로드 추출
        data_payload = can_message[payload_start:]
        
        byte_index = 0
        bit_offset = 0
        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']
                current_value = 0

                # 필요한 비트 수만큼 값을 추출
                for _ in range(bit_size):
                    if bit_offset == 8:
                        byte_index += 1
                        bit_offset = 0

                    byte_value = data_payload[byte_index]  # 현재 바이트 값을 읽어옴
                    binary_representation = format(byte_value, '08b')
                    # print(binary_representation)
                    bit = (byte_value >> (7 - bit_offset)) & 1
                    current_value = (current_value << 1) | bit

                    bit_offset += 1

                # 추출한 값을 record_values의 current_val에 업데이트
                col_info['current_val'][1] = current_value

            # 모든 비트가 사용된 후, byte_index를 다음 바이트로 이동
            if bit_offset > 0:
                byte_index += 1
                bit_offset = 0
    
    def send_parse(self, record_values):
        byte_array = bytearray()
        current_byte = 0
        bit_offset = 0
    
        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']
                write_val = col_info['current_val'][2]  # 쓰기 영역 값
                
                if write_val is None:
                    write_val = 0  # None이면 0으로 대체
    
                # 각 비트별로 값을 byte_array에 저장
                for i in range(bit_size):
                    bit = (write_val >> (bit_size - 1 - i)) & 1
                    current_byte = (current_byte << 1) | bit
                    bit_offset += 1
    
                    # 현재 바이트가 채워졌다면 byte_array에 추가
                    if bit_offset == 8:
                        byte_array.append(current_byte)
                        current_byte = 0
                        bit_offset = 0
    
        # 남아 있는 비트들이 있으면 마지막 바이트에 추가
        if bit_offset > 0:
            current_byte = current_byte << (8 - bit_offset)  # 남은 비트들을 0으로 채움
            byte_array.append(current_byte)
    
        return byte_array

class CarInfo(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [0x2E]
        identifier = [0x00, 0x80]
        method = ('r', 'w')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 'coloms':{ 'dealer_id(ASCII 5byte)':{'bit':40, 'type':['line_edit', "default"],'current_val': [5,"", ""]}}},
            'data2': { 'coloms':{ 'date(DEC 4byte, YYYYMMDD)':{'bit':32, 'type':['line_edit', "default"],'current_val': [8,"", ""]}}},
            'data3': { 'coloms':{ 'milage(DEC)':{'bit':32, 'type':['line_edit', "default"],'current_val': [6,"", ""]}}},
            'data4': { 'coloms':{ 'checksum':{'bit':8, 'type':['line_edit', "default"],'current_val': [27,"", ""]}}},
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray) or len(can_message) < 16:
            raise ValueError("Invalid CAN message")

        # Service ID와 Identifier 길이를 계산
        header_length = len(self.read_service_id) + len(self.identifier)

        # 데이터 페이로드 시작 부분을 설정
        payload_start = header_length

        # 실제 데이터 페이로드 추출
        data_payload = can_message[payload_start:]

        byte_index = 0

        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']
                byte_size = bit_size // 8  # bit를 byte로 변환

                # 값을 추출하여 current_val[1]에 업데이트
                extracted_bytes = data_payload[byte_index:byte_index + byte_size]

                if col_key == 'dealer_id(ASCII 5byte)':
                    try:
                        # ASCII로 변환
                        current_value = extracted_bytes.decode('ascii')             
                        # '\x00\x00\x00\x00\x00'인 경우 None으로 설정
                        if extracted_bytes == b'\x00\x00\x00\x00\x00':
                            current_value = "Not Set"                
                    except UnicodeDecodeError:
                        # ASCII로 변환할 수 없는 경우 None으로 설정
                        current_value = "Not Set"

                elif col_key == 'date(DEC 4byte, YYYYMMDD)':
                    if extracted_bytes == b'\x00\x00\x00\x00':
                        current_value = "Not Set"
                    else:
                        current_value = hex(int.from_bytes(extracted_bytes, byteorder='big'))[2:].upper()
                elif col_key == 'milage(DEC)':
                    if extracted_bytes == b'\x00\x00\x00\x00':
                        current_value = "Not Set"
                    else:
                        # 정수형으로 변환
                        current_value = int.from_bytes(extracted_bytes, byteorder='big')
                elif col_key == 'checksum':
                    current_value = "For Write Method (Auto Set)"
                else:
                    # 기본 정수형 처리
                    current_value = int.from_bytes(extracted_bytes, byteorder='big')

                col_info['current_val'][1] = current_value

                byte_index += byte_size  # 다음 데이터로 이동

    def send_parse(self, record_values):
        byte_array = bytearray()

        # 1. 딜러 ID (DealerID, 5Byte, ASCII)
        dealer_id = record_values['data1']['coloms']['dealer_id(ASCII 5byte)']['current_val'][2]
        if dealer_id is None:
            dealer_id = ''
        dealer_id_bytes = dealer_id.encode('ascii')
        byte_array.extend(dealer_id_bytes.ljust(5, b'\x00'))  # 5바이트로 맞추기 위해 0으로 패딩

        # 2. 수정 날짜 (Date, 4Byte, DEC)
        date = record_values['data2']['coloms']['date(DEC 4byte, YYYYMMDD)']['current_val'][2]

        try:
            # date를 문자열로 변환한 후, 각 부분을 분리
            date_str = str(int(date))  # date가 숫자 형태로 변환 가능한 경우 변환, 그렇지 않으면 예외 처리
            if len(date_str) == 8:
                date_str

                # 각각의 값을 바이트로 변환하여 결합
                date_bytes = bytes([int(date_str[:2], 16), int(date_str[2:4], 16), int(date_str[4:6], 16), int(date_str[6:], 16)])
            else:
                raise ValueError("Invalid date format")
        except (ValueError, TypeError):
            # 변환이 불가능한 경우 0x00000000으로 설정
            date_bytes = b'\x00\x00\x00\x00'

        byte_array.extend(date_bytes)

        

        # 3. 오도미터 (Mileage, 4Byte, HEX → DEC 변환)
        mileage_bytes = b'\x00\x00\x00\x00'  # 기본값 초기화
        mileage = record_values['data3']['coloms']['milage(DEC)']['current_val'][2]
        try:
            mileage = int(mileage)
            mileage = min(mileage, 1599999)  # km 사양 기준으로 최대 값 제한
            mileage_bytes = mileage.to_bytes(4, byteorder='big')
            print(mileage_bytes.hex().upper())
            
        except (ValueError, TypeError):
            mileage_bytes = b'\x00\x00\x00\x00'  # 오류 발생 시 기본값 설정

        byte_array.extend(mileage_bytes)

        # 4. Check Sum (1Byte)
        # Checksum 계산 방법:
        # 딜러 ID, 수정 날짜, 오도미터 값의 전체 합을 계산하고, 마지막 2자리의 인버트 값을 계산
        checksum = 0
        for byte in byte_array:
            checksum += byte
        checksum = checksum & 0xFF  # 전체 합의 마지막 1바이트 추출
        checksum = ~checksum & 0xFF  # Invert (보수 계산)
        byte_array.append(checksum)

        return byte_array

class ECUReset(UDSBase):
    def __init__(self):
        read_service_id = [None]
        write_service_id = [0x11]
        identifier = [0x01]
        method = ('w')
        dll_path = None
        record_values = {
            'data1': { 'coloms':{ 'ECU_reset':{'bit':8, 'type':['line_edit', "default"],'current_val': [10,"press send", "press send"]}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)
    
    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray) or len(can_message) < 16:
            raise ValueError("Invalid CAN message")
    
    def send_parse(self, record_values):
        byte_array = bytearray()

        
        return byte_array

class UnlockNotCoded(UDSBase):
    def __init__(self):
        read_service_id = [None]
        write_service_id = [0x3D]
        identifier = [0x24,0x50, 0x00, 0x10, 0x36, 0x00, 0x01, 0x00]
        method = ('w')
        dll_path = None
        record_values = {
            'data1': { 'coloms':{ 'Unlock Not Coded':{'bit':8, 'type':['line_edit', "default"],'current_val': [10,"press send", "press send"]}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)
    
    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray) or len(can_message) < 16:
            raise ValueError("Invalid CAN message")
    
    def send_parse(self, record_values):
        byte_array = bytearray()
        return byte_array

class LockNotCoded(UDSBase):
    def __init__(self):
        read_service_id = [None]
        write_service_id = [0x3D]
        identifier = [0x24,0x50, 0x00, 0x10, 0x36, 0x00, 0x01, 0x01]
        method = ('w')
        dll_path = None
        record_values = {
            'data1': { 'coloms':{ 'Lock Not Coded':{'bit':8, 'type':['line_edit', "default"],'current_val': [10,"press send", "press send"]}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)
    
    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray) or len(can_message) < 16:
            raise ValueError("Invalid CAN message")
    
    def send_parse(self, record_values):
        byte_array = bytearray()
        return byte_array

class InitVIN(UDSBase):
    def __init__(self):
        read_service_id = [None]
        write_service_id = [0x2E]
        identifier = [0xF1, 0x10]
        method = ('w')
        dll_path = None
        record_values = {
            'data1': { 'coloms':{ 'InitVIN':{'bit':8, 'type':['line_edit', "default"],'current_val': [10,"press send", "press send"]}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)
    
    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray) or len(can_message) < 16:
            raise ValueError("Invalid CAN message")
    
    def send_parse(self, record_values):
        byte_array = bytearray()
        byte_array.extend([0x00])
        return byte_array

class VIN(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [0x2E]
        identifier = [0xF1, 0x90]
        method = ('w', 'r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 'coloms':{ 'VIN':{'bit':136, 'type':['line_edit', "default"],'current_val': [17,None, None]}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray) or len(can_message) < 16:
            raise ValueError("Invalid CAN message")

        # Service ID와 Identifier 길이를 계산
        header_length = len(self.read_service_id) + len(self.identifier)

        # 데이터 페이로드 시작 부분을 설정
        payload_start = header_length

        # 실제 데이터 페이로드 추출
        data_payload = can_message[payload_start:]

        byte_index = 0

        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']
                byte_size = bit_size // 8  # bit를 byte로 변환

                # 값을 추출하여 current_val[1]에 업데이트
                extracted_bytes = data_payload[byte_index:byte_index + byte_size]
                if col_key == 'VIN':
                    try:
                        # ASCII로 변환
                        current_value = extracted_bytes.decode('ascii')             
                        # '\x00\x00\x00\x00\x00'인 경우 None으로 설정
                        if extracted_bytes == b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00':
                            current_value = "Not Set"                
                    except UnicodeDecodeError:
                        # ASCII로 변환할 수 없는 경우 None으로 설정
                        current_value = "Not Set"
                else:
                    # 기본 정수형 처리
                    current_value = int.from_bytes(extracted_bytes, byteorder='big')

                col_info['current_val'][1] = current_value

                byte_index += byte_size  # 다음 데이터로 이동

    def send_parse(self, record_values):
        byte_array = bytearray()

        # 1. 딜러 ID (DealerID, 5Byte, ASCII)
        vin_num = record_values['data1']['coloms']['VIN']['current_val'][2]
        if vin_num is None:
            vin_num = ''
        vin_bytes = vin_num.encode('ascii')
        byte_array.extend(vin_bytes.ljust(17, b'\x00'))  # 5바이트로 맞추기 위해 0으로 패딩


        return byte_array

class SetServiceType(UDSBase):
    def __init__(self):
        read_service_id = [None]
        write_service_id = [0x2E]
        identifier = [0x00, 0x70]
        method = ('w')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
           
            'data1': {'coloms':{'Service Type':{'bit':8, 'type':['combobox', {'Set by Customer':0b00,'Set by Workshop':0b01}],'current_val': ['bool',None, None]}
            
            }
            }
            }
        
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray) or len(can_message) < 2:
            raise ValueError("Invalid CAN message")
    
    def send_parse(self, record_values):
        byte_array = bytearray()
        current_byte = 0
        bit_offset = 0
    
        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']
                write_val = col_info['current_val'][2]  # 쓰기 영역 값
                
                if write_val is None:
                    write_val = 0  # None이면 0으로 대체
    
                # 각 비트별로 값을 byte_array에 저장
                for i in range(bit_size):
                    bit = (write_val >> (bit_size - 1 - i)) & 1
                    current_byte = (current_byte << 1) | bit
                    bit_offset += 1
    
                    # 현재 바이트가 채워졌다면 byte_array에 추가
                    if bit_offset == 8:
                        byte_array.append(current_byte)
                        current_byte = 0
                        bit_offset = 0
    
        # 남아 있는 비트들이 있으면 마지막 바이트에 추가
        if bit_offset > 0:
            current_byte = current_byte << (8 - bit_offset)  # 남은 비트들을 0으로 채움
            byte_array.append(current_byte)
    
        return byte_array

class InitService(UDSBase):
    def __init__(self):
        read_service_id = [None]
        write_service_id = [0x2E]
        identifier = [0x00, 0x71]
        method = ('w')
        dll_path = None
        record_values = {
            'data1': { 'coloms':{ 'Lock Not Coded':{'bit':8, 'type':['line_edit', "default"],'current_val': [43,None, "Press Send to Reset Service distance/time"]}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)
    
    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray) or len(can_message) < 16:
            raise ValueError("Invalid CAN message")
    
    def send_parse(self, record_values):
        byte_array = bytearray([0x00])
        return byte_array

class SetServiceDistance(UDSBase):
    def __init__(self):
        read_service_id = [None]
        write_service_id = [0x2E]
        identifier = [0x00, 0x72]
        method = ('w')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 'coloms':{ 'Service_Distance(DEC, 0~99999 Km or Mile)':{'bit':24, 'type':['line_edit', "default"],'current_val': [5,None, None]}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray) or len(can_message) < 16:
            raise ValueError("Invalid CAN message")


    def send_parse(self, record_values):
        byte_array = bytearray()

        service_dis = record_values['data1']['coloms']['Service_Distance(DEC, 0~99999 Km or Mile)']['current_val'][2]
        service_dis_bytes = b'\x00\x00\x00'
        try:
            service_dis = int(service_dis)
            service_dis = min(service_dis, 99999)  # km 사양 기준으로 최대 값 제한
            service_dis_bytes = service_dis.to_bytes(3, byteorder='big')
            print(service_dis_bytes.hex().upper())
            
        except (ValueError, TypeError):
            service_dis_bytes = b'\x00\x00\x00'  # 오류 발생 시 기본값 설정

        byte_array.extend(service_dis_bytes)

        return byte_array

class SetServiceTerm(UDSBase):
    def __init__(self):
        read_service_id = [None]
        write_service_id = [0x2E]
        identifier = [0x00, 0x73]
        method = ('w')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 'coloms':{ 'Service_Term(DEC, 0~99 Month)':{'bit':16, 'type':['line_edit', "default"],'current_val': [2,None, ""]}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray) or len(can_message) < 16:
            raise ValueError("Invalid CAN message")


    def send_parse(self, record_values):
        byte_array = bytearray()

        service_term = record_values['data1']['coloms']['Service_Term(DEC, 0~99 Month)']['current_val'][2]
        service_term_bytes = b'\x00\x00'
        try:
            service_term = int(service_term)
            service_term = min(service_term, 99)  # km 사양 기준으로 최대 값 제한
            service_term_bytes = service_term.to_bytes(2, byteorder='big')
            print(service_term_bytes.hex().upper())
            
        except (ValueError, TypeError):
            service_term_bytes = b'\x00\x00'  # 오류 발생 시 기본값 설정

        byte_array.extend(service_term_bytes)

        return byte_array

class CANDBVer(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xF1, 0x00]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 'coloms':{ 'Data_Record':{'bit':24, 'type':['line_edit', "default"],'current_val': [5,None, ""]}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        
        if not isinstance(can_message, bytearray):
            raise ValueError("Invalid CAN message")

        # Service ID와 Identifier 길이를 계산
        header_length = len(self.read_service_id) + len(self.identifier)

        # 데이터 페이로드 시작 부분을 설정
        payload_start = header_length

        # 실제 데이터 페이로드 추출
        data_payload = can_message[payload_start:]

        byte_index = 0

        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']
                byte_size = bit_size // 8  # bit를 byte로 변환

                # 값을 추출하여 current_val[1]에 업데이트
                extracted_bytes = data_payload[byte_index:byte_index + byte_size]

                if col_key == 'Data_Record':
                    try:
                        # ASCII로 변환
                        ascii_value = extracted_bytes.decode('ascii')
                        current_value = '.'.join(ascii_value)
                    except UnicodeDecodeError:
                        # ASCII로 변환할 수 없는 경우 None으로 설정
                        current_value = None
                    else:
                        # '\x00\x00\x00'인 경우 None으로 설정
                        if extracted_bytes == b'\x00\x00\x00':
                            current_value = None
                    finally:
                        # current_value를 그대로 저장 (이미 ASCII로 변환된 상태)
                        col_info['current_val'][1] = current_value
                else:
                    # 기본 정수형 처리
                    current_value = int.from_bytes(extracted_bytes, byteorder='big')
                    col_info['current_val'][1] = current_value

                byte_index += byte_size  # 다음 데이터로 이동


    def send_parse(self, record_values):
        byte_array = bytearray()
        return byte_array

class EtherDBVer(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xF1, 0x01]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 'coloms':{ 'Data_Record':{'bit':24, 'type':['line_edit', "default"],'current_val': [8,"", ""]}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray):
            raise ValueError("Invalid CAN message")

        # Service ID와 Identifier 길이를 계산
        header_length = len(self.read_service_id) + len(self.identifier)

        # 데이터 페이로드 시작 부분을 설정
        payload_start = header_length

        # 실제 데이터 페이로드 추출
        data_payload = can_message[payload_start:]

        byte_index = 0

        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']
                byte_size = bit_size // 8  # bit를 byte로 변환

                # 값을 추출하여 current_val[1]에 업데이트
                extracted_bytes = data_payload[byte_index:byte_index + byte_size]

                if col_key == 'Data_Record':
                    try:
                        # DEC 포맷으로 변환
                        current_value = f"{int(extracted_bytes[0]):02}.{int(extracted_bytes[1]):02}.{int(extracted_bytes[2]):02}"
                    except (ValueError, IndexError):
                        # 변환에 실패한 경우 None으로 설정
                        current_value = None
                    finally:
                        # 변환된 값을 저장
                        col_info['current_val'][1] = current_value
                else:
                    # 기본 정수형 처리
                    current_value = int.from_bytes(extracted_bytes, byteorder='big')
                    col_info['current_val'][1] = current_value

                byte_index += byte_size  # 다음 데이터로 이동


    def send_parse(self, record_values):
        byte_array = bytearray()
        return byte_array

class ClusterProductionCode(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xF1, 0xA1]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 'coloms':{ 'Data_Record':{'bit':32, 'type':['line_edit', "default"],'current_val': [4,"", None]}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        
        if not isinstance(can_message, bytearray):
            raise ValueError("Invalid CAN message")

        # Service ID와 Identifier 길이를 계산
        header_length = len(self.read_service_id) + len(self.identifier)

        # 데이터 페이로드 시작 부분을 설정
        payload_start = header_length

        # 실제 데이터 페이로드 추출
        data_payload = can_message[payload_start:]

        byte_index = 0

        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']
                byte_size = bit_size // 8  # bit를 byte로 변환

                # 값을 추출하여 current_val[1]에 업데이트
                extracted_bytes = data_payload[byte_index:byte_index + byte_size]

                if col_key == 'Data_Record':
                    try:
                        # ASCII로 변환
                        current_value = extracted_bytes.decode('ascii')
                    except UnicodeDecodeError:
                        # ASCII로 변환할 수 없는 경우 None으로 설정
                        current_value = None
                    else:
                        # '\x00\x00\x00'인 경우 None으로 설정
                        if extracted_bytes == b'\x00\x00\x00\x00':
                            current_value = None
                    finally:
                        # current_value를 그대로 저장 (이미 ASCII로 변환된 상태)
                        col_info['current_val'][1] = current_value
                else:
                    # 기본 정수형 처리
                    current_value = int.from_bytes(extracted_bytes, byteorder='big')
                    col_info['current_val'][1] = current_value

                byte_index += byte_size  # 다음 데이터로 이동


    def send_parse(self, record_values):
        byte_array = bytearray()
        return byte_array

class ClusterOEMHWVer(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xF1, 0x91]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 'coloms':{ 'Data_Record':{'bit':32, 'type':['line_edit', "default"],'current_val': [4,"", None]}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        
        if not isinstance(can_message, bytearray):
            raise ValueError("Invalid CAN message")

        # Service ID와 Identifier 길이를 계산
        header_length = len(self.read_service_id) + len(self.identifier)

        # 데이터 페이로드 시작 부분을 설정
        payload_start = header_length

        # 실제 데이터 페이로드 추출
        data_payload = can_message[payload_start:]

        byte_index = 0

        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']
                byte_size = bit_size // 8  # bit를 byte로 변환

                # 값을 추출하여 current_val[1]에 업데이트
                extracted_bytes = data_payload[byte_index:byte_index + byte_size]

                if col_key == 'Data_Record':
                    try:
                        # ASCII로 변환
                        current_value = extracted_bytes.decode('ascii')
                    except UnicodeDecodeError:
                        # ASCII로 변환할 수 없는 경우 None으로 설정
                        current_value = None
                    else:
                        # '\x00\x00\x00'인 경우 None으로 설정
                        if extracted_bytes == b'\x00\x00\x00\x00':
                            current_value = None
                    finally:
                        # current_value를 그대로 저장 (이미 ASCII로 변환된 상태)
                        col_info['current_val'][1] = current_value
                else:
                    # 기본 정수형 처리
                    current_value = int.from_bytes(extracted_bytes, byteorder='big')
                    col_info['current_val'][1] = current_value

                byte_index += byte_size  # 다음 데이터로 이동


    def send_parse(self, record_values):
        byte_array = bytearray()
        return byte_array

class OEMSWVer(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xF1, 0xA0]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 'coloms':{ 'Data_Record':{'bit':32, 'type':['line_edit', "default"],'current_val': [4,"", None]}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        
        if not isinstance(can_message, bytearray):
            raise ValueError("Invalid CAN message")

        # Service ID와 Identifier 길이를 계산
        header_length = len(self.read_service_id) + len(self.identifier)

        # 데이터 페이로드 시작 부분을 설정
        payload_start = header_length

        # 실제 데이터 페이로드 추출
        data_payload = can_message[payload_start:]

        byte_index = 0

        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']
                byte_size = bit_size // 8  # bit를 byte로 변환

                # 값을 추출하여 current_val[1]에 업데이트
                extracted_bytes = data_payload[byte_index:byte_index + byte_size]

                if col_key == 'Data_Record':
                    try:
                        # ASCII로 변환
                        current_value = extracted_bytes.decode('ascii')
                    except UnicodeDecodeError:
                        # ASCII로 변환할 수 없는 경우 None으로 설정
                        current_value = None
                    else:
                        # '\x00\x00\x00'인 경우 None으로 설정
                        if extracted_bytes == b'\x00\x00\x00\x00':
                            current_value = None
                    finally:
                        # current_value를 그대로 저장 (이미 ASCII로 변환된 상태)
                        col_info['current_val'][1] = current_value
                else:
                    # 기본 정수형 처리
                    current_value = int.from_bytes(extracted_bytes, byteorder='big')
                    col_info['current_val'][1] = current_value

                byte_index += byte_size  # 다음 데이터로 이동


    def send_parse(self, record_values):
        byte_array = bytearray()
        return byte_array

class AVNUpdateType(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xF1, 0xB1]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 'coloms':{ 'Data_Record':{'bit':312, 'type':['line_edit', "default"],'current_val': [39,"", None]}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        
        if not isinstance(can_message, bytearray):
            raise ValueError("Invalid CAN message")

        # Service ID와 Identifier 길이를 계산
        header_length = len(self.read_service_id) + len(self.identifier)

        # 데이터 페이로드 시작 부분을 설정
        payload_start = header_length

        # 실제 데이터 페이로드 추출
        data_payload = can_message[payload_start:]

        byte_index = 0

        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']
                byte_size = bit_size // 8  # bit를 byte로 변환

                # 값을 추출하여 current_val[1]에 업데이트
                extracted_bytes = data_payload[byte_index:byte_index + byte_size]

                if col_key == 'Data_Record':
                    try:
                        # ASCII로 변환
                        current_value = extracted_bytes.decode('ascii')
                    except UnicodeDecodeError:
                        # ASCII로 변환할 수 없는 경우 None으로 설정
                        current_value = None
                    else:
                        # '\x00\x00\x00'인 경우 None으로 설정
                        if extracted_bytes == b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00':
                            current_value = None
                    finally:
                        # current_value를 그대로 저장 (이미 ASCII로 변환된 상태)
                        col_info['current_val'][1] = current_value
                else:
                    # 기본 정수형 처리
                    current_value = int.from_bytes(extracted_bytes, byteorder='big')
                    col_info['current_val'][1] = current_value

                byte_index += byte_size  # 다음 데이터로 이동


    def send_parse(self, record_values):
        byte_array = bytearray()
        return byte_array

class RxSWIN(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xF1, 0xEF]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 
                'coloms': {
                    'CAN_Request_ID': {'bit': 16, 'type': ['line_edit', "default"], 'current_val': [4, "", None]},
                    'Data_Record': {'bit': 48, 'type': ['text_edit', "default"], 'current_val': [6, "", None]}
                }
            }
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray):
            raise ValueError("Invalid CAN message")

        # Service ID와 Identifier 길이를 계산
        header_length = len(self.read_service_id) + len(self.identifier)

        # 데이터 페이로드 시작 부분을 설정
        payload_start = header_length

        # 실제 데이터 페이로드 추출
        data_payload = can_message[payload_start:]

        byte_index = 0

        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']

                if col_key == 'CAN_Request_ID':
                    # CAN Request ID는 3바이트 고정
                    byte_size = 2
                    extracted_bytes = data_payload[byte_index:byte_index + byte_size]
                    current_value = extracted_bytes.hex().upper()
                    col_info['current_val'][1] = current_value
                    byte_index += byte_size

                elif col_key == 'Data_Record':
                    # 나머지 데이터는 ASCII 형식의 가변 길이로 처리
                    remaining_bytes = data_payload[byte_index:]
                    decoded_value = ""

                    while byte_index < len(data_payload):
                        # 첫 바이트는 뒤에 올 바이트 개수
                        byte_count = data_payload[byte_index]
                        byte_index += 1  # 첫 바이트는 개수이므로 넘어감

                        # 남은 데이터가 충분한지 확인
                        if byte_index + byte_count > len(data_payload):
                            raise ValueError("Not enough data in CAN message to process")

                        # 해당 개수만큼 데이터를 추출
                        segment = data_payload[byte_index:byte_index + byte_count]
                        try:
                            # ASCII로 변환
                            segment_value = segment.decode('ascii')
                        except UnicodeDecodeError:
                            segment_value = None
                        finally:
                            # 줄바꿈 추가하여 값을 이어붙임
                            if segment_value is not None:
                                decoded_value += segment_value + "\n"
                            else:
                                decoded_value += "[Invalid ASCII]" + "\n"

                        # 다음 데이터로 넘어감
                        byte_index += byte_count

                    # 마지막으로 추출된 값 저장
                    col_info['current_val'][1] = decoded_value.strip()



    def send_parse(self, record_values):
        byte_array = bytearray()
        return byte_array

class InternalSWVer(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0x00, 0x21]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 'coloms':{ 'SW_ver':{'bit':48, 'type':['line_edit', "default"],'current_val': [12,"", None]}}},
            'data2': { 'coloms':{ 'SNAND_ver':{'bit':32, 'type':['line_edit', "default"],'current_val': [8,"", None]}}},
            'data3': { 'coloms':{ 'NOR_ver':{'bit':32, 'type':['line_edit', "default"],'current_val': [8,"", None]}}},
            'data4': { 'coloms':{ 'ASK_ver':{'bit':24, 'type':['line_edit', "default"],'current_val': [6,"", None]}}},
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray) or len(can_message) < 16:
            raise ValueError("Invalid CAN message")

        # Service ID와 Identifier 길이를 계산
        header_length = len(self.read_service_id) + len(self.identifier)

        # 데이터 페이로드 시작 부분을 설정
        payload_start = header_length

        # 실제 데이터 페이로드 추출
        data_payload = can_message[payload_start:]

        byte_index = 0

        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']
                byte_size = bit_size // 8  # bit를 byte로 변환

                # 값을 추출하여 current_val[1]에 업데이트
                extracted_bytes = data_payload[byte_index:byte_index + byte_size]

                # 두 자리씩 끊어서 . 으로 연결
                def format_bytes_as_dotted_string(byte_data):
                    hex_string = byte_data.hex().upper()  # 16진수 대문자로 변환
                    return '.'.join([hex_string[i:i+2] for i in range(0, len(hex_string), 2)])  # 두 자리씩 끊어서 '.'으로 연결

                if col_key == 'SW_ver':
                    current_value = format_bytes_as_dotted_string(extracted_bytes)
                    if extracted_bytes == b'\x00\x00\x00\x00\x00\x00':
                        current_value = None
                elif col_key == 'SNAND_ver':
                    current_value = format_bytes_as_dotted_string(extracted_bytes)
                    if extracted_bytes == b'\x00\x00\x00\x00\x00\x00':
                        current_value = None
                elif col_key == 'NOR_ver':
                    current_value = format_bytes_as_dotted_string(extracted_bytes)
                    if extracted_bytes == b'\x00\x00\x00\x00\x00\x00':
                        current_value = None
                elif col_key == 'ASK_ver':
                    current_value = format_bytes_as_dotted_string(extracted_bytes)
                    if extracted_bytes == b'\x00\x00\x00\x00\x00\x00':
                        current_value = None
                else:
                    # 기본 정수형 처리
                    current_value = int.from_bytes(extracted_bytes, byteorder='big')

                col_info['current_val'][1] = current_value

                byte_index += byte_size  # 다음 데이터로 이동


    def send_parse(self, record_values):
        byte_array = bytearray()
        return byte_array

class DIDB002(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xB0, 0x02]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': {'coloms': {'Supported_PID': {'bit': 32, 'type': ['line_edit', "default"], 'current_val': [100, "", None]}}},
            'data2': {'coloms': {'Fuel_Input': {'bit': 8, 'type': ['line_edit', "default"], 'current_val': [4, "", None]}}},
            'data3': {'coloms': {'Battery Voltage on CLU': {'bit': 8, 'type': ['line_edit', "default"], 'current_val': [5, "", None]}}},
            'data4': {'coloms': {'Odometer(km)': {'bit': 24, 'type': ['line_edit', "default"], 'current_val': [5, "", None]}}},
            'data5': {'coloms': {'Odometer(mile)': {'bit': 24, 'type': ['line_edit', "default"], 'current_val': [5, "", None]}}},
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray):
            raise ValueError("Invalid CAN message")

        # Service ID와 Identifier 길이를 계산
        header_length = len(self.read_service_id) + len(self.identifier)

        # 데이터 페이로드 시작 부분을 설정
        payload_start = header_length

        # 실제 데이터 페이로드 추출
        data_payload = can_message[payload_start:]

        byte_index = 0  # 실제 데이터를 처리하는 바이트 인덱스

        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']
                byte_size = bit_size // 8  # bit를 byte로 변환

                # 값을 추출하여 current_val[1]에 업데이트
                extracted_bytes = data_payload[byte_index:byte_index + byte_size]

                if col_key == 'Supported_PID':
                    supported_pids = []
                    # 각 바이트를 순차적으로 처리
                    for i, byte_value in enumerate(extracted_bytes):
                        for bit_position in range(8):
                            # 각 비트를 확인하여 1인 경우 PID 추가
                            if byte_value & (1 << (7 - bit_position)):
                                pid_number = i * 8 + (bit_position + 1)
                                supported_pids.append(f'0x{pid_number:02X}')  # hex로 PID 추가

                    current_value = ', '.join(supported_pids) if supported_pids else 'None'

                elif col_key == 'Fuel_Input':
                    # 연료 입력은 1바이트(8비트)이며 0x00부터 0xFE까지는 0.5리터 단위로 표현
                    fuel_value = int.from_bytes(extracted_bytes, byteorder='big')
                    if fuel_value == 0xFF:
                        current_value = 0.5
                    else:
                        current_value = fuel_value  # 리터 단위로 변환

                elif col_key == 'Battery Voltage on CLU':
                    # 배터리 전압은 0.08 * X 로 계산
                    voltage_value = int.from_bytes(extracted_bytes, byteorder='big')
                    current_value = voltage_value * 0.08  # 전압 계산

                elif col_key == 'Odometer(km)':
                    # 주행거리 (km 사양)
                    current_value = int.from_bytes(extracted_bytes, byteorder='big')  # km로 변환

                elif col_key == 'Odometer(mile)':
                    # 주행거리 (mile 사양)
                    current_value = int.from_bytes(extracted_bytes, byteorder='big')  # mile로 변환

                else:
                    # 기본 정수형 처리
                    current_value = int.from_bytes(extracted_bytes, byteorder='big')

                # 추출한 값을 record_values의 current_val에 업데이트
                col_info['current_val'][1] = current_value

                byte_index += byte_size  # 다음 데이터로 이동



    def send_parse(self, record_values):
        byte_array = bytearray()
        return byte_array

class DIDB003(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xB0, 0x03]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': {'coloms': {'Supported_PID': {'bit': 32, 'type': ['line_edit', "default"], 'current_val':[100, "", None]}}},
            'data2': {'coloms':{'L_IGN1':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'resv1':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'resv2':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'resv3':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'resv4':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'resv5':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'resv6':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
                                'PARKING BRAKE SWITCH':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]}}}
        }
        
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        if not isinstance(can_message, bytearray):
            raise ValueError("Invalid CAN message")

        # Service ID와 Identifier 길이를 계산
        header_length = len(self.read_service_id) + len(self.identifier)

        # 데이터 페이로드 시작 부분을 설정
        payload_start = header_length

        # 실제 데이터 페이로드 추출
        data_payload = can_message[payload_start:]

        # 데이터가 충분한지 확인
        if len(data_payload) == 0:
            raise ValueError("No data payload in CAN message")

        byte_index = 0  # 바이트 단위의 데이터 인덱스
        bit_offset = 0  # 비트 단위로 처리할 때 필요한 오프셋

        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']

                # 필요한 비트 수만큼 값을 추출
                current_value = 0
                for _ in range(bit_size):
                    if bit_offset == 8:
                        byte_index += 1  # 다음 바이트로 이동
                        bit_offset = 0

                    byte_value = data_payload[byte_index]  # 현재 바이트 값을 읽음
                    bit = (byte_value >> (7 - bit_offset)) & 1  # 현재 비트 추출
                    current_value = (current_value << 1) | bit  # 추출한 비트를 current_value에 추가
                    bit_offset += 1  # 다음 비트로 이동

                # 추출한 값을 처리
                if col_key == 'Supported_PID':
                    supported_pids = []
                    for i in range(32):  # Supported PID는 4바이트 (32비트)
                        if (current_value >> (31 - i)) & 1:
                            pid_number = i + 1
                            supported_pids.append(f'0x{pid_number:02X}')
                    current_value = ', '.join(supported_pids) if supported_pids else 'None'

                elif col_key == 'L_IGN1':
                    current_value = current_value  # 이미 처리된 값

                elif 'resv' in col_key:
                    current_value = current_value  # 예약된 비트이므로 값을 유지

                elif col_key == 'PARKING BRAKE SWITCH':
                    current_value = current_value  # 이미 처리된 값

                else:
                    # 기본 정수형 처리
                    current_value = current_value

                # 추출한 값을 record_values의 current_val에 업데이트
                col_info['current_val'][1] = current_value

            # 모든 비트를 사용한 후, byte_index를 다음 바이트로 이동
            if bit_offset > 0:
                byte_index += 1
                bit_offset = 0

    def send_parse(self, record_values):
        byte_array = bytearray()
        return byte_array



did_map = {
    "EOL_Coding_R/W(0060/C0DE)": EOLCoding,
    "Vehicle_Odo_R/W(0080)": CarInfo,
    "ECUReset":ECUReset,
    "VIN_Reset_W(F110)":InitVIN,
    "VIN_R/W(F190)":VIN,
    "CodingErr_UnLock":UnlockNotCoded,
    "CodingErr_Lock":LockNotCoded,
    "ServiceReminder_Type_W(0070)":SetServiceType,
    "ServiceReminder__W(0071)":InitService,
    "ServiceReminder_Period_W(0073)":SetServiceTerm,
    "ServiceReminder_Distance_W(0072)":SetServiceDistance,
    "CANDBVer_R(F100)":CANDBVer,
    "EtherDBVer_R(F101)":EtherDBVer,
    "SupplierCode_R(F1A1)":ClusterProductionCode,
    "OEM_H/Wver_R(F191)":ClusterOEMHWVer,
    "OEM_S/Wver_R(F1A0)":OEMSWVer,
    "Supplier_S/Wver_R(F1B1)":AVNUpdateType,
    "RxSWIN_R(F1EF)":RxSWIN,
    "Conti_S/Wver_R(0021)":InternalSWVer,
    "InOutput_B002_R(B002)":DIDB002,
    "InOutput_B003_R(B003)":DIDB003
}