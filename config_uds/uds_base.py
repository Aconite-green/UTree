class UDSBase:
    def __init__(self, read_service_id, write_service_id, identifier, record_values, dll_path):
        self.read_service_id = read_service_id
        self.write_service_id = write_service_id
        self.identifier = identifier
        self.record_values = record_values
        self.byte_array = bytearray()
        self.dll_path = dll_path

    def get_record_values(self):
        return self.record_values

