import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from GUI_main import Ui_MainWindow 

class kinwriter(QMainWindow, Ui_MainWindow): 
    
    def __init__(self):

        super().__init__()

        self.setupUi(self)

        self.show()

app = QApplication([])
app.setQuitOnLastWindowClosed(False)
sn = kinwriter()
QApplication.processEvents()
sys.exit(app.exec_())
