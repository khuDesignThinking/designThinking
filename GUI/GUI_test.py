"""
deb : luckydipper
date : 2020/10/23
copy from https://webnautes.tistory.com/1290
next thing I have to do is combine Grapic_User_interface.py & _GUI.py module
"""
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class OurApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def bt1_clicked(self):
        QMessageBox.about(self, "message", "clicked")


    def initUI(self):
        self.setWindowTitle('CITIZEN CLASS PROJECT')
        self.setWindowIcon(QIcon('./resource/images/networking.png'))
        self.setGeometry(300, 300, 300, 200)
        self.move(300,300)
        self.resize(600,400)


        label1 = QLabel('result', self)
        label1.setAlignment(Qt.AlignCenter)
        font1 = label1.font()
        font1.setPointSize(10)


        bt1 = QPushButton("Auto Capture", self)
        bt2 = QPushButton("Manual Capture", self)

        bt1.clicked.connect(self.bt1_clicked)

        layout = QVBoxLayout()

        layout.addWidget(bt1)
        layout.addWidget(bt2)
        layout.addWidget(label1)
        
        self.setLayout(layout)
        self.show()



if __name__ == '__main__':
    print(sys.argv)
    app = QApplication(sys.argv)
    ex = OurApp()
    sys.exit(app.exec_())

