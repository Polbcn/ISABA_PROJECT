import serial
from PyQt5.QtCore import QThread, pyqtSignal
import time
class SerialThread(QThread):
    datos_recibidos = pyqtSignal(int, float, float, float, float, float)  # estado, L1, L2, C1, C2, T

    def __init__(self, port="/dev/ttyUSB0", baud=115200, parent=None):
        super().__init__(parent)
        self.port = port
        self.baud = baud
        self.running = True
        self.ser = None
        self.comandos = []

    def run(self):
        while self.running:
            if self.ser is None or not self.ser.is_open:
                try:
                    print(f"Intentando conectar a {self.port}...")
                    self.ser = serial.Serial(self.port, self.baud, timeout=1)
                    print("Puerto serie conectado")
                except serial.SerialException as e:
                    print(f"Error al abrir el puerto serie: {e}")
                    time.sleep(2)
                    continue  # Reintenta en 2 segundos

            try:
                linea = self.ser.readline().decode(errors='ignore')
                if linea:
                    print(linea)
                    datos = self.parsear_linea(linea)
                    if datos and self._datos_completos(datos):
                        self.datos_recibidos.emit(
                            datos.get('estado', 0),
                            datos.get('L_olla1', 0.0),
                            datos.get('L_olla2', 0.0),
                            datos.get('C_red', 0.0),
                            datos.get('C_olla12', 0.0),
                            datos.get('T_agua', 0.0)
                        )
                        if len(self.comandos) >= 1:
                            comando = self.comandos.pop(0)
                            print(comando)
                        else:
                            comando = b"ack\n"
                        if self.ser:
                            try:
                                self.ser.write(comando)
                                print(comando)
                            except serial.SerialException as e:
                                print(f"Error al enviar limpieza: {e}")

            except serial.SerialException as e:
                print(f"Error de lectura/escritura del puerto: {e}")
                self._cerrar_puerto()
                time.sleep(1)
            except Exception as e:
                print(f"Otro error en el hilo serie: {e}")
                time.sleep(0.5)

    def _cerrar_puerto(self):
        if self.ser:
            try:
                self.ser.close()
            except:
                pass
            self.ser = None

    def stop(self):
        self.running = False
        self.wait()

    def parsear_linea(self, linea):
        linea = linea.strip()
        if linea.startswith('<') and linea.endswith('>'):
            contenido = linea[1:-1]
            partes = contenido.split(',')
            datos = {}
            for parte in partes:
                id_var = parte[0]
                valor = parte[1:]
                try:
                    if id_var == 'e':
                        datos['estado'] = int(valor)
                    elif id_var == 'L':
                        datos['L_olla1'] = float(valor)
                    elif id_var == 'V':
                        datos['L_olla2'] = float(valor)
                    elif id_var == 'C':
                        datos['C_red'] = float(valor)
                    elif id_var == 'Q':
                        datos['C_olla12'] = float(valor)
                    elif id_var == 'T':
                        datos['T_agua'] = float(valor)
                except ValueError:
                    print(f"Valor inválido: {valor}")
            return datos
        return None
    
    def enviar_limpieza(self):
        self.comandos.append(b"limpieza\n")
        # if self.ser:
        #     try:
        #         self.ser.write(b'limpieza')
        #         print("------------Comando de limpieza enviado-------------")
        #     except serial.SerialException as e:
        #         print(f"Error al enviar limpieza: {e}")
    def enviar_stop(self):
        self.comandos.append(b"STOP\n")

    def enviar_inicio(self):
        self.comandos.append(b"INICIO\n")
        # if self.ser:
        #     try:
        #         self.ser.write(b'STOP')
        #     except serial.SerialException as e:
        #         print(f"Error al enviar limpieza: {e}")

    def _datos_completos(self, datos):
        # Opcional: solo emitir si están todos los datos necesarios
        keys_requeridas = ['estado', 'L_olla1', 'L_olla2', 'C_red', 'C_olla12', 'T_agua']
        return all(k in datos for k in keys_requeridas)
