import isotp
import logging
import time
import can
import isotp.errors

import ctypes
import binascii

class CanManager:
    def __init__(self, can_data, error_handler):
        self.can_data = can_data
        self.error_handler = error_handler

        # CAN configuration
        self.send_id = None
        self.recv_id = None
        self.bitrate_abr = None
        self.bitrate_dbr = None
        self.stmin = None
        self.bs = None
        self.padding = None
        self.interface = None
        self.tseg1_abr = None
        self.tseg2_abr = None
        self.sjw_abr = None
        self.sjw_dbr = None
        self.tseg1_dbr = None
        self.tseg2_dbr = None
        self.lib_file_name = None
        self.isotp_params = None


        # CAN Object
        self.bus = None
        self.can_send_msg = None
        self.can_recv_msg = None
        self.layer = None

    # SET CAN CONFIGURATION
    # ///////////////////////////////////////////////////////////////
    def setup_can(self):
        
        # APP CONFIG
        app_config = self.can_data['AppConfig']
        self.send_id = app_config['SendID']
        self.recv_id = app_config['RecvID']
        self.interface = self._get_device_type(app_config['CanTargetDevice'])
        self.channel = self._get_channel(app_config['CanTargetDevice'])
        self.is_fd = self._get_fd_info(app_config['Interface'])

        # BASIC CAN
        basic_can = self.can_data['Basic_CAN']
        self.bitrate_abr = basic_can['bitrateAbr']
        self.sjw_abr = basic_can['sjwAbr']
        self.tseg1_abr = basic_can['tseg1Abr']
        self.tseg2_abr = basic_can['tseg2Abr']

        # FD ONLY
        fd_only = self.can_data['FD_only']
        self.bitrate_dbr = fd_only['bitrateDbr']
        self.sjw_dbr = fd_only['sjwDbr']
        self.tseg1_dbr = fd_only['tseg1Dbr']
        self.tseg2_dbr = fd_only['tseg2Dbr']

        # ISOTP
        isotp_data = self.can_data['ISOTP']
        self.bs = isotp_data['BS']
        self.padding = isotp_data['Padding']
        self.stmin = isotp_data['STmin']
        
        # ASK
        ask = self.can_data['ASK']
        self.lib_file_name = ask['LibFileName']

        # Layer Params
        self.isotp_params= {
                'stmin': self.stmin,  # Separation time, default is 0 (no timing requirement)
                'blocksize': self.bs,  # Block size, default is 8
                'tx_data_length': 8,  # Maximum number of data bytes per CAN message (for CAN FD), default is 8
                'tx_data_min_length': 8,  # Minimum length of CAN messages, default is None
                'override_receiver_stmin': None,  # Override the receiver's STmin, default is None
                'rx_flowcontrol_timeout': 1000,  # Timeout for receiving flow control frames in milliseconds, default is 1000 ms
                'rx_consecutive_frame_timeout': 1000,  # Timeout for receiving consecutive frames in milliseconds, default is 1000 ms
                'tx_padding': self.padding,  # Padding byte for transmitted messages, default is None (no padding)
                'wftmax': 0,  # Maximum wait frames, default is 0 (no wait frames allowed)
                'max_frame_size': 4095,  # Maximum frame size that can be received, default is 4095 bytes
                'can_fd': self.is_fd,  # Use CAN FD, default is False (use CAN 2.0)
                'bitrate_switch': self.is_fd,  # Use CAN FD bitrate switch, default is False
                'default_target_address_type': isotp.TargetAddressType.Physical,  # Default address type, Physical (0) or Functional (1)
                'rate_limit_enable': False,  # Enable rate limiting, default is False
                'rate_limit_max_bitrate': 10000000,  # Maximum bitrate for rate limiter in bits per second, default is 10,000,000 bps
                'rate_limit_window_size': 0.2,  # Time window for rate limiting in seconds, default is 0.2 seconds
                'listen_mode': False,  # Enable listen mode (no flow control), default is False
                'blocking_send': True,  # Enable blocking send, default is False
                    }
            
            
    # START/STOP CAN CONFIGURATION
    # ///////////////////////////////////////////////////////////////
    def start_communication(self):
    # Connect CAN BUS
        try:
            self.bus = can.interface.Bus(
                interface=self.interface, 
                channel=self.channel, 
                bitrate=self.bitrate_abr, 
                fd=self.is_fd, 
                app_name=None,
                data_bitrate=self.bitrate_dbr, 
                sjw_abr=self.sjw_abr,
                tseg1_abr=self.tseg1_abr, 
                tseg2_abr=self.tseg2_abr, 
                sam_abr=1, 
                sjw_dbr=self.sjw_dbr, 
                tseg1_dbr=self.tseg1_dbr,
                tseg2_dbr=self.tseg2_dbr, 
                output_mode=1
            )
            # Connect CAN ISOTP LAYER
            addr = isotp.Address(isotp.AddressingMode.Normal_11bits, rxid=self.recv_id, txid=self.send_id)
            self.layer = isotp.TransportLayer(rxfn=self._rxfn, txfn=self._txfn,address=addr, error_handler=self.error_handler, params=self.isotp_params)
            self.layer.start()
        
            
        except KeyError as e:
            self.error_handler.handle_error(f"Configuration key error: {str(e)}")
        except can.CanError as e:
            self.error_handler.handle_error(f"CAN interface error: {str(e)}")
        except Exception as e:
            self.error_handler.handle_error(f"Unexpected error during CAN setup: {str(e)}")
        
        self.error_handler.log_message("can connected.")
    
    def stop_communication(self):
        try:

            if self.layer is not None:
                self.layer.stop()
            else:
                self.error_handler.log_message("CAN layer was not initialized.")
            if self.bus is not None:
                self.bus.shutdown()
            else:
                self.error_handler.log_message("CAN bus was not initialized.")
        
        except can.CanError as e:
            self.error_handler.handle_error(f"Error during CAN bus shutdown: {str(e)}")
        except Exception as e:
            self.error_handler.handle_error(f"Unexpected error during CAN shutdown: {str(e)}")


        self.error_handler.log_message("can disconnected.")






    def _get_required_value(self, config_section, key):
        if key not in config_section:
            raise ValueError(f"{key}가 YML 파일의 섹션에 정의되어 있지 않습니다.")
        return config_section[key]
    def _get_fd_info(self, Interface):
        if Interface == 'CANFD':
            return True
        else:
            return False
    def _get_channel(self, CanTargetDevice):
        device = CanTargetDevice.split()
        return int(device[-1]) - 1   
    
    def _get_device_type(self, CanTargetDevice):
        if 'VN1630A' in CanTargetDevice:
            return 'vector'
    

    def _txfn(self, msg):
    # Raw CAN message 생성
        self.can_send_msg = can.Message(arbitration_id=msg.arbitration_id, 
                          data=msg.data, 
                          is_extended_id=msg.is_extended_id, 
                          is_fd=msg.is_fd)
        try:
            self.bus.send(self.can_send_msg)
        except can.CanError as e:
            logging.error(f"Failed to send message: {str(e)}")

    def _rxfn(self, timeout):
        try:
            self.can_recv_msg = self.bus.recv(timeout)
            if self.can_recv_msg is None:
                return None
            return isotp.CanMessage(arbitration_id=self.can_recv_msg.arbitration_id, 
                                    data=self.can_recv_msg.data, 
                                    dlc=self.can_recv_msg.dlc, 
                                    extended_id=self.can_recv_msg.is_extended_id, 
                                    is_fd=self.can_recv_msg.is_fd)
        except isotp.errors.IsoTpError as e:
           logging.error(f"Failed to receive message: {str(e)}")
           return None
    

    def send_message(self, message):
        # CAN 메시지 송신 코드
        pass

    def receive_message(self):
        # CAN 메시지 수신 코드
        pass
