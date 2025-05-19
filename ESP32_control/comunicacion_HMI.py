import struct
import time
import machine
import sys
class ComunicacionHMI:
    def __init__(self):
        pass
        #self.uart = machine.UART(1, baudrate=115200, tx=19, rx=18, timeout=100)

    def comunicacion(self, estado, L_olla1, L_olla2, C_red, C_olla12,
                     T_agua):
        # print(f"Estado: {estado}")
        # print(f"L_olla1: {L_olla1:.2f}, L_olla2: {L_olla2:.2f}")
        # print(f"C_red: {C_red:.2f}, C_olla12: {C_olla12:.2f}")
        # print(f"T_agua: {T_agua:.2f}")
        #print("hola")
        cadena = self.formato_datos(estado, L_olla1, L_olla2, C_red, C_olla12, T_agua)
        #data = struct.pack('ifffff', estado, L_olla1, L_olla2, C_red, C_olla12, T_agua)
        #self.uart.write(data)
        print(cadena)
        
    def formato_datos(self, estado, L_olla1, L_olla2, C_red, C_olla12, T_agua):
        cadena = (f"<e{estado},"
                  f"L{L_olla1:.2f},"
                  f"V{L_olla2:.2f},"
                  f"C{C_red:.2f},"
                  f"Q{C_olla12:.2f},"
                  f"T{T_agua:.2f}>")
        return cadena
    
    def recibir_comando(self):
        linea = sys.stdin.readline()
        return linea
        # if self.uart.any():
        #     linea = self.uart.readline()
        #     if linea:
        #         try:
        #             linea = linea.decode('utf-8').strip()
        #             print("Comando recibido:", linea)
        #             return linea
        #         except Exception as e:
        #             pass
        #             print("Error decodificando:", e)
        # return None
