from uds_base import UDSBase

class EOLCoding(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [0x2E]
        identifier = [0x00, 0x60]
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
                                'ARIBAG':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
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
                                '#resv#':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]},
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
                                '#resv#':{'bit':2, 'type':['button', 0],'current_val': ['bool',None, None]}}
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
                                '#resv#':{'bit':4, 'type':['button', 0],'current_val': ['bool',None, None]}}        
            }
            
            }
        
        super().__init__(read_service_id, write_service_id, identifier, record_values)

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




class CarInfo(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [0x2E]
        identifier = [0x00, 0x80]
        record_values = {
            'dealer_id': {'r':0x00, 'w':0x00},
            'date' : {'r':0x00, 'w':0x00},
            'mileage' : {'r':0x00, 'w':0x00},
            'checksum' : {'r':0x00, 'w':0x00},
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values,)

class Test(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [0x2E]
        identifier = [0x00, 0x80]
        record_values = {
            
            'data1': { 'coloms':{ 'a':{'bit':1, 'type':['combobox', {'0':0, '1':1}],'current_val': ['bool',None, None]}}},
            'data2': { 'coloms':{ 'b':{'bit':7, 'type':['line_edit', "default"],'current_val': ['ascii',1, 1]}}},
            'btn1': {'coloms':{ 'c':{'bit':1, 'type':['button', 0],'current_val': ['bool',1, 1]}}},
            'btn0': { 'coloms':{ 'c':{'bit':1, 'type':['button', 0],'current_val': ['bool',0, 0]}}},
            'btnNone': {'coloms':{ 'c':{'bit':1, 'type':['button', 0],'current_val': ['bool',None, None]}}}  
                        }
        
        super().__init__(read_service_id, write_service_id, identifier, record_values,)




# 클래스 이름과 실제 클래스를 매핑하는 딕셔너리
did_map = {
    "EOLCoding": EOLCoding,
    # "CarInfo": CarInfo,
    "Test": Test
}