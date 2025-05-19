from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 360)

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
        MainWindow.showFullScreen()

    def add_logo(self, parent_widget):
        self.logo = QtWidgets.QLabel(parent_widget)
        self.logo.setGeometry(QtCore.QRect(410, 5, 60, 60))

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
        self.btn_inicio.setGeometry(QtCore.QRect(5, 5, 60, 28))

        self.btn_carga = QtWidgets.QPushButton("Carga Agua", self.centralwidget)
        self.btn_carga.setGeometry(QtCore.QRect(70, 5, 75, 28))

        self.btn_calentar = QtWidgets.QPushButton("Calentar Agua", self.centralwidget)
        self.btn_calentar.setGeometry(QtCore.QRect(150, 5, 90, 28))

        self.btn_enfriar = QtWidgets.QPushButton("Enfriar Agua", self.centralwidget)
        self.btn_enfriar.setGeometry(QtCore.QRect(245, 5, 90, 28))

        self.btn_vaciar = QtWidgets.QPushButton("Vaciar Agua", self.centralwidget)
        self.btn_vaciar.setGeometry(QtCore.QRect(340, 5, 90, 28))

    def create_stacked_pages(self):
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font2 = QtGui.QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(60)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 40, 480, 320))
        self.stackedWidget.setObjectName("stackedWidget")

        # Página 0: Inicio
        self.Inicio = QtWidgets.QWidget()
        self.Inicio.setObjectName("Inicio")
        self.pushButton = QtWidgets.QPushButton(self.Inicio)
        self.pushButton.setGeometry(QtCore.QRect(120, 100, 85, 40))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.Inicio)
        self.cleanButton = QtWidgets.QPushButton(self.Inicio)
        self.cleanButton.setGeometry(QtCore.QRect(280, 100, 85, 40))
        self.cleanButton.setObjectName("cleanButton")
        self.stackedWidget.addWidget(self.Inicio)
        self.btn_config = QtWidgets.QPushButton(self.centralwidget)
        self.btn_config.setGeometry(QtCore.QRect(420, 250, 30, 30))
        self.btn_config.setIcon(QtGui.QIcon("resources/settings.png"))  # Usa un ícono apropiado
        self.btn_config.setIconSize(QtCore.QSize(24, 24))
        self.btn_config.setFlat(True)


        # Página 1: Carga de Agua
        self.CargaAgua = QtWidgets.QWidget()
        self.CargaAgua.setObjectName("CargaAgua")

        self.volumen = QtWidgets.QLabel(self.CargaAgua)
        self.volumen.setGeometry(QtCore.QRect(190, 60, 70, 40))
        self.volumen.setFont(font)
        self.volumen.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.unit_vol = QtWidgets.QLabel(self.CargaAgua)
        self.unit_vol.setGeometry(QtCore.QRect(265, 60, 60, 40))
        self.unit_vol.setFont(font)

        self.caudal = QtWidgets.QLabel(self.CargaAgua)
        self.caudal.setGeometry(QtCore.QRect(190, 110, 70, 40))
        self.caudal.setFont(font)
        self.caudal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.units_caudal = QtWidgets.QLabel(self.CargaAgua)
        self.units_caudal.setGeometry(QtCore.QRect(265, 110, 80, 40))
        self.units_caudal.setFont(font)

        self.STOP = QtWidgets.QPushButton(self.CargaAgua)
        self.STOP.setGeometry(QtCore.QRect(195, 160, 90, 45))

        self.cargando_titulo = QtWidgets.QLabel(self.CargaAgua)
        self.cargando_titulo.setGeometry(QtCore.QRect(10, 10, 460, 40))
        self.cargando_titulo.setFont(font)
        self.cargando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.stackedWidget.addWidget(self.CargaAgua)

        # Página 2: Calentar Agua
        self.CalentarAgua = QtWidgets.QWidget()
        self.CalentarAgua.setObjectName("CalentarAgua")

        self.temp_2 = QtWidgets.QLabel(self.CalentarAgua)
        self.temp_2.setGeometry(QtCore.QRect(190, 100, 70, 40))
        self.temp_2.setFont(font)
        self.temp_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.units_2 = QtWidgets.QLabel(self.CalentarAgua)
        self.units_2.setGeometry(QtCore.QRect(265, 100, 60, 40))
        self.units_2.setFont(font)

        self.STOP_2 = QtWidgets.QPushButton(self.CalentarAgua)
        self.STOP_2.setGeometry(QtCore.QRect(195, 160, 90, 45))

        self.calentando_titulo = QtWidgets.QLabel(self.CalentarAgua)
        self.calentando_titulo.setGeometry(QtCore.QRect(10, 10, 460, 40))
        self.calentando_titulo.setFont(font)
        self.calentando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.stackedWidget.addWidget(self.CalentarAgua)

        # Página 3: Enfriar Agua
        self.EnfriarAgua = QtWidgets.QWidget()
        self.EnfriarAgua.setObjectName("EnfriarAgua")

        self.temp_3 = QtWidgets.QLabel(self.EnfriarAgua)
        self.temp_3.setGeometry(QtCore.QRect(190, 100, 70, 40))
        self.temp_3.setFont(font)
        self.temp_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.units_3 = QtWidgets.QLabel(self.EnfriarAgua)
        self.units_3.setGeometry(QtCore.QRect(265, 100, 60, 40))
        self.units_3.setFont(font)

        self.STOP_3 = QtWidgets.QPushButton(self.EnfriarAgua)
        self.STOP_3.setGeometry(QtCore.QRect(195, 160, 90, 45))

        self.enfriando_titulo = QtWidgets.QLabel(self.EnfriarAgua)
        self.enfriando_titulo.setGeometry(QtCore.QRect(10, 10, 460, 40))
        self.enfriando_titulo.setFont(font)
        self.enfriando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.stackedWidget.addWidget(self.EnfriarAgua)

        # Página 4: Vaciar Agua
        self.VaciarAgua = QtWidgets.QWidget()
        self.VaciarAgua.setObjectName("VaciarAgua")

        self.volumen_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.volumen_2.setGeometry(QtCore.QRect(190, 60, 70, 40))
        self.volumen_2.setFont(font)
        self.volumen_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.unit_vol_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.unit_vol_2.setGeometry(QtCore.QRect(265, 60, 60, 40))
        self.unit_vol_2.setFont(font)

        self.caudal_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.caudal_2.setGeometry(QtCore.QRect(190, 110, 70, 40))
        self.caudal_2.setFont(font)
        self.caudal_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.units_caudal_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.units_caudal_2.setGeometry(QtCore.QRect(265, 110, 80, 40))
        self.units_caudal_2.setFont(font)

        self.STOP_4 = QtWidgets.QPushButton(self.VaciarAgua)
        self.STOP_4.setGeometry(QtCore.QRect(195, 160, 90, 45))

        self.vaciando_titulo = QtWidgets.QLabel(self.VaciarAgua)
        self.vaciando_titulo.setGeometry(QtCore.QRect(10, 10, 460, 40))
        self.vaciando_titulo.setFont(font)
        self.vaciando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.stackedWidget.addWidget(self.VaciarAgua)

        # Página 5: Limpieza
        self.Limpieza = QtWidgets.QWidget()
        self.Limpieza.setObjectName("Limpieza")

        self.limpieza_titulo = QtWidgets.QLabel(self.Limpieza)
        self.limpieza_titulo.setGeometry(QtCore.QRect(10, 10, 460, 40))
        self.limpieza_titulo.setFont(font)
        self.limpieza_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.STOP_limpieza = QtWidgets.QPushButton(self.Limpieza)
        self.STOP_limpieza.setGeometry(QtCore.QRect(195, 160, 90, 45))

        self.stackedWidget.addWidget(self.Limpieza)

        # Página 6: Configuración 1 (Volumen Llenado, Temperatura High)
        self.Config1 = QtWidgets.QWidget()
        self.Config1.setObjectName("Config1")

        self.param_title1 = QtWidgets.QLabel(self.Config1)
        self.param_title1.setGeometry(QtCore.QRect(10, 10, 460, 40))
        self.param_title1.setFont(font)
        self.param_title1.setAlignment(QtCore.Qt.AlignCenter)
        self.param_title1.setText("Parámetros (1/2)")

        # Volumen Llenado
        self.lbl_vol_llenado = QtWidgets.QLabel("Volumen Llenado:", self.Config1)
        self.lbl_vol_llenado.setGeometry(QtCore.QRect(60, 70, 200, 40))
        self.lbl_vol_llenado.setFont(font2)

        self.btn_dec_vol_llenado = QtWidgets.QPushButton("-", self.Config1)
        self.btn_dec_vol_llenado.setGeometry(QtCore.QRect(240, 70, 40, 40))

        self.val_vol_llenado = QtWidgets.QLabel("15", self.Config1)
        self.val_vol_llenado.setGeometry(QtCore.QRect(285, 70, 40, 40))
        self.val_vol_llenado.setFont(font)
        self.val_vol_llenado.setAlignment(QtCore.Qt.AlignCenter)

        self.btn_inc_vol_llenado = QtWidgets.QPushButton("+", self.Config1)
        self.btn_inc_vol_llenado.setGeometry(QtCore.QRect(330, 70, 40, 40))

        # Temperatura High
        self.lbl_temp_high = QtWidgets.QLabel("Temperatura High:", self.Config1)
        self.lbl_temp_high.setGeometry(QtCore.QRect(60, 130, 200, 40))
        self.lbl_temp_high.setFont(font2)

        self.btn_dec_temp_high = QtWidgets.QPushButton("-", self.Config1)
        self.btn_dec_temp_high.setGeometry(QtCore.QRect(240, 130, 40, 40))

        self.val_temp_high = QtWidgets.QLabel("100", self.Config1)
        self.val_temp_high.setGeometry(QtCore.QRect(285, 130, 40, 40))
        self.val_temp_high.setFont(font)
        self.val_temp_high.setAlignment(QtCore.Qt.AlignCenter)

        self.btn_inc_temp_high = QtWidgets.QPushButton("+", self.Config1)
        self.btn_inc_temp_high.setGeometry(QtCore.QRect(330, 130, 40, 40))

        # Botón para ir a siguiente página
        self.btn_siguiente_config = QtWidgets.QPushButton("Siguiente", self.Config1)
        self.btn_siguiente_config.setGeometry(QtCore.QRect(190, 200, 100, 40))

        self.stackedWidget.addWidget(self.Config1)


        # Página 7: Configuración 2 (Temperatura Low, Volumen Vaciado)
        self.Config2 = QtWidgets.QWidget()
        self.Config2.setObjectName("Config2")

        self.param_title2 = QtWidgets.QLabel(self.Config2)
        self.param_title2.setGeometry(QtCore.QRect(10, 10, 460, 40))
        self.param_title2.setFont(font)
        self.param_title2.setAlignment(QtCore.Qt.AlignCenter)
        self.param_title2.setText("Parámetros (2/2)")

        # Temperatura Low
        self.lbl_temp_low = QtWidgets.QLabel("Temperatura Low:", self.Config2)
        self.lbl_temp_low.setGeometry(QtCore.QRect(60, 70, 200, 40))
        self.lbl_temp_low.setFont(font2)

        self.btn_dec_temp_low = QtWidgets.QPushButton("-", self.Config2)
        self.btn_dec_temp_low.setGeometry(QtCore.QRect(240, 70, 40, 40))

        self.val_temp_low = QtWidgets.QLabel("80", self.Config2)
        self.val_temp_low.setGeometry(QtCore.QRect(285, 70, 40, 40))
        self.val_temp_low.setFont(font)
        self.val_temp_low.setAlignment(QtCore.Qt.AlignCenter)

        self.btn_inc_temp_low = QtWidgets.QPushButton("+", self.Config2)
        self.btn_inc_temp_low.setGeometry(QtCore.QRect(330, 70, 40, 40))

        # Volumen Vaciado
        self.lbl_vol_vaciado = QtWidgets.QLabel("Volumen Vaciado:", self.Config2)
        self.lbl_vol_vaciado.setGeometry(QtCore.QRect(60, 130, 200, 40))
        self.lbl_vol_vaciado.setFont(font2)

        self.btn_dec_vol_vaciado = QtWidgets.QPushButton("-", self.Config2)
        self.btn_dec_vol_vaciado.setGeometry(QtCore.QRect(240, 130, 40, 40))

        self.val_vol_vaciado = QtWidgets.QLabel("10", self.Config2)
        self.val_vol_vaciado.setGeometry(QtCore.QRect(285, 130, 40, 40))
        self.val_vol_vaciado.setFont(font)
        self.val_vol_vaciado.setAlignment(QtCore.Qt.AlignCenter)

        self.btn_inc_vol_vaciado = QtWidgets.QPushButton("+", self.Config2)
        self.btn_inc_vol_vaciado.setGeometry(QtCore.QRect(330, 130, 40, 40))

        # Botón para volver al inicio
        self.btn_guardar_config = QtWidgets.QPushButton("Guardar", self.Config2)
        self.btn_guardar_config.setGeometry(QtCore.QRect(280, 200, 100, 40))

        self.stackedWidget.addWidget(self.Config2)
        # Botón para volver a la página anterior (Configuración 1)
        self.btn_atras_config = QtWidgets.QPushButton("Atrás", self.Config2)
        self.btn_atras_config.setGeometry(QtCore.QRect(190, 200, 80, 40))



    def create_additional_labels(self, parent_widget):
        self.label = QtWidgets.QLabel(parent_widget)
        self.label.setGeometry(QtCore.QRect(5, 260, 150, 18))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent_widget)
        self.label_2.setGeometry(QtCore.QRect(5, 280, 150, 18))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent_widget)
        self.label_3.setGeometry(QtCore.QRect(5, 300, 150, 18))
        self.label_3.setObjectName("label_3")

    def setup_statusbar(self, MainWindow):
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema Agua"))

        self.pushButton.setText(_translate("MainWindow", "Inicio"))
        self.cleanButton.setText(_translate("MainWindow", "Limpieza"))


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

        self.limpieza_titulo.setText(_translate("MainWindow", "Limpieza del Sistema"))
        self.STOP_limpieza.setText(_translate("MainWindow", "STOP"))

        


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
        # self.btn_config.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.btn_siguiente_config.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
        # self.btn_guardar_config.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btn_atras_config.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
