from ctypes import Structure, c_byte, c_char
class CcsSec_secretKey(Structure):
    _fields_ = [("", c_byte * 16)]

class CCS_RAND_state(Structure):
    _fields_ = [("", c_char * 64)]

