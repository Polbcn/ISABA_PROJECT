from machine import ADC, Pin, Timer
import machine
import math
import time
from pines import ESP32_PLC
from comunicacion_HMI import ComunicacionHMI




# Definicion de estados
class FSM():
    """
    ESTADOS
    0 -> Idle
    1 -> Cargando agua de red 
    2 -> Proceso 1 (olla 1)
    3 -> Traspaso olla 1/2
    4 -> Proceso 2 (olla 2)
    5 -> Proceso 3 (olla 2)
    6 -> Procesos no controlados (requiere atención manual)
    7 -> Finalizado (Requiere atención manual)

    Variables a configurar:
    (Estado 1)
     - self.capacidad_olla1: Cantidad de agua en L que se quiere cargar en la olla 1
    (Estado 2)
     - self.temp_agua: Temperatura de consigna del agua
     - self.tiempo_espera_agua_min: Tiempo que se espera a que el agua llegue a la temperatura de consigna
    """
    def __init__(self):
        self.estado = 0
        self.cambio_estado = False
        self.PLC = ESP32_PLC()
        
        # Variables de control
        self.capacidad_olla1 = 5.0
        self.capacidad_olla2 = 10.0
        self.temp_agua = 100.0
        self.temp_agualow = 80.0
        self.tiempo_espera_agua_min = 10 # min
        # Variables de estado
        self.caudal_acumulado = 0.0
        self.caudal_acumulado2 = 0.0
        self.prev_time = 0
        self.timer_agua = 0.0
        self.temperatura_red_reached = False

        # COmunicacion
        self.comunicacion = ComunicacionHMI()

    # Estado 0 -> Idle (estado de reposo)
    def estado0(self):
        self.PLC.ba_red.value(0)
        self.PLC.ba_olla12.value(0)
        self.prev_time = time.time()
        self.caudal_acumulado = 0.0
        self.caudal_acumulado2 = 0.0
        self.timer_agua = 0.0
        self.temperatura_red_reached = False
        # Espera a que el usuario inice el proceso

    #Estado 1-> Cargando agua de red
    """
    Variables a configurar:
    self.capacidad_olla1: Cantidad de agua en L que se quiere cargar en la olla 1

    Variables que se emplean:
    self.caudal_acumulado: Cantidad de agua acumulada en L
    self.prev_time: Tiempo de la ultima lectura del caudal
    self.PLC.caudal_red: Caudal de agua de red en L/min
    self.PLC.ba_red: Bomba de agua de red
    """
    def estado1(self):
        self.PLC.ba_red.value(1)  # Encender bomba de red
        self.caudal_acumulado += self.PLC.caudal_red*(time.time()-self.prev_time)/60.0 # Litros
        self.prev_time = time.time()
        if self.caudal_acumulado >= self.capacidad_olla1:
            self.PLC.ba_red.value(0)  # Apagar bomba de red
            self.temperatura_red_reached = False
            self.estado = 3

    # Estado 2 -> Proceso 1 (olla 1) 
    # Calentamiento de agua
    """
    Variables a configurar:
    self.temp_agua: Temperatura de consigna del agua
    self.tiempo_espera_agua_min: Tiempo que se espera a que el agua llegue a la temperatura de consigna

    Variables que se emplean:
    self.PLC.get_temp(): Temperatura del agua de red
    self.PLC.calefactor: Calefactor de la olla
    self.timer_agua: Tiempo que se ha mantenido el agua a la temperatura de consigna
    self.prev_time: Tiempo de la ultima lectura de temperatura
    self.temperatura_red_reached: Indica si se ha alcanzado la temperatura de consigna
    """
    def estado2(self):
        temperatura = self.PLC.get_temp()
        if temperatura == -1:
            # print("Error en la lectura de temperatura")
            self.estado = 0
            return
        if temperatura >= self.temp_agua:
            self.PLC.calefactor.value(0)
            if self.temperatura_red_reached == False:
                self.prev_time = time.time()
            self.temperatura_red_reached = True
        elif temperatura < self.temp_agua:
            self.PLC.calefactor.value(1)
        
        # Timer que mantiene el agua a la temperatura consigna
        if self.temperatura_red_reached:
            self.timer_agua += time.time() - self.prev_time
            self.prev_time = time.time()
            if self.timer_agua >= self.tiempo_espera_agua_min*60.0:
                self.estado = 3
                self.timer_agua = 0.0
    
    # Estado 3 -> Enfriamiento de agua
    """
    Variables a configurar:
    self.temp_agualow: Temperatura de consigna del agua
    """ 
    def estado3(self):
        temperatura = self.PLC.get_temp()
        if temperatura <= self.temp_agualow and temperatura != -1:
            self.estado = 4


    # Estado 4 -> Traspaso olla 1/2
    """
    Variables a configurar:
    self.PLC.ba_olla12: Bomba de agua de olla 1/2
    self.capacidad_olla2: Cantidad de agua en L que se quiere cargar en la olla 2

    Variables que se emplean:
    self.caudal_acumulado: Cantidad de agua acumulada en L
    self.prev_time: Tiempo de la ultima lectura del caudal
    self.PLC.caudal_olla12: Caudal de agua de olla 1/2 en L/min
    self.PLC.ba_olla12: Bomba de agua de olla 1/2
    """ 
    def estado4(self):
        self.PLC.ba_olla12.value(1)  # Encender bomba de olla 1/2
        self.caudal_acumulado2 += self.PLC.caudal_olla12*(time.time()-self.prev_time)/60.0 # Litros
        self.prev_time = time.time()
        if self.caudal_acumulado2 >= self.capacidad_olla2:
            self.PLC.ba_olla12.value(0)  # Encender bomba de olla 1/2
            self.estado = 0

    def estado5(self):
        # Estado de limpieza
        self.PLC.ba_red.value(1)
        self.PLC.ba_olla12.value(0)

    def comunicacion_HMI(self):
        try:
            self.comunicacion.comunicacion(self.estado, self.caudal_acumulado, self.caudal_acumulado2,
                                            self.PLC.caudal_red, self.PLC.caudal_olla12, self.PLC.get_temp())
            
            #print("Done comunicacion")
        except:
            # print("Error en la comunicacion con la HMI")
            pass
    def recibir_datos(self):
        try:
            reading = self.comunicacion.recibir_comando()
            if reading:
                print("--------------------------------")
                print(reading)
            if "limpieza" in reading:
                self.estado = 5
            elif "STOP" in reading:
                self.estado = 0
            elif "ack" in reading:
                pass
            elif "INICIO" in reading:
                self.estado = 1
            else:
                print("Recibido algo desconocido:")
                print(reading)
            pass
        except Exception as e:
            print(f"Error recibiendo datos: {e}")



if __name__ == "__main__":
    # PLC = ESP32_PLC()
    # while(True):
    #     # print(PLC.caudal_red)
    #     print(PLC.get_temp())
    #     time.sleep(1)
    PLC = FSM()
    prev_time = time.ticks_ms()
    while True:
        if PLC.estado == 0:
            PLC.estado0()
        elif PLC.estado == 1:
            PLC.estado1()
        elif PLC.estado == 2:
            PLC.estado2()
        elif PLC.estado == 3:
            PLC.estado3()
        elif PLC.estado == 4:
            PLC.estado4()
        elif PLC.estado == 5:
            PLC.estado5()
        else:
            # print("Estado no definido")
            pass
        #print(f"tiempo: {time.time()-prev_time}")
        # Comunicacion con la HMI
        if time.ticks_ms()-prev_time >= 200:
            PLC.comunicacion_HMI()
            prev_time = time.ticks_ms()
            PLC.recibir_datos()

