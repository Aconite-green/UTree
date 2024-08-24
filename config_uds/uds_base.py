class UDSBase:
    def __init__(self, read_service_id, write_service_id, identifier, record_values):
        self.read_service_id = read_service_id
        self.write_service_id = write_service_id
        self.identifier = identifier
        self.record_values = record_values
        self.byte_array = bytearray()

    def get_record_values(self):
        return self.record_values


    def clear_byte_array(self):
        return self.byte_array.clear()

    def get_byte_array(self):
        return self.byte_array
