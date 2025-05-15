from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 240)  # Cambié a horizontal

        self.create_central_widget(MainWindow)
        self.add_logo(MainWindow)
        self.create_navigation_buttons()
        self.create_stacked_pages()
        self.create_additional_labels(MainWindow)
        self.setup_statusbar(MainWindow)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.set_style(MainWindow)
        self.connect_buttons()
        MainWindow.keyPressEvent = self.keyPressEvent
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_logo(self, parent_widget):
        self.logo = QtWidgets.QLabel(parent_widget)
        self.logo.setGeometry(QtCore.QRect(585, 5, 50, 50))  # A la derecha
        pixmap = QtGui.QPixmap("resources/logo.png")
        pixmap = pixmap.scaled(self.logo.width(), self.logo.height(),
                               QtCore.Qt.KeepAspectRatio,
                               QtCore.Qt.SmoothTransformation)
        self.logo.setPixmap(pixmap)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)

    def create_central_widget(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

    def create_navigation_buttons(self):
        # Botones en fila horizontal arriba
        base_x = 5
        spacing = 60
        y_pos = 5
        btn_width = 55
        btn_height = 25

        self.btn_inicio = QtWidgets.QPushButton("Empezar", self.centralwidget)
        self.btn_inicio.setGeometry(QtCore.QRect(base_x, y_pos, btn_width, btn_height))
        self.btn_inicio.setObjectName("btn_inicio")

        self.btn_carga = QtWidgets.QPushButton("Carga Agua", self.centralwidget)
        self.btn_carga.setGeometry(QtCore.QRect(base_x + spacing * 1, y_pos, btn_width, btn_height))
        self.btn_carga.setObjectName("btn_carga")

        self.btn_calentar = QtWidgets.QPushButton("Calentar Agua", self.centralwidget)
        self.btn_calentar.setGeometry(QtCore.QRect(base_x + spacing * 2, y_pos, btn_width + 10, btn_height))
        self.btn_calentar.setObjectName("btn_calentar")

        self.btn_enfriar = QtWidgets.QPushButton("Enfriar Agua", self.centralwidget)
        self.btn_enfriar.setGeometry(QtCore.QRect(base_x + spacing * 3 + 5, y_pos, btn_width + 10, btn_height))
        self.btn_enfriar.setObjectName("btn_enfriar")

        self.btn_vaciar = QtWidgets.QPushButton("Vaciar Agua", self.centralwidget)
        self.btn_vaciar.setGeometry(QtCore.QRect(base_x + spacing * 4 + 10, y_pos, btn_width + 10, btn_height))
        self.btn_vaciar.setObjectName("btn_vaciar")

    def create_stacked_pages(self):
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        # Ajuste del stacked widget a horizontal, tomando casi todo el ancho menos espacio para logo y botones
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(5, 40, 630, 190))  
        self.stackedWidget.setMinimumSize(QtCore.QSize(630, 190))
        self.stackedWidget.setObjectName("stackedWidget")

        # Página 0: Inicio
        self.Inicio = QtWidgets.QWidget()
        self.Inicio.setObjectName("Inicio")
        self.pushButton = QtWidgets.QPushButton(self.Inicio)
        self.pushButton.setGeometry(QtCore.QRect(270, 70, 90, 50))  # Centrado horizontal y vertical
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.Inicio)

        # Página 1: Carga de Agua
        self.CargaAgua = QtWidgets.QWidget()
        self.CargaAgua.setObjectName("CargaAgua")

        self.cargando_titulo = QtWidgets.QLabel(self.CargaAgua)
        self.cargando_titulo.setGeometry(QtCore.QRect(0, 0, 630, 35))
        self.cargando_titulo.setFont(font)
        self.cargando_titulo.setObjectName("cargando_titulo")
        self.cargando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.volumen = QtWidgets.QLabel(self.CargaAgua)
        self.volumen.setGeometry(QtCore.QRect(180, 50, 90, 35))
        self.volumen.setFont(font)
        self.volumen.setObjectName("volumen")
        self.volumen.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.unit_vol = QtWidgets.QLabel(self.CargaAgua)
        self.unit_vol.setGeometry(QtCore.QRect(280, 50, 50, 35))
        self.unit_vol.setFont(font)
        self.unit_vol.setObjectName("unit_vol")

        self.caudal = QtWidgets.QLabel(self.CargaAgua)
        self.caudal.setGeometry(QtCore.QRect(180, 90, 90, 35))
        self.caudal.setFont(font)
        self.caudal.setObjectName("caudal")
        self.caudal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.units_caudal = QtWidgets.QLabel(self.CargaAgua)
        self.units_caudal.setGeometry(QtCore.QRect(280, 90, 70, 35))
        self.units_caudal.setFont(font)
        self.units_caudal.setObjectName("units_caudal")

        self.STOP = QtWidgets.QPushButton(self.CargaAgua)
        self.STOP.setGeometry(QtCore.QRect(400, 70, 90, 50))
        self.STOP.setObjectName("STOP")

        self.stackedWidget.addWidget(self.CargaAgua)

        # Página 2: Calentar Agua
        self.CalentarAgua = QtWidgets.QWidget()
        self.CalentarAgua.setObjectName("CalentarAgua")

        self.calentando_titulo = QtWidgets.QLabel(self.CalentarAgua)
        self.calentando_titulo.setGeometry(QtCore.QRect(0, 0, 630, 35))
        self.calentando_titulo.setFont(font)
        self.calentando_titulo.setObjectName("calentando_titulo")
        self.calentando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.temp_2 = QtWidgets.QLabel(self.CalentarAgua)
        self.temp_2.setGeometry(QtCore.QRect(180, 60, 90, 35))
        self.temp_2.setFont(font)
        self.temp_2.setObjectName("temp_2")
        self.temp_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.units_2 = QtWidgets.QLabel(self.CalentarAgua)
        self.units_2.setGeometry(QtCore.QRect(280, 60, 50, 35))
        self.units_2.setFont(font)
        self.units_2.setObjectName("units_2")

        self.STOP_2 = QtWidgets.QPushButton(self.CalentarAgua)
        self.STOP_2.setGeometry(QtCore.QRect(400, 60, 90, 50))
        self.STOP_2.setObjectName("STOP_2")

        self.stackedWidget.addWidget(self.CalentarAgua)

        # Página 3: Enfriar Agua
        self.EnfriarAgua = QtWidgets.QWidget()
        self.EnfriarAgua.setObjectName("EnfriarAgua")

        self.enfriando_titulo = QtWidgets.QLabel(self.EnfriarAgua)
        self.enfriando_titulo.setGeometry(QtCore.QRect(0, 0, 630, 35))
        self.enfriando_titulo.setFont(font)
        self.enfriando_titulo.setObjectName("enfriando_titulo")
        self.enfriando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.temp_3 = QtWidgets.QLabel(self.EnfriarAgua)
        self.temp_3.setGeometry(QtCore.QRect(180, 60, 90, 35))
        self.temp_3.setFont(font)
        self.temp_3.setObjectName("temp_3")
        self.temp_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.units_3 = QtWidgets.QLabel(self.EnfriarAgua)
        self.units_3.setGeometry(QtCore.QRect(280, 60, 50, 35))
        self.units_3.setFont(font)
        self.units_3.setObjectName("units_3")

        self.STOP_3 = QtWidgets.QPushButton(self.EnfriarAgua)
        self.STOP_3.setGeometry(QtCore.QRect(400, 60, 90, 50))
        self.STOP_3.setObjectName("STOP_3")

        self.stackedWidget.addWidget(self.EnfriarAgua)

        # Página 4: Vaciar Agua
        self.VaciarAgua = QtWidgets.QWidget()
        self.VaciarAgua.setObjectName("VaciarAgua")

        self.vaciando_titulo = QtWidgets.QLabel(self.VaciarAgua)
        self.vaciando_titulo.setGeometry(QtCore.QRect(0, 0, 630, 35))
        self.vaciando_titulo.setFont(font)
        self.vaciando_titulo.setObjectName("vaciando_titulo")
        self.vaciando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.volumen_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.volumen_2.setGeometry(QtCore.QRect(180, 40, 90, 35))
        self.volumen_2.setFont(font)
        self.volumen_2.setObjectName("volumen_2")
        self.volumen_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.unit_vol_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.unit_vol_2.setGeometry(QtCore.QRect(280, 40, 50, 35))
        self.unit_vol_2.setFont(font)
        self.unit_vol_2.setObjectName("unit_vol_2")

        self.caudal_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.caudal_2.setGeometry(QtCore.QRect(180, 85, 90, 35))
        self.caudal_2.setFont(font)
        self.caudal_2.setObjectName("caudal_2")
        self.caudal_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.units_caudal_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.units_caudal_2.setGeometry(QtCore.QRect(280, 85, 70, 35))
        self.units_caudal_2.setFont(font)
        self.units_caudal_2.setObjectName("units_caudal_2")

        self.STOP_4 = QtWidgets.QPushButton(self.VaciarAgua)
        self.STOP_4.setGeometry(QtCore.QRect(400, 60, 90, 50))
        self.STOP_4.setObjectName("STOP_4")

        self.stackedWidget.addWidget(self.VaciarAgua)

    def create_additional_labels(self, parent_widget):
        self.label = QtWidgets.QLabel(parent_widget)
        self.label.setGeometry(QtCore.QRect(5, 200, 150, 18))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent_widget)
        self.label_2.setGeometry(QtCore.QRect(5, 220, 150, 18))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent_widget)
        self.label_3.setGeometry(QtCore.QRect(5, 240, 100, 18))
        self.label_3.setObjectName("label_3")

    def setup_statusbar(self, MainWindow):
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema Agua"))

        self.pushButton.setText(_translate("MainWindow", "Inicio"))

        self.volumen.setText(_translate("MainWindow", "30"))
        self.unit_vol.setText(_translate("MainWindow", "L"))
        self.caudal.setText(_translate("MainWindow", "30"))
        self.units_caudal.setText(_translate("MainWindow", "L/min"))
        self.STOP.setText(_translate("MainWindow", "STOP"))
        self.cargando_titulo.setText(_translate("MainWindow", "Cargando Agua"))

        self.units_2.setText(_translate("MainWindow", "°C"))
        self.temp_2.setText(_translate("MainWindow", "30"))
        self.STOP_2.setText(_translate("MainWindow", "STOP"))
        self.calentando_titulo.setText(_translate("MainWindow", "Calentando Agua"))

        self.temp_3.setText(_translate("MainWindow", "30"))
        self.units_3.setText(_translate("MainWindow", "°C"))
        self.STOP_3.setText(_translate("MainWindow", "STOP"))
        self.enfriando_titulo.setText(_translate("MainWindow", "Enfriando Agua"))

        self.unit_vol_2.setText(_translate("MainWindow", "L"))
        self.volumen_2.setText(_translate("MainWindow", "30"))
        self.caudal_2.setText(_translate("MainWindow", "30"))
        self.units_caudal_2.setText(_translate("MainWindow", "L/min"))
        self.STOP_4.setText(_translate("MainWindow", "STOP"))
        self.vaciando_titulo.setText(_translate("MainWindow", "Vaciando Agua"))

        self.label.setText(_translate("MainWindow", "ISABA 2025"))
        self.label_2.setText(_translate("MainWindow", "German Bueno"))
        self.label_3.setText(_translate("MainWindow", "Pol Pavo"))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            QtWidgets.QApplication.quit()

    def set_style(self, MainWindow):
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #2c3e50;
            }
            QWidget {
                color: #ecf0f1;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            QPushButton {
                background-color: #3498db;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)

    def connect_buttons(self):
        self.btn_inicio.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btn_carga.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btn_calentar.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btn_enfriar.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.btn_vaciar.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
