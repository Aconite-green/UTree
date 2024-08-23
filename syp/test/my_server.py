from msl.loadlib import Server32
import ctypes

class MyServer(Server32):
    """Wrapper around a 32-bit C++ library 'my_lib.dll' that has an 'add' and 'version' function."""

    def __init__(self, host, port, **kwargs):
        # Load the 'my_lib' shared-library file using ctypes.CDLL
        super(MyServer, self).__init__('HKMC_AdvancedSeedKey_Win32.dll', 'cdll', host, port)

        # The Server32 class has a 'lib' property that is a reference to the ctypes.CDLL object

        # Call the version function from the library
        self.lib.ASK_KeyGenerate.restype = ctypes.c_uint
        self.lib.ASK_KeyGenerate.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    
    def generate_key(self, seed):
        key = ctypes.create_string_buffer(8)
        self.lib.ASK_KeyGenerate(seed, key)
        return key.raw