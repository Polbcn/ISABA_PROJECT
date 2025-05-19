import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_layout2 import Ui_MainWindow  # O el nombre del archivo generado
import serial
import struct
import time
from customserial import SerialThread

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
        # Linkeamos los botones de parada a la función stop
        self.ui.STOP_limpieza.clicked.connect(self.stop)
        self.ui.STOP.clicked.connect(self.stop)
        self.ui.STOP_2.clicked.connect(self.stop)
        self.ui.STOP_3.clicked.connect(self.stop)
        self.ui.STOP_4.clicked.connect(self.stop)
        self.ui.pushButton.clicked.connect(self.enviar_inicio)
        self.serial_thread.start()

# self.stackedWidget.addWidget(self.Inicio)       # índice 0
# self.stackedWidget.addWidget(self.CargaAgua)    # índice 1
# self.stackedWidget.addWidget(self.CalentarAgua) # índice 2
# self.stackedWidget.addWidget(self.EnfriarAgua)  # índice 3
# self.stackedWidget.addWidget(self.VaciarAgua)   # índice 4
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
    
    def actualizar_datos(self, estado, L_olla1, L_olla2, C_red, C_olla12, T_agua):
        self.ui.stackedWidget.setCurrentIndex(estado)
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
