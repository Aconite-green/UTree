class UDSBase:
    def __init__(self, read_service_id, write_service_id, identifier, record_values, dll_path, method):
        self.read_service_id = read_service_id
        self.write_service_id = write_service_id
        self.identifier = identifier
        self.record_values = record_values
        self.byte_array = bytearray()
        self.dll_path = dll_path
        self.method = method

    def get_record_values(self):
        return self.record_values

    def get_method(self):
        return self.method
    
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
        last_col_info = None  # 마지막으로 처리한 col_info 저장
    
        # record_values에서 각 row를 순회
        for data_key, data_info in record_values.items():
            # row_type이 'bitwise'인지 'bytewise'인지 확인
            row_type = data_info.get('row_type', 'bitwise')
    
            if row_type == 'bitwise':
                # 'bitwise'일 경우 coloms 안의 키와 아이템을 순회
                for col_key, col_info in data_info['coloms'].items():
                    bit_size = col_info['bit']
                    current_value = 0
                    last_col_info = col_info  # 마지막으로 처리한 col_info 업데이트
    
                    # 필요한 비트 수만큼 값을 추출
                    for _ in range(bit_size):
                        if bit_offset == 8:
                            byte_index += 1
                            bit_offset = 0
    
                        byte_value = data_payload[byte_index]  # 현재 바이트 값을 읽어옴
                        bit = (byte_value >> (7 - bit_offset)) & 1
                        current_value = (current_value << 1) | bit
    
                        bit_offset += 1
    
                    # 추출한 값을 col_info의 'r_val'에 저장
                    col_info['r_val'] = current_value
    
                # 모든 비트가 사용된 후, byte_index를 다음 바이트로 이동
                if bit_offset > 0:
                    byte_index += 1
                    bit_offset = 0
    
            elif row_type == 'bytewise':
                # 'bytewise'일 경우 처리
                for col_key, col_info in data_info['coloms'].items():
                    bit_size = col_info['bit']
                    byte_size = bit_size // 8  # bit 크기를 byte 크기로 변환
                    last_col_info = col_info  # 마지막으로 처리한 col_info 업데이트

                    # 값을 추출
                    extracted_bytes = data_payload[byte_index:byte_index + byte_size]

                    # r_type에 따른 값 변환 처리
                    r_type = col_info['r_type']
                    options = col_info.get('options', None)

                    # options가 'auto'이면 무조건 None 설정
                    if options == 'auto':
                        current_value = 'auto'

                    else:
                        if r_type == 'ascii':
                            try:
                                current_value = extracted_bytes.decode('ascii')
                                # if extracted_bytes == b'\x00' * byte_size:
                                #     current_value = "Not Set"
                            except UnicodeDecodeError:
                                current_value = "Not Set"

                        elif r_type == 'hex':
                            if extracted_bytes == b'\x00' * byte_size:
                                current_value = "Not Set"
                            else:
                                # 앞의 0을 유지하면서 hex 문자열로 변환
                                current_value = extracted_bytes.hex().upper()

                        elif r_type == 'dec':
                            if extracted_bytes == b'\x00' * byte_size:
                                current_value = "Not Set"
                            else:
                                current_value = int.from_bytes(extracted_bytes, byteorder='big')

                        else:
                            # 기본 정수형 처리
                            current_value = int.from_bytes(extracted_bytes, byteorder='big')

                    # col_info의 r_val에 추출한 값을 저장
                    col_info['r_val'] = current_value

                    byte_index += byte_size  # 다음 데이터로 이동

            else:
                # 다른 row_type이 있는 경우 처리 추가 가능
                pass

        # 남은 데이터가 있는 경우 마지막 col_info에 추가
        if last_col_info and byte_index < len(data_payload):
            remaining_bytes = data_payload[byte_index:]
            if last_col_info['r_type'] == 'hex':
                last_col_info['r_val'] += remaining_bytes.hex().upper()
            elif last_col_info['r_type'] == 'ascii':
                try:
                    last_col_info['r_val'] += remaining_bytes.decode('ascii')
                except UnicodeDecodeError:
                    last_col_info['r_val'] += "[Invalid ASCII]"
            elif last_col_info['r_type'] == 'dec':
                last_col_info['r_val'] += int.from_bytes(remaining_bytes, byteorder='big')
            else:
                last_col_info['r_val'] += int.from_bytes(remaining_bytes, byteorder='big')

    def send_parse(self, record_values):
        self.byte_array.clear()
        current_byte = 0
        bit_offset = 0
    
        for data_key, data_info in record_values.items():
        
            row_type = data_info.get('row_type', 'bitwise')
            if row_type == 'bitwise':
                for col_key, col_info in data_info['coloms'].items():
                    bit_size = col_info['bit']
                    write_val = col_info['w_val']  # 쓰기 값으로 'w_val'을 사용
                    options = col_info['options']
    
                    # options가 'auto'일 경우 처리
                    if options == 'auto':
                        continue  # auto 값은 별도 처리로 패스하거나 추가 연산이 필요할 경우 처리 가능
                    
                    if write_val is None:
                        write_val = 0  # None이면 0으로 대체
    
                    # 각 비트별로 값을 byte_array에 저장
                    for i in range(bit_size):
                        bit = (write_val >> (bit_size - 1 - i)) & 1
                        current_byte = (current_byte << 1) | bit
                        bit_offset += 1
    
                        # 현재 바이트가 채워졌다면 byte_array에 추가
                        if bit_offset == 8:
                            self.byte_array.append(current_byte)
                            current_byte = 0
                            bit_offset = 0
    
                # 남아 있는 비트들이 있으면 마지막 바이트에 추가
                if bit_offset > 0:
                    current_byte = current_byte << (8 - bit_offset)  # 남은 비트들을 0으로 채움
                    self.byte_array.append(current_byte)
    
            elif row_type == 'bytewise':
                # bytewise 처리 로직
                for col_key, col_info in data_info['coloms'].items():
                    bit_size = col_info['bit']
                    byte_size = bit_size // 8  # bit 크기를 byte 크기로 변환
    
                    # w_val 값을 가져옴
                    write_val = col_info['w_val']
                    options = col_info.get('options', None)
                    w_type = col_info.get('w_type', 'int')  # 기본적으로 w_type을 'int'로 설정
    
                    # options 값이 'auto'일 경우 처리
                    if options == 'auto':
                        write_val = None  # auto에 맞는 값을 처리할 수 있으면 여기에 작성
                        continue  # 필요 시 추가 연산 후 처리 가능
                    
                    # w_type에 따라 값을 처리
                    if w_type == 'ascii':
                        # ASCII 변환
                        if write_val is None:
                            write_val = ''
                        write_val_bytes = write_val.encode('ascii')
                        self.byte_array.extend(write_val_bytes.ljust(byte_size, b'\x00'))  # 0으로 패딩
    
                    elif w_type == 'hex':
                        # HEX 변환
                        if write_val is None:
                            write_val = ""
                        try:
                            write_val_bytes = int(write_val, 16).to_bytes(byte_size, byteorder='big')
                        except (ValueError, TypeError) as e:
                            write_val_bytes = b'\x00' * byte_size  # 변환 실패 시 0으로 설정
                            print(f"Error converting hex: {write_val}, error: {e}")
                        self.byte_array.extend(write_val_bytes)
    
                    elif w_type == 'dec':
                        # DEC 변환
                        if write_val is None:
                            write_val = 0
                        try:
                            write_val_bytes = int(write_val).to_bytes(byte_size, byteorder='big')
                        except (ValueError, TypeError) as e:
                            write_val_bytes = b'\x00' * byte_size  # 변환 실패 시 0으로 설정
                            print(f"Error converting decimal: {write_val}, error: {e}")
                        self.byte_array.extend(write_val_bytes)
    
                    else:
                        # 기본 처리 (정수형으로 처리)
                        if write_val is None:
                            write_val = 0
                        try:
                            write_val_bytes = int(write_val).to_bytes(byte_size, byteorder='big')
                        except (ValueError, TypeError) as e:
                            write_val_bytes = b'\x00' * byte_size  # 변환 실패 시 0으로 설정
                            print(f"Error converting value: {write_val}, error: {e}")
                        self.byte_array.extend(write_val_bytes)
    
        return self.byte_array

    
    def validate_record_values(self):
        """
        Validate the record values.
    
        Returns:
            is_ok (bool): True if validation succeeds, False otherwise.
            failure_message (str): Combined string with the column key and failure reason, or None if successful.
        """
        for data_key, data_info in self.record_values.items():
            for col_key, col_info in data_info['coloms'].items():
                w_val = col_info['w_val']
                bit_size = col_info['bit']
                byte_size = bit_size // 8
                w_type = col_info['w_type']
                options = col_info['options']
    
                if options == 'auto':
                    continue  # auto 옵션은 검증하지 않음
                
                if w_val is None:
                    return False, f"{col_key}: Value is None"  # w_val이 None이면 실패 반환
    
                if w_type == 'ascii':
                    if len(w_val.encode('ascii')) != byte_size:
                        return False, f"{col_key}: Expected ASCII length {byte_size}, but got {len(w_val.encode('ascii'))}"
    
                elif w_type == 'hex':
                    # HEX 값일 때는 바이트당 2자릿수여야 함
                    if len(w_val) != byte_size * 2:  # hex 문자열은 바이트당 2자릿수
                        return False, f"{col_key}: Expected hex length {byte_size * 2}, but got {len(w_val)}"
    
                elif w_type == 'dec':
                    try:
                        int_value = int(w_val)
                        if int_value.bit_length() > bit_size:
                            return False, f"{col_key}: Decimal value too large for {bit_size} bits"
                    except ValueError:
                        return False, f"{col_key}: Invalid decimal value"
    
                else:  # 기본적인 int로 처리하는 경우
                    try:
                        int_value = int(w_val)
                        if int_value.bit_length() > bit_size:
                            return False, f"{col_key}: Value too large for {bit_size} bits"
                    except ValueError:
                        return False, f"{col_key}: Invalid value"
    
        return True, None  # 모든 값이 유효하면 성공


