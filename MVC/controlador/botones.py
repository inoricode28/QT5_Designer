from  PySide2 import QtWidgets , QtCore
import sys
#Vista.ui_botones eso signidica Carpeta.archivo
from vista.ui_botones import Ui_MainWindow #Ui_MainWindow es la clase que se encuentra en la particula
#El nombre de la clase es cambiable
#Driver el controlador
class Clark(QtWidgets.QMainWindow):#Boton es cambiable
    
    def __init__(self, *args , parent=None):
        
        super(Clark, self).__init__(parent)#Boton es cambiable
        self.venPri = Ui_MainWindow()# Particula
        self.venPri.setupUi(self)  
        self.venPri.pushButton_5.clicked.connect(lambda: self.close())
        self.venPri.pushButton_6.clicked.connect(self.cerrar)
    
    def cerrar(self):
        self.close()
        
    