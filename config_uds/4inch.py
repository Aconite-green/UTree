from uds_base import UDSBase

class EOLCoding(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [0x2E]
        identifier = [0x00, 0x60]
        record_values = {
            'data1': {'ECO': {'r':0x00, 'w':0x00}, 'EPB': {'r':0x00, 'w':0x00}, 'AHLS': {'r':0x00, 'w':0x00}, 'MDPS': {'r':0x00, 'w':0x00},'ESC': {'r':0x00, 'w':0x00}, 'TPMS': {'r':0x00, 'w':0x00},'NORMAL': {'r':0x00, 'w':0x00}, 'ECS': {'r':0x00, 'w':0x00}},
            'data2': {'ABS': {'r':0x00, 'w':0x00}, 'AIR BAG': {'r':0x00, 'w':0x00}, 'PSB': {'r':0x00, 'w':0x00}, 'AFL': {'r':0x00, 'w':0x00},'4WD': {'r':0x00, 'w':0x00}, 'AT': {'r':0x00, 'w':0x00},'SPORT': {'r':0x00, 'w':0x00}, 'eCall': {'r':0x00, 'w':0x00}},
            'data3': {'Fuel Type ': {'r':0x00, 'w':0x00}, 'Speedometer Type': {'r':0x00, 'w':0x00}, 'Area': {'r':0x00, 'w':0x00}},
            'data4': {'Multifunction ': {'r':0x00, 'w':0x00}, 'Power Type': {'r':0x00, 'w':0x00}, 'High Performance Type': {'r':0x00, 'w':0x00}, '??': {'r':0x00, 'w':0x00},'Autolight': {'r':0x00, 'w':0x00}},
            'data5': {'Multifunction Type': {'r':0x00, 'w':0x00}, 'Maximum Indicated Speed': {'r':0x00, 'w':0x00}, 'HUD': {'r':0x00, 'w':0x00}, 'Fuel Tank Type': {'r':0x00, 'w':0x00},'ICC': {'r':0x00, 'w':0x00}},
            'data6': {'RSBR': {'r':0x00, 'w':0x00}, 'Body Type': {'r':0x00, 'w':0x00}},
            'data7': {'FCA': {'r':0x00, 'w':0x00}, 'FCA2': {'r':0x00, 'w':0x00}, 'LKA': {'r':0x00, 'w':0x00}, 'ISLA': {'r':0x00, 'w':0x00},'DAW': {'r':0x00, 'w':0x00}, 'SOC': {'r':0x00, 'w':0x00},'LFA': {'r':0x00, 'w':0x00}, 'HDA': {'r':0x00, 'w':0x00}},
            'data8': {'HDA2': {'r':0x00, 'w':0x00}, 'HDP': {'r':0x00, 'w':0x00}, 'Emergency Stop': {'r':0x00, 'w':0x00}, 'PDW': {'r':0x00, 'w':0x00}}
        }
        super().__init__(read_service_id, write_service_id, identifier, record_values)

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
            
            'data1': {'byte': 1, 'coloms':{ 'a':{'bit':1, 'type':['combobox', [0, 1]],'current_val': ['bool',1, 1]}}},
            'data2': {'byte': 1, 'coloms':{ 'b':{'bit':7, 'type':['line_edit', "default"],'current_val': ['ascii',1, 1]}}},
            'data3': {'byte': 1, 'coloms':{ 'c':{'bit':1, 'type':['button', 0],'current_val': ['bool',1, 1]}}}  
                        }
        super().__init__(read_service_id, write_service_id, identifier, record_values,)




# 클래스 이름과 실제 클래스를 매핑하는 딕셔너리
did_map = {
    # "EOLCoding": EOLCoding,
    # "CarInfo": CarInfo,
    "Test": Test
}