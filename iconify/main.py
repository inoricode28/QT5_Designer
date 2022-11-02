import sys
import iconify as ico
from iconify.qt import QtGui,QtWidgets
from PySide2.QtCore import *

from ui_infercas_icon import *
class MainWindows(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        anim = ico.anim.Spin()

        icon = ico.Icon('feather:settings', color=QtGui.QColor('orange'),anim=anim)
        #self.ui.pushButton.setIcon(icon)
        icon.setAsButtonIcon(self.ui.pushButton)
        anim.start()
        self.ui.pushButton.setIconSize(QSize(64,64))
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindows()
    window.show()
    sys.exit(app.exec_())



