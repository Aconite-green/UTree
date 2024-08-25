from uds_base import UDSBase

class EOLCoding(UDSBase):
    def __init__(self):
        read_service_id = [0x22]
        write_service_id = [0x2E]
        identifier = [0x00, 0x60]
        record_values = {
            'data1': {'a': {'r':0x00, 'w':0x00}, 'b': {'r':0x00, 'w':0x00}},
            'data2': {'a': {'r':0x00, 'w':0x00}, 'b': {'r':0x00, 'w':0x00}},
            'data3': {'a': {'r':0x00, 'w':0x00}, 'b': {'r':0x00, 'w':0x00}}
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


# 클래스 이름과 실제 클래스를 매핑하는 딕셔너리
did_map = {
    "EOLCoding": EOLCoding,
    "CarInfo": CarInfo
}