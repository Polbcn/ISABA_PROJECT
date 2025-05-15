from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 320)

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
        self.logo.setGeometry(QtCore.QRect(350, 5, 50, 50))  # Posición ajustada

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
        self.btn_inicio = QtWidgets.QPushButton("Empezar", self.centralwidget)
        self.btn_inicio.setGeometry(QtCore.QRect(5, 5, 55, 25))

        self.btn_carga = QtWidgets.QPushButton("Carga Agua", self.centralwidget)
        self.btn_carga.setGeometry(QtCore.QRect(65, 5, 65, 25))

        self.btn_calentar = QtWidgets.QPushButton("Calentar Agua", self.centralwidget)
        self.btn_calentar.setGeometry(QtCore.QRect(135, 5, 75, 25))

        self.btn_enfriar = QtWidgets.QPushButton("Enfriar Agua", self.centralwidget)
        self.btn_enfriar.setGeometry(QtCore.QRect(215, 5, 75, 25))

        self.btn_vaciar = QtWidgets.QPushButton("Vaciar Agua", self.centralwidget)
        self.btn_vaciar.setGeometry(QtCore.QRect(295, 5, 75, 25))

    def create_stacked_pages(self):
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 35, 420, 280))
        self.stackedWidget.setObjectName("stackedWidget")

        # Página 0: Inicio
        self.Inicio = QtWidgets.QWidget()
        self.Inicio.setObjectName("Inicio")
        self.pushButton = QtWidgets.QPushButton(self.Inicio)
        self.pushButton.setGeometry(QtCore.QRect(170, 110, 85, 40))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.Inicio)

        # Página 1: Carga de Agua
        self.CargaAgua = QtWidgets.QWidget()
        self.CargaAgua.setObjectName("CargaAgua")

        self.volumen = QtWidgets.QLabel(self.CargaAgua)
        self.volumen.setGeometry(QtCore.QRect(150, 50, 60, 35))
        self.volumen.setFont(font)
        self.volumen.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.unit_vol = QtWidgets.QLabel(self.CargaAgua)
        self.unit_vol.setGeometry(QtCore.QRect(215, 50, 60, 35))
        self.unit_vol.setFont(font)

        self.caudal = QtWidgets.QLabel(self.CargaAgua)
        self.caudal.setGeometry(QtCore.QRect(150, 90, 60, 35))
        self.caudal.setFont(font)
        self.caudal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.units_caudal = QtWidgets.QLabel(self.CargaAgua)
        self.units_caudal.setGeometry(QtCore.QRect(215, 90, 60, 35))
        self.units_caudal.setFont(font)

        self.STOP = QtWidgets.QPushButton(self.CargaAgua)
        self.STOP.setGeometry(QtCore.QRect(165, 180, 85, 40))

        self.cargando_titulo = QtWidgets.QLabel(self.CargaAgua)
        self.cargando_titulo.setGeometry(QtCore.QRect(10, 5, 400, 35))
        self.cargando_titulo.setFont(font)
        self.cargando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.stackedWidget.addWidget(self.CargaAgua)

        # Página 2: Calentar Agua
        self.CalentarAgua = QtWidgets.QWidget()
        self.CalentarAgua.setObjectName("CalentarAgua")

        self.temp_2 = QtWidgets.QLabel(self.CalentarAgua)
        self.temp_2.setGeometry(QtCore.QRect(150, 70, 60, 35))
        self.temp_2.setFont(font)
        self.temp_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.units_2 = QtWidgets.QLabel(self.CalentarAgua)
        self.units_2.setGeometry(QtCore.QRect(215, 70, 60, 35))
        self.units_2.setFont(font)

        self.STOP_2 = QtWidgets.QPushButton(self.CalentarAgua)
        self.STOP_2.setGeometry(QtCore.QRect(165, 180, 85, 40))

        self.calentando_titulo = QtWidgets.QLabel(self.CalentarAgua)
        self.calentando_titulo.setGeometry(QtCore.QRect(10, 5, 400, 35))
        self.calentando_titulo.setFont(font)
        self.calentando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.stackedWidget.addWidget(self.CalentarAgua)

        # Página 3: Enfriar Agua
        self.EnfriarAgua = QtWidgets.QWidget()
        self.EnfriarAgua.setObjectName("EnfriarAgua")

        self.temp_3 = QtWidgets.QLabel(self.EnfriarAgua)
        self.temp_3.setGeometry(QtCore.QRect(150, 70, 60, 35))
        self.temp_3.setFont(font)
        self.temp_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.units_3 = QtWidgets.QLabel(self.EnfriarAgua)
        self.units_3.setGeometry(QtCore.QRect(215, 70, 60, 35))
        self.units_3.setFont(font)

        self.STOP_3 = QtWidgets.QPushButton(self.EnfriarAgua)
        self.STOP_3.setGeometry(QtCore.QRect(165, 180, 85, 40))

        self.enfriando_titulo = QtWidgets.QLabel(self.EnfriarAgua)
        self.enfriando_titulo.setGeometry(QtCore.QRect(10, 5, 400, 35))
        self.enfriando_titulo.setFont(font)
        self.enfriando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.stackedWidget.addWidget(self.EnfriarAgua)

        # Página 4: Vaciar Agua
        self.VaciarAgua = QtWidgets.QWidget()
        self.VaciarAgua.setObjectName("VaciarAgua")

        self.volumen_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.volumen_2.setGeometry(QtCore.QRect(150, 50, 60, 35))
        self.volumen_2.setFont(font)
        self.volumen_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.unit_vol_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.unit_vol_2.setGeometry(QtCore.QRect(215, 50, 60, 35))
        self.unit_vol_2.setFont(font)

        self.caudal_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.caudal_2.setGeometry(QtCore.QRect(150, 90, 60, 35))
        self.caudal_2.setFont(font)
        self.caudal_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.units_caudal_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.units_caudal_2.setGeometry(QtCore.QRect(215, 90, 60, 35))
        self.units_caudal_2.setFont(font)

        self.STOP_4 = QtWidgets.QPushButton(self.VaciarAgua)
        self.STOP_4.setGeometry(QtCore.QRect(165, 180, 85, 40))

        self.vaciando_titulo = QtWidgets.QLabel(self.VaciarAgua)
        self.vaciando_titulo.setGeometry(QtCore.QRect(10, 5, 400, 35))
        self.vaciando_titulo.setFont(font)
        self.vaciando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.stackedWidget.addWidget(self.VaciarAgua)

    def create_additional_labels(self, parent_widget):
        self.label = QtWidgets.QLabel(parent_widget)
        self.label.setGeometry(QtCore.QRect(5, 270, 150, 18))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent_widget)
        self.label_2.setGeometry(QtCore.QRect(5, 290, 150, 18))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent_widget)
        self.label_3.setGeometry(QtCore.QRect(5, 310, 150, 18))
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

        self.temp_2.setText(_translate("MainWindow", "30"))
        self.units_2.setText(_translate("MainWindow", "°C"))
        self.STOP_2.setText(_translate("MainWindow", "STOP"))
        self.calentando_titulo.setText(_translate("MainWindow", "Calentando Agua"))

        self.temp_3.setText(_translate("MainWindow", "30"))
        self.units_3.setText(_translate("MainWindow", "°C"))
        self.STOP_3.setText(_translate("MainWindow", "STOP"))
        self.enfriando_titulo.setText(_translate("MainWindow", "Enfriando Agua"))

        self.volumen_2.setText(_translate("MainWindow", "30"))
        self.unit_vol_2.setText(_translate("MainWindow", "L"))
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
                border-radius: 12px;
                color: white;
                font-size: 14px;
                padding: 8px;
                transition: background-color 0.3s ease;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QLabel {
                font-weight: bold;
            }
            QLabel#cargando_titulo, QLabel#vaciando_titulo, QLabel#enfriando_titulo, QLabel#calentando_titulo {
                font-size: 18pt;
                color: #3498db;
            }
            QLabel#volumen, QLabel#caudal, QLabel#temp_2, QLabel#temp_3, QLabel#volumen_2, QLabel#caudal_2 {
                font-size: 22pt;
            }
            QLabel#unit_vol, QLabel#units_caudal, QLabel#units_2, QLabel#units_3, QLabel#unit_vol_2, QLabel#units_caudal_2 {
                font-size: 18pt;
                color: #bdc3c7;
            }
            QLabel#label, QLabel#label_2, QLabel#label_3 {
                font-size: 11pt;
                color: #7f8c8d;
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
    MainWindow.show()  # <-- Aquí se usa tamaño 420x320, no fullscreen, porque es chiquito

    sys.exit(app.exec_())
