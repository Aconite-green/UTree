from uds_base import UDSBase

class EOLCoding(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [0x2E]
        identifier = [0x00, 0x60]
        method = ('r', 'w')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
                          'data1': {
                                   'row_type': 'bitwise',
                                   'coloms': {
                                       'ECO': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                       'EPB': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                       'AHLS': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                       'MDPS': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                       'ESC': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                       'TPMS': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                       'NORMAL': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                       'ECS': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None}}},
                          'data2': {
                                    'row_type': 'bitwise',
                                    'coloms': {
                                        'ABS': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'AIRBAG': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'PSB': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'AFL': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        '4WD': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'MT/AT': {'bit': 1, 'col_type': 'combobox', 'options': {'MT':0b00,'AT':0b01},'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'SPORT': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'eCall': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None}}},
                          'data3': {
                                    'row_type': 'bitwise',
                                    'coloms': {
                                        'FuelType': {'bit': 2, 'col_type': 'combobox', 
                                                     'options': {'GSL':0b00,'DSL':0b01,'LPI':0b10,'OTHERS':0b11},
                                                     'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'Speedometer Type': {'bit': 2, 'col_type': 'combobox', 
                                                             'options': {'KPH':0b00,'KMPH':0b01,'MKPH':0b10},
                                                             'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'PSB': {'bit': 4, 'col_type': 'combobox', 
                                                'options': {'DOM': 0b0000, 'GEN': 0b0001, 'MID': 0b0010, 'EEC': 0b0011, 'AUS': 0b0100, 'CAN': 0b0101, 'USA': 0b0110, 'CHINA': 0b0111, 
                                                            'RUSSIA': 0b1000, 'INDIA': 0b1001, 'BRAZIL': 0b1010, 'MEX': 0b1011, 'INDONESIA': 0b1100, 'JAPAN ': 0b1101},
                                                'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None}}},
                          'data4': {
                                    'row_type': 'bitwise',
                                    'coloms': {
                                        'Multifunction Type2': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'Power Type': {'bit': 3, 'col_type': 'combobox', 
                                                       'options':{'ICV': 0b000, 'HEV': 0b001, 'PHEV': 0b010, 'EV': 0b011, 'FCEV': 0b100},
                                                       'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'High Performance Type': {'bit': 2, 'col_type': 'combobox', 
                                                                  'options': {'OFF': 0b00, 'HIGH_PERFORMANCE': 0b01, 'N': 0b10},
                                                                  'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'reserved': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'Autolight': {'bit': 1, 'col_type': 'button', 'options': None, 'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None}}},
                          'data5': {
                                    'row_type': 'bitwise',
                                    'coloms': {
                                        'Multifunction Type': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'Maximum Indicated Speed': {'bit': 3, 'col_type': 'combobox', 
                                                                    'options': {'KPH_260': 0b000, 'KPH_160': 0b001, 'KPH_220': 0b010, 'KPH_300': 0b011},
                                                                    'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'HUD': {'bit': 1, 'col_type': 'button', 'options':None, 'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'Fuel Tank Size': {'bit': 2, 'col_type': 'combobox', 
                                                           'options': {'TANK_A': 0b00, 'TANK_B': 0b01, 'TANK_C': 0b10, 'TANK_D': 0b11},
                                                           'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'ICC': {'bit': 1, 'col_type': 'button', 'options': None, 'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None}}},
                          'data6': {
                                    'row_type': 'bitwise',
                                    'coloms': {
                                        'RSBR': {'bit': 3, 'col_type': 'combobox', 
                                                 'options': {'NONE': 0b000, 'R2_P2': 0b001, 'R2_P3': 0b010, 'R2_P2_R3_P2': 0b011, 'R2_P3_R3_P2': 0b100,'R2_P2_R3_P3': 0b101, 'R2_P3_R3_P3': 0b110},
                                                 'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'Body Type': {'bit': 3, 'col_type': 'combobox', 
                                                      'options': {'SEDAN': 0b000, 'SUV': 0b001, 'MPV': 0b010, 'WAGON': 0b011, 'HATCHBACK': 0b100, 'PICKUP_TRUCK': 0b101, 'TYPE_G': 0b110, 'TYPE_H': 0b111},
                                                       'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'reserved': {'bit': 2, 'col_type': 'button', 'options':None, 'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None}}},
                          'data7': {
                                    'row_type': 'bitwise',
                                    'coloms': {
                                        'FCA': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'FCA2': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'LKA': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'ISLA': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'DAW': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'SCC': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'LFA': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'HDA': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None}}},
                          'data8': {
                                    'row_type': 'bitwise',
                                    'coloms': {
                                        'HDA2': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'HDP': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'Emergency Stop': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'PDW': {'bit': 1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                        'reserved': {'bit': 4, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None}}}}
        
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

class CarInfo(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [0x2E]
        identifier = [0x00, 0x80]
        method = ('r', 'w')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': {
                      'row_type': 'bytewise',
                      'coloms':{ 
                                'dealer_id':{'bit':40, 'col_type':'line_edit','options':None, 'r_type': 'ascii', 'w_type': 'ascii', 'r_val': None, 'w_val': 'CONTI'}}},
            'data2': {
                      'row_type': 'bytewise',
                      'coloms':{ 
                                'date':{'bit':32, 'col_type':'calendar','options':None, 'r_type': 'hex', 'w_type': 'hex', 'r_val': None, 'w_val': None}}},
            'data3': {
                      'row_type': 'bytewise',
                      'coloms':{ 
                                'milage(DEC)':{'bit':32, 'col_type':'line_edit','options':None, 'r_type': 'dec', 'w_type': 'dec', 'r_val': None, 'w_val': None}}},
            'data4': {
                      'row_type': 'bytewise',         
                      'coloms':{ 
                                'checksum':{'bit':8, 'col_type':'line_edit','options':'auto', 'r_type': 'dec', 'w_type': 'dec', 'r_val': None, 'w_val': None}}},
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    # Method Overide For CheckSum
    def send_parse(self, record_values):
        # 먼저 UDSBase의 send_parse 호출하여 기본적인 데이터 전송 로직 실행
        byte_array = super().send_parse(record_values)
        
        # CarInfo 클래스에서만 options가 'auto'인 경우 추가 연산 수행
        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                options = col_info.get('options', None)
                
                if options == 'auto':
                    # Checksum 계산 (현재 byte_array에 대해)
                    checksum = 0
                    for byte in byte_array:
                        checksum += byte
                    checksum = checksum & 0xFF  # 전체 합의 마지막 1바이트 추출
                    checksum = ~checksum & 0xFF  # Invert (보수 계산)
                    byte_array.append(checksum)  # 최종적으로 byte_array에 checksum 추가

        return byte_array

class ECUReset(UDSBase):
   def __init__(self):
       read_service_id = [None]
       write_service_id = [0x11]
       identifier = [0x01]
       method = ('w')
       dll_path = None
       record_values = {
           'data1': { 
                     'row_type': 'bytewise',
                     'coloms':{ 
                               'ECU_reset':{'bit':8, 'col_type':'line_edit','options':'auto', 'r_type': 'dec', 'w_type': 'dec', 'r_val': None, 'w_val': None}}}
       }
       super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

class UnlockNotCoded(UDSBase):
    def __init__(self):
        read_service_id = [None]
        write_service_id = [0x3D]
        identifier = [0x24,0x50, 0x00, 0x10, 0x36, 0x00, 0x01, 0x00]
        method = ('w')
        dll_path = None
        record_values = {
            'data1': { 
                      'row_type': 'bytewise',
                      'coloms':{ 'Unlock Not Coded':{'bit':8,  'col_type':'line_edit','options':'auto', 'r_type': 'dec', 'w_type': 'dec', 'r_val': None, 'w_val': None}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

class LockNotCoded(UDSBase):
    def __init__(self):
        read_service_id = [None]
        write_service_id = [0x3D]
        identifier = [0x24,0x50, 0x00, 0x10, 0x36, 0x00, 0x01, 0x01]
        method = ('w')
        dll_path = None
        record_values = {
            'data1': { 
                      'row_type': 'bytewise',
                      'coloms':{ 'Lock Not Coded':{'bit':8,  'col_type':'line_edit','options':'auto', 'r_type': 'dec', 'w_type': 'dec', 'r_val': None, 'w_val': None}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

class InitVIN(UDSBase):
    def __init__(self):
        read_service_id = [None]
        write_service_id = [0x2E]
        identifier = [0xF1, 0x10]
        method = ('w')
        dll_path = None
        record_values = {
            'data1': { 'coloms':{ 'InitVIN':{'bit':8, 'col_type':'line_edit','options':'auto', 'r_type': 'dec', 'w_type': 'dec', 'r_val': None, 'w_val': None}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)
    
    # Method Overide For Any Data
    def send_parse(self, record_values):
        byte_array = super().send_parse(record_values)
        byte_array.append(0x00)
        return byte_array

class VIN(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [0x2E]
        identifier = [0xF1, 0x90]
        method = ('w', 'r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': {
                      'row_type': 'bytewise',
                      'coloms':{ 
                                'VIN':{'bit':136, 'col_type':'line_edit','options':None, 'r_type': 'ascii', 'w_type': 'ascii', 'r_val': None, 'w_val': None}}},
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

class SetServiceType(UDSBase):
    def __init__(self):
        read_service_id = [None]
        write_service_id = [0x2E]
        identifier = [0x00, 0x70]
        method = ('w')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
           
            'data1': {
                'row_type': 'bitwise',
                'coloms':{
                    'Service Type':{'bit':8, 'col_type':'combobox', 
                                    'options':{'Set by Customer':0b00,'Set by Workshop':0b01},
                                    'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None}}}}

        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

class InitService(UDSBase):
    def __init__(self):
        read_service_id = [None]
        write_service_id = [0x2E]
        identifier = [0x00, 0x71]
        method = ('w')
        dll_path = None
        record_values = {
            'data1': {
                'row_type': 'bitwise', 
                'coloms':{ 'InitService':{'bit':8, 'col_type':'line_edit','options':'auto', 'r_type': 'dec', 'w_type': 'dec', 'r_val': None, 'w_val': None}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def send_parse(self, record_values):
        byte_array = super().send_parse(record_values)
        byte_array.append(0x00)
        
        return byte_array

class SetServiceDistance(UDSBase):
    def __init__(self):
        read_service_id = [None]
        write_service_id = [0x2E]
        identifier = [0x00, 0x72]
        method = ('w')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': {
                'row_type': 'bytewise', 
                'coloms':{ 
                    'Service_Distance(DEC, 0~99999 Km or Mile)':{'bit':24, 'col_type':'line_edit','options':None, 'r_type': 'dec', 'w_type': 'dec', 'r_val': None, 'w_val': None}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

class SetServiceTerm(UDSBase):
    def __init__(self):
        read_service_id = [None]
        write_service_id = [0x2E]
        identifier = [0x00, 0x73]
        method = ('w')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': {
                'row_type': 'bytewise', 
                'coloms':{ 'Service_Term(DEC, 0~99 Month)':{'bit':16, 'col_type':'line_edit','options':None, 'r_type': 'dec', 'w_type': 'dec', 'r_val': None, 'w_val': None}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

class CANDBVer(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xF1, 0x00]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': {
                'row_type': 'bytewise', 
                'coloms':{ 'Data_Record':{'bit':24, 'col_type':'line_edit','options':None, 'r_type': 'ascii', 'w_type': 'dec', 'r_val': None, 'w_val': None}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

class EtherDBVer(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xF1, 0x01]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 
                'row_type': 'bytewise',
                'coloms':{ 'Data_Record':{'bit':24, 'col_type':'line_edit','options':None, 'r_type': 'dec', 'w_type': 'dec', 'r_val': None, 'w_val': None}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

class ClusterProductionCode(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xF1, 0xA1]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 
                'row_type': 'bytewise',
                'coloms':{ 'Data_Record':{'bit':32,'col_type':'line_edit','options':None, 'r_type': 'ascii', 'w_type': 'dec', 'r_val': None, 'w_val': None}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

class ClusterOEMHWVer(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xF1, 0x91]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 
                'row_type': 'bytewise',
                'coloms':{ 'Data_Record':{'bit':32, 'col_type':'line_edit','options':None, 'r_type': 'ascii', 'w_type': 'dec', 'r_val': None, 'w_val': None}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

class OEMSWVer(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xF1, 0xA0]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 
                'row_type': 'bytewise',
                'coloms':{ 'Data_Record':{'bit':32, 'col_type':'line_edit','options':None, 'r_type': 'ascii', 'w_type': 'dec', 'r_val': None, 'w_val': None}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

class AVNUpdateType(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xF1, 0xB1]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 
                'row_type': 'bytewise',
                'coloms':{ 'Data_Record':{'bit':312, 'col_type':'line_edit','options':None, 'r_type': 'ascii', 'w_type': 'dec', 'r_val': None, 'w_val': None}}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

class RxSWIN(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xF1, 0xEF]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 
                'row_type': 'bytewise',
                'coloms': {
                    'CAN_Request_ID': {'bit': 16, 'col_type':'line_edit','options':None, 'r_type': 'hex', 'w_type': 'dec', 'r_val': None, 'w_val': None},
                    'Data_Record': {'bit': 48, 'col_type':'text_edit','options':None, 'r_type': 'ascii', 'w_type': 'dec', 'r_val': None, 'w_val': None}
                }
            }
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        # 우선 UDSBase의 read_parse 호출하여 기본 처리
        super().read_parse(can_message, record_values)
        
        # 기존 로직 추가: CAN_Request_ID와 Data_Record에 대한 처리
        header_length = len(self.read_service_id) + len(self.identifier)
        data_payload = can_message[header_length:]
        byte_index = 2

        for data_key, data_info in record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                bit_size = col_info['bit']

                if col_key == 'Data_Record':
                    # ASCII 형식의 가변 길이 처리
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
                    col_info['r_val'] = decoded_value.strip()
# need: hex upper
class InternalSWVer(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0x00, 0x21]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': { 
                'row_type': 'bytewise',
                'coloms':{ 'SW_ver':{'bit':48, 'col_type':'line_edit','options':None, 'r_type': 'hex', 'w_type': 'dec', 'r_val': None, 'w_val': None}}},
            'data2': { 
                'row_type': 'bytewise',
                'coloms':{ 'SNAND_ver':{'bit':32, 'col_type':'line_edit','options':None, 'r_type': 'hex', 'w_type': 'dec', 'r_val': None, 'w_val': None}}},
            'data3': { 
                'row_type': 'bytewise',
                'coloms':{ 'NOR_ver':{'bit':32, 'col_type':'line_edit','options':None, 'r_type': 'hex', 'w_type': 'dec', 'r_val': None, 'w_val': None}}},
            'data4': { 
                'row_type': 'bytewise',
                'coloms':{ 'ASK_ver':{'bit':24,'col_type':'line_edit','options':None, 'r_type': 'hex', 'w_type': 'dec', 'r_val': None, 'w_val': None}}},
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

class DIDB002(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xB0, 0x02]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data1': {
                'row_type': 'bytewise',
                'coloms': {'Supported_PID': {'bit': 32, 'col_type':'line_edit','options':None, 'r_type': 'hex', 'w_type': 'dec', 'r_val': None, 'w_val': None}}},
            'data2': {
                'row_type': 'bytewise',
                'coloms': {'Fuel_Input': {'bit': 8, 'col_type':'line_edit','options':None, 'r_type': 'hex', 'w_type': 'dec', 'r_val': None, 'w_val': None}}},
            'data3': {
                'row_type': 'bytewise',
                'coloms': {'Battery Voltage on CLU': {'bit': 8, 'col_type':'line_edit','options':None, 'r_type': 'hex', 'w_type': 'dec', 'r_val': None, 'w_val': None}}},
            'data4': {
                'row_type': 'bytewise',
                'coloms': {'Odometer(km)': {'bit': 24, 'col_type':'line_edit','options':None, 'r_type': 'hex', 'w_type': 'dec', 'r_val': None, 'w_val': None}}},
            'data5': {
                'row_type': 'bytewise',
                'coloms': {'Odometer(mile)': {'bit': 24, 'col_type':'line_edit','options':None, 'r_type': 'hex', 'w_type': 'dec', 'r_val': None, 'w_val': None}}},
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
            # 우선 기본적인 UDSBase의 read_parse를 호출하여 공통 부분 처리
            super().read_parse(can_message, record_values)

            # Supported_PID에 대해서만 오버라이딩 처리
            if 'data1' in record_values and 'Supported_PID' in record_values['data1']['coloms']:
                data_info = record_values['data1']['coloms']['Supported_PID']
                bit_size = data_info['bit']
                byte_size = bit_size // 8  # bit를 byte로 변환

                # Service ID와 Identifier 길이를 계산
                header_length = len(self.read_service_id) + len(self.identifier)
                data_payload = can_message[header_length:]

                # 값 추출
                extracted_bytes = data_payload[:byte_size]

                supported_pids = []
                # 각 바이트를 순차적으로 처리
                for i, byte_value in enumerate(extracted_bytes):
                    for bit_position in range(8):
                        # 각 비트를 확인하여 1인 경우 PID 추가
                        if byte_value & (1 << (7 - bit_position)):
                            pid_number = i * 8 + (bit_position + 1)
                            supported_pids.append(f'0x{pid_number:02X}')  # hex로 PID 추가

                current_value = ', '.join(supported_pids) if supported_pids else 'None'

                # Supported_PID의 r_val에 값 저장
                data_info['r_val'] = current_value

class DIDB003(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [None]
        identifier = [0xB0, 0x03]
        method = ('r')
        dll_path = "HKMC_AdvancedSeedKey_Win32_4inch.dll"
        record_values = {
            'data': {
                'row_type': 'bytewise',
                'coloms': {'Supported_PID': {'bit': 32, 'col_type':'line_edit','options':None, 'r_type': 'hex', 'w_type': 'dec', 'r_val': None, 'w_val': None}}},
            'data1': {
                'row_type': 'bitwise',
                'coloms':{'L_IGN1':{'bit':1, 'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                'reserved':{'bit':6,  'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None},
                                'PARKING BRAKE SWITCH':{'bit':1,  'col_type': 'button', 'options': None,'r_type': 'bool', 'w_type': 'bool', 'r_val': None, 'w_val': None}}}
        }
        
        super().__init__(read_service_id, write_service_id, identifier, record_values, dll_path, method)

    def read_parse(self, can_message, record_values):
        # 기본적인 UDSBase의 read_parse 처리
        super().read_parse(can_message, record_values)
        
        # Supported_PID의 특이한 처리 부분을 오버라이드
        if 'data' in record_values and 'Supported_PID' in record_values['data']['coloms']:
            data_info = record_values['data']['coloms']['Supported_PID']
            bit_size = data_info['bit']
            byte_size = bit_size // 8  # bit를 byte로 변환

            # Service ID와 Identifier 길이를 계산
            header_length = len(self.read_service_id) + len(self.identifier)
            data_payload = can_message[header_length:]

            # 값 추출
            extracted_bytes = data_payload[:byte_size]

            supported_pids = []
            # 각 바이트를 순차적으로 처리
            for i, byte_value in enumerate(extracted_bytes):
                for bit_position in range(8):
                    # 각 비트를 확인하여 1인 경우 PID 추가
                    if byte_value & (1 << (7 - bit_position)):
                        pid_number = i * 8 + (bit_position + 1)
                        supported_pids.append(f'0x{pid_number:02X}')  # hex로 PID 추가

            current_value = ', '.join(supported_pids) if supported_pids else 'None'
            
            # Supported_PID의 r_val에 값 저장
            data_info['r_val'] = current_value

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

negative_response_codes = {
    0x11: {
        "code": "ServiceNotSupported",
        "description": "Send if the requested service is no supported",
        "remark": ""
    },
    0x12: {
        "code": "SubFunctionNotSupported",
        "description": "Send if the sub-function parameter in the request message is not supported",
        "remark": ""
    },
    0x13: {
        "code": "IncorrectMessageLengthOrInvalidFormat",
        "description": "The length of the message is wrong",
        "remark": ""
    },
    0x22: {
        "code": "ConditionNotCorrect",
        "description": "This code shall be returned if the criteria for the request DiagnosticSessionControl are not met",
        "remark": ""
    },
    0x24: {
        "code": "RequestSequenceError",
        "description": "Send if the ‘sendKey’ sub-function is received without first receiving a ‘requestSeed’ request message",
        "remark": ""
    },
    0x31: {
        "code": "RequestOutOfRange",
        "description": "Requested message contains a parameter which attempts to substitute a value beyond its range, or access a Data Identifier/Routine Identifier that is not supported (in active session)",
        "remark": ""
    },
    0x33: {
        "code": "SecurityAccessDenied",
        "description": "Security strategy has not been satisfied",
        "remark": ""
    },
    0x35: {
        "code": "InvalidKey",
        "description": "Send if an expected ‘sendKey’ sub-function value is received and the value of the key does not match the server’s internally stored/calculated key",
        "remark": ""
    },
    0x36: {
        "code": "ExceedNumberOfAttempts",
        "description": "Send if the delay timer is active due to exceeding the maximum number of allowed false access attempts",
        "remark": ""
    },
    0x37: {
        "code": "RequiredTimeDelayNotExpired",
        "description": "Send if the delay time is active and request is transmitted",
        "remark": ""
    },
    0x72: {
        "code": "GeneralProgrammingFailure",
        "description": "Detected an error when erasing or programming a memory location in the permanent memory device",
        "remark": ""
    },
    0x78: {
        "code": "RequestCorrectlyReceived-ResponsePending",
        "description": "Request message was received correctly but the action to be performed is not yet completed",
        "remark": "CAN Message Timeout 감지 시간 동안에 통신 연결 유지를 위함"
    },
    0x7E: {
        "code": "SubFunctionNotSupportedInActiveSession",
        "description": "Does not support the requested sub-function in the session currently active",
        "remark": ""
    },
    0x7F: {
        "code": "ServiceNotSupportedInActiveSession",
        "description": "Does not support the requested service in the session currently active",
        "remark": ""
    }
}
