import sys
from Gui_test1 import Ui_MainWindow 
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from threading import Thread
import time


class kinwriter(QMainWindow, Ui_MainWindow): 
    
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.show()



app = QApplication([])
sn = kinwriter()
QApplication.processEvents()
sys.exit(app.exec_())
