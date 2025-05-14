import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_layout2 import Ui_MainWindow  # O el nombre del archivo generado

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.ir_a_carga_agua)
# self.stackedWidget.addWidget(self.Inicio)       # índice 0
# self.stackedWidget.addWidget(self.CargaAgua)    # índice 1
# self.stackedWidget.addWidget(self.CalentarAgua) # índice 2
# self.stackedWidget.addWidget(self.EnfriarAgua)  # índice 3
# self.stackedWidget.addWidget(self.VaciarAgua)   # índice 4
    def ir_a_carga_agua(self):
        self.ui.stackedWidget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainApp()
    ventana.show()
    sys.exit(app.exec_())
