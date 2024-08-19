import isotp
import logging
import time
import can
import isotp.errors

import ctypes
import binascii

def my_error_handler(error):
   logging.warning('IsoTp error happened : %s - %s' % (error.__class__.__name__, str(error)))


# CAN configuration
send_id = 0x7c6
recv_id = 0x7ce
bitrate_abr = 500000
bitrate_dbr = 2000000
stmin = 10
bs = 8
padding = 0x55

# Initialize CAN interface
bus = can.interface.Bus(interface='vector', channel=0, bitrate=bitrate_abr, fd=True, app_name=None,
                                                data_bitrate=bitrate_dbr, sjw_abr=32,
                                                tseg1_abr=127, tseg2_abr=32, sam_abr=1, sjw_dbr=10, tseg1_dbr=29,
                                                tseg2_dbr=10, output_mode=1)

def txfn(msg):
    # Raw CAN message 생성
    can_msg = can.Message(arbitration_id=msg.arbitration_id, 
                          data=msg.data, 
                          is_extended_id=msg.is_extended_id, 
                          is_fd=msg.is_fd)

    # 디버깅용 출력
    print(f"Original data sent: {msg.data.hex().upper()}")
    print(f"CAN Message details:")
    print(f"  Arbitration ID: {hex(can_msg.arbitration_id).upper()}")
    print(f"  Data: {can_msg.data.hex().upper()}")
    print(f"  Extended ID: {can_msg.is_extended_id}")
    print(f"  FD: {can_msg.is_fd}")
    print(f"  DLC: {can_msg.dlc}")

    try:
        bus.send(can_msg)
        logging.info(f"Message sent: ID={hex(msg.arbitration_id)}, Data={msg.data.hex().upper()}")
    except can.CanError as e:
        logging.error(f"Failed to send message: {str(e)}")


# Define the receive function (rxfn)
def rxfn(timeout):
    try:
        msg = bus.recv(timeout)
        if msg is None:
            return None
        return isotp.CanMessage(arbitration_id=msg.arbitration_id, 
                                data=msg.data, 
                                dlc=msg.dlc, 
                                extended_id=msg.is_extended_id, 
                                is_fd=msg.is_fd)
    
    except isotp.errors as e:
        logging.error(f"Failed to receive message: {str(e)}")
        return None




# Hard reset request data
addr = isotp.Address(isotp.AddressingMode.Normal_11bits, rxid=recv_id, txid=send_id)

params = {
    'stmin': 10,  # Separation time, default is 0 (no timing requirement)
    'blocksize': 8,  # Block size, default is 8
    'tx_data_length': 8,  # Maximum number of data bytes per CAN message (for CAN FD), default is 8
    'tx_data_min_length': 8,  # Minimum length of CAN messages, default is None
    'override_receiver_stmin': None,  # Override the receiver's STmin, default is None
    'rx_flowcontrol_timeout': 1000,  # Timeout for receiving flow control frames in milliseconds, default is 1000 ms
    'rx_consecutive_frame_timeout': 1000,  # Timeout for receiving consecutive frames in milliseconds, default is 1000 ms
    'tx_padding': 0x55,  # Padding byte for transmitted messages, default is None (no padding)
    'wftmax': 0,  # Maximum wait frames, default is 0 (no wait frames allowed)
    'max_frame_size': 4095,  # Maximum frame size that can be received, default is 4095 bytes
    'can_fd': True,  # Use CAN FD, default is False (use CAN 2.0)
    'bitrate_switch': True,  # Use CAN FD bitrate switch, default is False
    'default_target_address_type': isotp.TargetAddressType.Physical,  # Default address type, Physical (0) or Functional (1)
    'rate_limit_enable': False,  # Enable rate limiting, default is False
    'rate_limit_max_bitrate': 10000000,  # Maximum bitrate for rate limiter in bits per second, default is 10,000,000 bps
    'rate_limit_window_size': 0.2,  # Time window for rate limiting in seconds, default is 0.2 seconds
    'listen_mode': False,  # Enable listen mode (no flow control), default is False
    'blocking_send': True,  # Enable blocking send, default is False
}

layer = isotp.TransportLayer(rxfn=rxfn, txfn=txfn,address=addr, error_handler=my_error_handler, params=params)
layer.start()


# Session change
session_change_request = bytearray([0x10, 0x03])
print("session change request")
layer.send(session_change_request, target_address_type=0, send_timeout=2.0)
msg = layer.recv(block=True, timeout=2.0)
if msg:
    print(f"Received ISO-TP message:")
    print(f"  Data: {msg.hex().upper()}")
else:
    print("No message received or timeout occurred.")
print("------------------------------------------------")
print()

# seed request
seed_request = bytearray([0x27, 0x11])
print("seed request")
layer.send(seed_request, target_address_type=0, send_timeout=2.0)
msg = layer.recv(block=True, timeout=2.0)
if msg:
    print(f"Received ISO-TP message:")
    print(f"  Data: {msg.hex().upper()}")

    # 뒤의 8바이트 추출하여 bytearray에 저장
    if len(msg) >= 10:  # 최소 10바이트(앞의 2바이트는 시드 요청 정보)
        response_seed = bytearray(msg[-8:])
        print(f"Extracted 8 bytes: {response_seed.hex().upper()}")
    else:
        print("Received message is too short to extract 8 bytes.")
else:
    print("No message received or timeout occurred.")
print("------------------------------------------------")


# generate key value
dll = ctypes.CDLL('./HKMC_AdvancedSeedKey_Win32.dll')
dll.ASK_KeyGenerate.restype = ctypes.c_uint
dll.ASK_KeyGenerate.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
response_seed_bytes = bytes.fromhex(response_seed.hex())
key = ctypes.create_string_buffer(8)
dll.ASK_KeyGenerate(response_seed_bytes,key)
print(f"Generated Key: {binascii.hexlify(key.raw).decode('utf-8').upper()}")
print("------------------------------------------------")



# send key value
print("send key")
send_key = bytearray([0x27, 0x12])
send_key.extend(key.raw)  # 방금 생성된 key 값을 추가
print(f"Full send_key data: {send_key.hex().upper()}")
layer.send(send_key, target_address_type=0, send_timeout=2.0)
msg = layer.recv(block=True, timeout=2.0)
if msg:
    print(f"Received ISO-TP message:")
    print(f"  Data: {msg.hex().upper()}")
else:
    print("No message received or timeout occurred.")
print("------------------------------------------------")


# EOL coding
print("eol send")
eol_write =  bytearray([0x2e,0x00,0x60,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF])
layer.send(eol_write, target_address_type=0, send_timeout=2.0)
msg = layer.recv(block=True, timeout=2.0)
if msg:
    print(f"Received ISO-TP message:")
    print(f"  Data: {msg.hex().upper()}")
else:
    print("No message received or timeout occurred.")
print("------------------------------------------------")

# ECU Reset
print("ecu reset")
eol_write =  bytearray([0x11,0x01])
layer.send(eol_write, target_address_type=0, send_timeout=2.0)
msg = layer.recv(block=True, timeout=2.0)
if msg:
    print(f"Received ISO-TP message:")
    print(f"  Data: {msg.hex().upper()}")
else:
    print("No message received or timeout occurred.")
print("------------------------------------------------")

layer.stop()
bus.shutdown()


