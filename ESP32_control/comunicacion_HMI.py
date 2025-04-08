import struct
import time
import machine

class ComunicacionHMI:
    def __init__(self):
        self.uart = machine.UART(1, baudrate=115200, tx=17, rx=16)

    def comunicacion(self, estado, L_olla1, L_olla2, C_red, C_olla12,
                     T_agua):
        data = struct.pack('ifffff', estado, L_olla1, L_olla2, C_red, C_olla12, T_agua)
        self.uart.write(data)
