import serial
import time

def parsear_linea(linea):
    linea = linea.strip()
    if linea.startswith('<') and linea.endswith('>'):
        contenido = linea[1:-1]  # Quita < y >
        partes = contenido.split(',')
        datos = {}
        for parte in partes:
            id_var = parte[0]
            valor = parte[1:]
            print(f"ID: {id_var}, Valor: {valor}")
            if id_var == 'e':
                datos['estado'] = int(valor)
            elif id_var == 'L':
                if 'L_olla1' not in datos:
                    datos['L_olla1'] = float(valor)
                else:
                    datos['L_olla2'] = float(valor)
            elif id_var == 'C':
                if 'C_red' not in datos:
                    datos['C_red'] = float(valor)
                else:
                    datos['C_olla12'] = float(valor)
            elif id_var == 'T':
                datos['T_agua'] = float(valor)
        return datos
    else:
        return None

def leer_serial(puerto='/dev/ttyUSB0', baudrate=115200):
    with serial.Serial(puerto, baudrate, timeout=1) as ser:
        while True:
            linea = ser.readline().decode(errors='ignore')
            if linea:
                datos = parsear_linea(linea)
                if datos:
                    print(f"Datos recibidos: {datos}")
                else:
                    print(f"Línea inválida o incompleta: {linea.strip()}")

if __name__ == "__main__":
    try:
        while True:
            try:
                leer_serial()
            except serial.SerialException as e:
                pass
            time.sleep(1)  # Espera un segundo entre lecturas
    except KeyboardInterrupt:
        print("Lectura serial finalizada.")
