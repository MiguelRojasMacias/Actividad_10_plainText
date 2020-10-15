# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(287, 411)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.origenY_spinBox = QSpinBox(self.centralwidget)
        self.origenY_spinBox.setObjectName(u"origenY_spinBox")
        self.origenY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origenY_spinBox, 3, 7, 1, 1)

        self.salida = QPlainTextEdit(self.centralwidget)
        self.salida.setObjectName(u"salida")

        self.gridLayout.addWidget(self.salida, 9, 0, 1, 11)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 1)

        self.velocidad_spinBox = QSpinBox(self.centralwidget)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setMaximum(100)

        self.gridLayout.addWidget(self.velocidad_spinBox, 6, 2, 1, 3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 2, 2)

        self.Final_pushButton = QPushButton(self.centralwidget)
        self.Final_pushButton.setObjectName(u"Final_pushButton")

        self.gridLayout.addWidget(self.Final_pushButton, 8, 4, 1, 4)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 7, 5, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 8, 8, 1, 3)

        self.origenX_spinBox = QSpinBox(self.centralwidget)
        self.origenX_spinBox.setObjectName(u"origenX_spinBox")
        self.origenX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origenX_spinBox, 3, 2, 1, 2)

        self.ID_lineEdit = QLineEdit(self.centralwidget)
        self.ID_lineEdit.setObjectName(u"ID_lineEdit")

        self.gridLayout.addWidget(self.ID_lineEdit, 1, 1, 1, 4)

        self.Inicio_pushButton = QPushButton(self.centralwidget)
        self.Inicio_pushButton.setObjectName(u"Inicio_pushButton")

        self.gridLayout.addWidget(self.Inicio_pushButton, 8, 0, 1, 4)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 2)

        self.B_spinBox = QSpinBox(self.centralwidget)
        self.B_spinBox.setObjectName(u"B_spinBox")
        self.B_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.B_spinBox, 7, 10, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 4, 1, 2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 4, 1, 2)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 7, 9, 1, 1)

        self.destinoX_spinBox = QSpinBox(self.centralwidget)
        self.destinoX_spinBox.setObjectName(u"destinoX_spinBox")
        self.destinoX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinoX_spinBox, 5, 2, 1, 2)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 5, 1, 2)

        self.destinoY_spinBox = QSpinBox(self.centralwidget)
        self.destinoY_spinBox.setObjectName(u"destinoY_spinBox")
        self.destinoY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinoY_spinBox, 5, 7, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 5, 5, 1, 2)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 7, 2, 1, 1)

        self.G_spinBox = QSpinBox(self.centralwidget)
        self.G_spinBox.setObjectName(u"G_spinBox")
        self.G_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.G_spinBox, 7, 6, 1, 2)

        self.R_spinBox = QSpinBox(self.centralwidget)
        self.R_spinBox.setObjectName(u"R_spinBox")
        self.R_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.R_spinBox, 7, 3, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 287, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.Final_pushButton.setText(QCoreApplication.translate("MainWindow", u"AGREGAR FINAL", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"MOSTRAR", None))
        self.Inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"AGREGAR INICIO", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DESTINO", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ORIGEN", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"R", None))
    # retranslateUi

