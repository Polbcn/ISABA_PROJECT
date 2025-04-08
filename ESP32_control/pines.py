from machine import Pin, I2C, Timer
from adafruit_mcp9600 import MCP9600
# Pines de control
class ESP32_PLC():
    def __init__(self):
        # Definicion de pines de salida
        self.ba_red = Pin(26, Pin.OUT)
        self.ba_olla12 = Pin(27, Pin.OUT)
        self.calefactor = Pin(25, Pin.OUT)
        # Definicion de pines de entrada
        self.rot_red = Pin(19, Pin.IN)
        self.rot_olla12 = Pin(18, Pin.IN)
        self.errores = []
        try:
            # Definicion termopar
            self.i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
            self.termopar = MCP9600(self.i2c, address=0x60, tctype="K")
        except OSError:
            print("Termopar no inicializado")
            self.errores.append("Termopar no inicializado")
        
        # Definicon de timers y variables para calcular el caudal
        try:
            self.timer_caudal1 = Timer(0)
            self.timer_caudal2 = Timer(1)
            self.timer_caudal1.init(period=1000, mode=Timer.PERIODIC, callback=self.calcular_caudal1)
            self.timer_caudal2.init(period=1000, mode=Timer.PERIODIC, callback=self.calcular_caudal2)
            self.rot_red.irq(trigger=Pin.IRQ_RISING, handler=self.captar_rot_red)
            self.rot_olla12.irq(trigger=Pin.IRQ_RISING, handler=self.captar_rot_olla12)
            self.caudal_red = 0
            self.caudal_olla12 = 0
            self.pulsos_red = 0
            self.pulsos_olla12 = 0
        except ... :
            print("Error en la definicon")

    #Contador flancos rotametro agua de red
    def captar_rot_red(self, pin):
        self.pulsos_red += 1

    #Contador flancos rotametro agua de olla 1/2
    def captar_rot_olla12(self, pin):
        self.pulsos_olla12 += 1

    # Calculo de caudal de agua de red
    def calcular_caudal1(self, timer):
        try:
            self.caudal_red = (self.pulsos_red / 5.0)  # L/min
            self.pulsos_red = 0
        except ZeroDivisionError:
            pass
    
    # Calculo de caudal de agua de olla 1/2
    def calcular_caudal2(self, timer):
        try:
            self.caudal_olla12 = (self.pulsos_olla12 / 5.0)  # L/min
            self.pulsos_olla12 = 0
        except ZeroDivisionError:
            pass
    
    def get_temp(self):
        if "Termopar no inicializado" in self.errores:
            return -1
        return self.termopar.temperature

