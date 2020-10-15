from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from Particulas import Particulas
from particula import Particula

# la clase mainwindow hereda lo de QMainWindow
class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()

        self.particula = Particula()
        self.particulas = Particulas()
        #al declarar el objeto de manera globar ya podemos crear particulas

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Inicio_pushButton.clicked.connect(self.agregar_Particula_Inicio)
        self.ui.Final_pushButton.clicked.connect(self.agregar_Particula_Final)
        self.ui.pushButton_2.clicked.connect(self.mostrar_Particula)



    @Slot()
    def agregar_Particula_Inicio(self):
        id = self.ui.ID_lineEdit.text()
        origenX = self.ui.origenX_spinBox.value()
        origenY = self.ui.origenY_spinBox.value()
        destinoX = self.ui.destinoX_spinBox.value()
        destinoY = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        colorR = self.ui.R_spinBox.value()
        colorG = self.ui.G_spinBox.value()
        colorB = self.ui.B_spinBox.value()

        particula = Particula(id, origenX, origenY, destinoX, destinoY, velocidad, colorR, colorG, colorB)
        self.particulas.agregar_inicio(particula)
            

    @Slot()
    def agregar_Particula_Final(self):
        id = self.ui.ID_lineEdit.text()
        origenX = self.ui.origenX_spinBox.value()
        origenY = self.ui.origenY_spinBox.value()
        destinoX = self.ui.destinoX_spinBox.value()
        destinoY = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        colorR = self.ui.R_spinBox.value()
        colorG = self.ui.G_spinBox.value()
        colorB = self.ui.B_spinBox.value()

        particula = Particula(id, origenX, origenY, destinoX, destinoY, velocidad, colorR, colorG, colorB)
        self.particulas.agregar_final(particula)


    @Slot()
    def mostrar_Particula(self):
        #self.particulas.mostrar()
        self.ui.salida.clear(
            
        )
        self.ui.salida.insertPlainText(str(self.particulas))