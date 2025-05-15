from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)

        self.create_central_widget(MainWindow)
        self.add_logo(MainWindow)
        # self.create_navigation_buttons() # Comentar en codigo final
        self.create_stacked_pages()
        self.create_additional_labels(MainWindow)
        self.setup_statusbar(MainWindow)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)  # Página inicial
        self.set_style(MainWindow)  # Aplicar estilos
        # self.connect_buttons() # comentar en codigo final

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_logo(self, parent_widget):
        # from PyQt5 import QtGui, QtCore, QtWidgets

        self.logo = QtWidgets.QLabel(parent_widget)
        self.logo.setGeometry(QtCore.QRect(520, -10, 100, 100))  # Ajusta posición y tamaño

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
        self.btn_inicio = QtWidgets.QPushButton("Inicio", self.centralwidget)
        self.btn_inicio.setGeometry(QtCore.QRect(10, 10, 80, 40))
        self.btn_inicio.setObjectName("btn_inicio")

        self.btn_carga = QtWidgets.QPushButton("Carga Agua", self.centralwidget)
        self.btn_carga.setGeometry(QtCore.QRect(100, 10, 100, 40))
        self.btn_carga.setObjectName("btn_carga")

        self.btn_calentar = QtWidgets.QPushButton("Calentar Agua", self.centralwidget)
        self.btn_calentar.setGeometry(QtCore.QRect(210, 10, 110, 40))
        self.btn_calentar.setObjectName("btn_calentar")

        self.btn_enfriar = QtWidgets.QPushButton("Enfriar Agua", self.centralwidget)
        self.btn_enfriar.setGeometry(QtCore.QRect(330, 10, 110, 40))
        self.btn_enfriar.setObjectName("btn_enfriar")

        self.btn_vaciar = QtWidgets.QPushButton("Vaciar Agua", self.centralwidget)
        self.btn_vaciar.setGeometry(QtCore.QRect(450, 10, 110, 40))
        self.btn_vaciar.setObjectName("btn_vaciar")

    def create_stacked_pages(self):
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 60, 640, 400))
        self.stackedWidget.setMinimumSize(QtCore.QSize(640, 0))
        self.stackedWidget.setObjectName("stackedWidget")

        # Página 0: Inicio
        self.Inicio = QtWidgets.QWidget()
        self.Inicio.setObjectName("Inicio")
        self.pushButton = QtWidgets.QPushButton(self.Inicio)
        self.pushButton.setGeometry(QtCore.QRect(240, 110, 171, 81))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.Inicio)

        # Página 1: Carga de Agua
        self.CargaAgua = QtWidgets.QWidget()
        self.CargaAgua.setObjectName("CargaAgua")

        self.volumen = QtWidgets.QLabel(self.CargaAgua)
        self.volumen.setGeometry(QtCore.QRect(200, 90, 171, 71))
        self.volumen.setFont(font)
        self.volumen.setObjectName("volumen")
        self.volumen.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.unit_vol = QtWidgets.QLabel(self.CargaAgua)
        self.unit_vol.setGeometry(QtCore.QRect(390, 90, 171, 71))
        self.unit_vol.setFont(font)
        self.unit_vol.setObjectName("unit_vol")

        self.caudal = QtWidgets.QLabel(self.CargaAgua)
        self.caudal.setGeometry(QtCore.QRect(200, 160, 171, 71))
        self.caudal.setFont(font)
        self.caudal.setObjectName("caudal")
        self.caudal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.units_caudal = QtWidgets.QLabel(self.CargaAgua)
        self.units_caudal.setGeometry(QtCore.QRect(380, 160, 171, 71))
        self.units_caudal.setFont(font)
        self.units_caudal.setObjectName("units_caudal")

        self.STOP = QtWidgets.QPushButton(self.CargaAgua)
        self.STOP.setGeometry(QtCore.QRect(250, 280, 171, 81))
        self.STOP.setObjectName("STOP")

        self.cargando_titulo = QtWidgets.QLabel(self.CargaAgua)
        self.cargando_titulo.setGeometry(QtCore.QRect(20, 10, 611, 71))
        self.cargando_titulo.setFont(font)
        self.cargando_titulo.setObjectName("cargando_titulo")
        self.cargando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.stackedWidget.addWidget(self.CargaAgua)

        # Página 2: Calentar Agua
        self.CalentarAgua = QtWidgets.QWidget()
        self.CalentarAgua.setObjectName("CalentarAgua")

        self.units_2 = QtWidgets.QLabel(self.CalentarAgua)
        self.units_2.setGeometry(QtCore.QRect(360, 130, 171, 71))
        self.units_2.setFont(font)
        self.units_2.setObjectName("units_2")

        self.temp_2 = QtWidgets.QLabel(self.CalentarAgua)
        self.temp_2.setGeometry(QtCore.QRect(180, 130, 171, 71))
        self.temp_2.setFont(font)
        self.temp_2.setObjectName("temp_2")
        self.temp_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.STOP_2 = QtWidgets.QPushButton(self.CalentarAgua)
        self.STOP_2.setGeometry(QtCore.QRect(250, 280, 171, 81))
        self.STOP_2.setObjectName("STOP_2")

        self.calentando_titulo = QtWidgets.QLabel(self.CalentarAgua)
        self.calentando_titulo.setGeometry(QtCore.QRect(30, 20, 611, 71))
        self.calentando_titulo.setFont(font)
        self.calentando_titulo.setObjectName("calentando_titulo")
        self.calentando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.stackedWidget.addWidget(self.CalentarAgua)

        # Página 3: Enfriar Agua
        self.EnfriarAgua = QtWidgets.QWidget()
        self.EnfriarAgua.setObjectName("EnfriarAgua")

        self.temp_3 = QtWidgets.QLabel(self.EnfriarAgua)
        self.temp_3.setGeometry(QtCore.QRect(170, 140, 171, 71))
        self.temp_3.setFont(font)
        self.temp_3.setObjectName("temp_3")
        self.temp_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.units_3 = QtWidgets.QLabel(self.EnfriarAgua)
        self.units_3.setGeometry(QtCore.QRect(350, 140, 171, 71))
        self.units_3.setFont(font)
        self.units_3.setObjectName("units_3")

        self.STOP_3 = QtWidgets.QPushButton(self.EnfriarAgua)
        self.STOP_3.setGeometry(QtCore.QRect(250, 280, 171, 81))
        self.STOP_3.setObjectName("STOP_3")

        self.enfriando_titulo = QtWidgets.QLabel(self.EnfriarAgua)
        self.enfriando_titulo.setGeometry(QtCore.QRect(30, 20, 611, 71))
        self.enfriando_titulo.setFont(font)
        self.enfriando_titulo.setObjectName("enfriando_titulo")
        self.enfriando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.stackedWidget.addWidget(self.EnfriarAgua)

        # Página 4: Vaciar Agua
        self.VaciarAgua = QtWidgets.QWidget()
        self.VaciarAgua.setObjectName("VaciarAgua")

        self.unit_vol_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.unit_vol_2.setGeometry(QtCore.QRect(360, 80, 171, 71))
        self.unit_vol_2.setFont(font)
        self.unit_vol_2.setObjectName("unit_vol_2")

        self.volumen_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.volumen_2.setGeometry(QtCore.QRect(180, 80, 171, 71))
        self.volumen_2.setFont(font)
        self.volumen_2.setObjectName("volumen_2")
        self.volumen_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.caudal_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.caudal_2.setGeometry(QtCore.QRect(180, 170, 171, 71))
        self.caudal_2.setFont(font)
        self.caudal_2.setObjectName("caudal_2")
        self.caudal_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.units_caudal_2 = QtWidgets.QLabel(self.VaciarAgua)
        self.units_caudal_2.setGeometry(QtCore.QRect(360, 170, 171, 71))
        self.units_caudal_2.setFont(font)
        self.units_caudal_2.setObjectName("units_caudal_2")

        self.STOP_4 = QtWidgets.QPushButton(self.VaciarAgua)
        self.STOP_4.setGeometry(QtCore.QRect(250, 280, 171, 81))
        self.STOP_4.setObjectName("STOP_4")

        self.vaciando_titulo = QtWidgets.QLabel(self.VaciarAgua)
        self.vaciando_titulo.setGeometry(QtCore.QRect(20, 0, 611, 71))
        self.vaciando_titulo.setFont(font)
        self.vaciando_titulo.setObjectName("vaciando_titulo")
        self.vaciando_titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.stackedWidget.addWidget(self.VaciarAgua)

    def create_additional_labels(self, parent_widget):
        self.label = QtWidgets.QLabel(parent_widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 120, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent_widget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 150, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent_widget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 100, 16))
        self.label_3.setObjectName("label_3")

    def setup_statusbar(self, MainWindow):
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def connect_buttons(self):
        self.btn_inicio.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btn_carga.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btn_calentar.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btn_enfriar.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.btn_vaciar.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))


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
                font-size: 18px;
                padding: 10px;
                transition: background-color 0.3s ease;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QLabel {
                font-weight: bold;
            }
            QLabel#cargando_titulo, QLabel#vaciando_titulo, QLabel#enfriando_titulo, QLabel#calentando_titulo {
                font-size: 20pt;
                color: #3498db; /* Cambié el rojo a azul */
            }
            QLabel#volumen, QLabel#caudal, QLabel#temp_2, QLabel#temp_3, QLabel#volumen_2, QLabel#caudal_2 {
                font-size: 26pt;
            }
            QLabel#unit_vol, QLabel#units_caudal, QLabel#units_2, QLabel#units_3, QLabel#unit_vol_2, QLabel#units_caudal_2 {
                font-size: 22pt;
                color: #bdc3c7;
            }
            QLabel#label, QLabel#label_2, QLabel#label_3 {
                font-size: 12pt;
                color: #95a5a6;
            }
        """)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Empezar Proceso"))
        self.volumen.setText(_translate("MainWindow", "30"))
        self.unit_vol.setText(_translate("MainWindow", "L"))
        self.caudal.setText(_translate("MainWindow", "30"))
        self.units_caudal.setText(_translate("MainWindow", "L/min"))
        self.STOP.setText(_translate("MainWindow", "STOP"))
        self.cargando_titulo.setText(_translate("MainWindow", "CARGANDO AGUA A LA OLLA 1"))
        self.units_2.setText(_translate("MainWindow", "ºC"))
        self.temp_2.setText(_translate("MainWindow", "30"))
        self.STOP_2.setText(_translate("MainWindow", "STOP"))
        self.calentando_titulo.setText(_translate("MainWindow", "CALENTANDO..."))
        self.temp_3.setText(_translate("MainWindow", "30"))
        self.units_3.setText(_translate("MainWindow", "ºC"))
        self.STOP_3.setText(_translate("MainWindow", "STOP"))
        self.enfriando_titulo.setText(_translate("MainWindow", "ENFRIANDO..."))
        self.unit_vol_2.setText(_translate("MainWindow", "L"))
        self.volumen_2.setText(_translate("MainWindow", "30"))
        self.caudal_2.setText(_translate("MainWindow", "30"))
        self.units_caudal_2.setText(_translate("MainWindow", "L/min"))
        self.STOP_4.setText(_translate("MainWindow", "STOP"))
        self.vaciando_titulo.setText(_translate("MainWindow", "VACIANDO AGUA DE LA OLLA 1"))
        self.label.setText(_translate("MainWindow", "ISABA 2025"))
        self.label_2.setText(_translate("MainWindow", "German Bueno"))
        self.label_3.setText(_translate("MainWindow", "Pol Pavo"))
