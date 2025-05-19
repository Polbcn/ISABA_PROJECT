import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_layout2 import Ui_MainWindow  # O el nombre del archivo generado
import serial
import struct
import time
from customserial import SerialThread
from PyQt5.QtCore import QTimer


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.ir_a_carga_agua)
        # Iniciar hilo serial
        self.serial_thread = SerialThread()
        self.serial_thread.datos_recibidos.connect(self.actualizar_datos)
        self.ui.cleanButton.clicked.connect(self.enviar_limpieza)
        self.ui.vaciarButton.clicked.connect(self.serial_thread.enviar_vaciado)
        # Linkeamos los botones de parada a la función stop
        self.ui.STOP_limpieza.clicked.connect(self.stop)
        self.ui.STOP_vaciado.clicked.connect(self.stop)
        self.ui.STOP.clicked.connect(self.stop)
        self.ui.STOP_2.clicked.connect(self.stop)
        self.ui.STOP_3.clicked.connect(self.stop)
        self.ui.STOP_4.clicked.connect(self.stop)
        self.ui.pushButton.clicked.connect(self.enviar_inicio)
        self.serial_thread.start()
        # Configuración inicial
        self.volumen_llenado = 15
        self.temp_high = 100
        self.temp_low = 80
        self.volumen_vaciado = 10
        self.ui.btn_config.clicked.connect(self.serial_thread.enviar_config)

        # Timers por cada parámetro
        self.timers = {
            "volumen_llenado_mas": QTimer(),
            "volumen_llenado_menos": QTimer(),
            "temp_high_mas": QTimer(),
            "temp_high_menos": QTimer(),
            "temp_low_mas": QTimer(),
            "temp_low_menos": QTimer(),
            "volumen_vaciado_mas": QTimer(),
            "volumen_vaciado_menos": QTimer(),
        }

        # Intervalo de repetición (ajustable)
        for timer in self.timers.values():
            timer.setInterval(100)

        # Conectar señales
        self.ui.btn_inc_vol_llenado.pressed.connect(lambda: self.iniciar_timer("volumen_llenado_mas"))
        self.ui.btn_inc_vol_llenado.released.connect(lambda: self.detener_timer("volumen_llenado_mas"))
        self.ui.btn_dec_vol_llenado.pressed.connect(lambda: self.iniciar_timer("volumen_llenado_menos"))
        self.ui.btn_dec_vol_llenado.released.connect(lambda: self.detener_timer("volumen_llenado_menos"))

        self.ui.btn_inc_temp_high.pressed.connect(lambda: self.iniciar_timer("temp_high_mas"))
        self.ui.btn_inc_temp_high.released.connect(lambda: self.detener_timer("temp_high_mas"))
        self.ui.btn_dec_temp_high.pressed.connect(lambda: self.iniciar_timer("temp_high_menos"))
        self.ui.btn_dec_temp_high.released.connect(lambda: self.detener_timer("temp_high_menos"))

        self.ui.btn_inc_temp_low.pressed.connect(lambda: self.iniciar_timer("temp_low_mas"))
        self.ui.btn_inc_temp_low.released.connect(lambda: self.detener_timer("temp_low_mas"))
        self.ui.btn_dec_temp_low.pressed.connect(lambda: self.iniciar_timer("temp_low_menos"))
        self.ui.btn_dec_temp_low.released.connect(lambda: self.detener_timer("temp_low_menos"))

        self.ui.btn_inc_vol_vaciado.pressed.connect(lambda: self.iniciar_timer("volumen_vaciado_mas"))
        self.ui.btn_inc_vol_vaciado.released.connect(lambda: self.detener_timer("volumen_vaciado_mas"))
        self.ui.btn_dec_vol_vaciado.pressed.connect(lambda: self.iniciar_timer("volumen_vaciado_menos"))
        self.ui.btn_dec_vol_vaciado.released.connect(lambda: self.detener_timer("volumen_vaciado_menos"))

        # Asociar funciones de acción
        self.timers["volumen_llenado_mas"].timeout.connect(self.incrementar_volumen_llenado)
        self.timers["volumen_llenado_menos"].timeout.connect(self.decrementar_volumen_llenado)
        self.timers["temp_high_mas"].timeout.connect(self.incrementar_temp_high)
        self.timers["temp_high_menos"].timeout.connect(self.decrementar_temp_high)
        self.timers["temp_low_mas"].timeout.connect(self.incrementar_temp_low)
        self.timers["temp_low_menos"].timeout.connect(self.decrementar_temp_low)
        self.timers["volumen_vaciado_mas"].timeout.connect(self.incrementar_volumen_vaciado)
        self.timers["volumen_vaciado_menos"].timeout.connect(self.decrementar_volumen_vaciado)

        # Botón guardar
        self.ui.btn_guardar_config.clicked.connect(self.guardar_config)

        self.first_con = True



# self.stackedWidget.addWidget(self.Inicio)       # índice 0
# self.stackedWidget.addWidget(self.CargaAgua)    # índice 1
# self.stackedWidget.addWidget(self.CalentarAgua) # índice 2
# self.stackedWidget.addWidget(self.EnfriarAgua)  # índice 3
# self.stackedWidget.addWidget(self.VaciarAgua)   # índice 4
    def iniciar_timer(self, nombre):
        self.timers[nombre].start()
        # Ejecuta una vez al tocar por primera vez
        self.timers[nombre].timeout.emit()
    
    def detener_timer(self, nombre):
        self.timers[nombre].stop()
    
    # --- Volumen llenado
    def incrementar_volumen_llenado(self):
        self.volumen_llenado = min(50, self.volumen_llenado + 1)
        self.ui.val_vol_llenado.setText(str(self.volumen_llenado))
    
    def decrementar_volumen_llenado(self):
        self.volumen_llenado = max(0, self.volumen_llenado - 1)
        self.ui.val_vol_llenado.setText(str(self.volumen_llenado))
    
    # --- Temp High
    def incrementar_temp_high(self):
        self.temp_high = min(200, self.temp_high + 1)
        self.ui.val_temp_high.setText(str(self.temp_high))
    
    def decrementar_temp_high(self):
        self.temp_high = max(0, self.temp_high - 1)
        self.ui.val_temp_high.setText(str(self.temp_high))
    
    # --- Temp Low
    def incrementar_temp_low(self):
        self.temp_low = min(200, self.temp_low + 1)
        self.ui.val_temp_low.setText(str(self.temp_low))
    
    def decrementar_temp_low(self):
        self.temp_low = max(0, self.temp_low - 1)
        self.ui.val_temp_low.setText(str(self.temp_low))
    
    # --- Volumen vaciado
    def incrementar_volumen_vaciado(self):
        self.volumen_vaciado = min(50, self.volumen_vaciado + 1)
        self.ui.val_vol_vaciado.setText(str(self.volumen_vaciado))
    
    def decrementar_volumen_vaciado(self):
        self.volumen_vaciado = max(0, self.volumen_vaciado - 1)
        self.ui.val_vol_vaciado.setText(str(self.volumen_vaciado))
    
    

    def enviar_limpieza(self):
        # Aquí puedes enviar el comando de limpieza al ESP32
        self.serial_thread.enviar_limpieza()  # Implementa este método en SerialThread
        # self.ui.stackedWidget.setCurrentIndex(5)  # Cambia al índice correspondiente

    def enviar_inicio(self):
        self.serial_thread.enviar_inicio()

    def stop(self):
        self.serial_thread.enviar_stop()  # Implementa este método en SerialThread
        # self.ui.stackedWidget.setCurrentIndex(0)  # Cambia al índice correspondiente

    def ir_a_carga_agua(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def guardar_config(self):
        print("Valores guardados:")
        print("Volumen llenado:", self.volumen_llenado)
        print("Temperatura High:", self.temp_high)
        print("Temperatura Low:", self.temp_low)
        print("Volumen vaciado:", self.volumen_vaciado)
        cadena = (f"<T{self.temp_high:.2f},"
                  f"V{self.volumen_llenado:.2f},"
                  f"I{self.temp_low:.2f},"
                  f"Q{self.volumen_vaciado:.2f}>\n")
        self.serial_thread.enviar_texto(cadena)


    # Aquí podrías enviar los datos al ESP32, guardarlos en archivo, etc.


    def actualizar_datos(self, estado, L_olla1, L_olla2, C_red, C_olla12, T_agua):
        if estado == 6:
            if self.first_con:
                self.ui.stackedWidget.setCurrentIndex(6)
                self.first_con = False
        else:
            self.ui.stackedWidget.setCurrentIndex(estado)
            self.first_con = True
        print(f"Estado: {estado}")
        # print(f"L_olla1: {L_olla1:.2f}, L_olla2: {L_olla2:.2f}")
        # print(f"C_red: {C_red:.2f}, C_olla12: {C_olla12:.2f}")
        # print(f"T_agua: {T_agua:.2f}")
        # Aquí puedes actualizar etiquetas de la UI si quieres
        self.ui.volumen.setText(f"{L_olla1:.1f}")
        self.ui.caudal.setText(f"{C_red:.1f}")
        self.ui.temp_2.setText(f"{T_agua:.1f}")
        self.ui.temp_3.setText(f"{T_agua:.1f}")
        self.ui.volumen_2.setText(f"{L_olla2:.1f}")
        self.ui.caudal_2.setText(f"{C_olla12:.1f}")

    def closeEvent(self, event):
        self.serial_thread.stop()
        self.serial_thread.wait()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainApp()
    ventana.show()
    sys.exit(app.exec_())
