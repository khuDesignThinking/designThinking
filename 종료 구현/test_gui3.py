# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_gui3.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import thread
import time
from threading import Thread
import GUI_main
photo1="resource\image\profile.png"
photo2="resource\image\profile2.png"
phototemp=""

class Thread1(QThread):
    def __init__(self, parent):
        super().__init__(parent)
    def run(self):
        thread.detect_blink()

class Thread2(QThread):
    vid = GUI_main.ShowVideo()
    image_viewer1 = GUI_main.ImageViewer()
    vid.VideoSignal1.connect(image_viewer1.setImage)
    def __init__(self, parent):
        super().__init__(parent)
    def run(self):
        self.vid.startVideo()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(738, 428)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 301, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resource\image\profile.png"))
        self.label.setObjectName("label")

        self.gender = QtWidgets.QComboBox(self.centralwidget)
        self.gender.setGeometry(QtCore.QRect(360, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 M")
        font.setPointSize(10)
        self.gender.setFont(font)
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.addItem("")

        self.age = QtWidgets.QComboBox(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(360, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 M")
        font.setPointSize(10)
        self.age.setFont(font)
        self.age.setObjectName("age")
        self.age.addItem("")
        self.age.addItem("")
        self.age.addItem("")
        self.age.addItem("")
        self.age.addItem("")
        self.age.addItem("")
        self.age.addItem("")
        self.age.addItem("")
        self.age.addItem("")

        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(520, 30, 191, 51))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 B")
        font.setPointSize(12)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")

        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(520, 100, 191, 51))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 B")
        font.setPointSize(12)
        self.stop_btn.setFont(font)
        self.stop_btn.setObjectName("stop_btn")

        self.graphic_show = QtWidgets.QPushButton("그래프 나타내기", self.centralwidget)
        self.graphic_show.setGeometry(QtCore.QRect(552, 186, 141, 48))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 B")
        font.setPointSize(12)
        self.graphic_show.setFont(font)
        self.graphic_show.setObjectName("graphic_show")

        self.graphic_hide = QtWidgets.QPushButton("그래프 숨기기", self.centralwidget)
        self.graphic_hide.setGeometry(QtCore.QRect(552, 240, 141, 81))
        self.graphic_hide.setFont(font)
        self.graphic_hide.setObjectName("graphic_hide")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(9, 363, 720, 480))
        self.widget.setObjectName("widget")

        self.graphicsView = QtWidgets.QLabel(self.widget)
        self.graphicsView.setGeometry(QtCore.QRect(9, 9, 700, 460))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setPixmap(QtGui.QPixmap("dataset/graph.jpg"))

        self.graphic_hide.setEnabled(False)
        self.graphic_show.setEnabled(True)
        self.widget.hide()
        self.centralwidget.setFixedSize(738, 408)
        MainWindow.setFixedSize(738, 428)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 170, 151, 51))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 B")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 230, 151, 81))
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setPixmap(QtGui.QPixmap("resource\image\Soso.png"))
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 290, 31, 28))
        self.pushButton.setText("")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource\image\change.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.dialog = QDialog()
        
        self.pushButton.clicked.connect(self.change_profile)
        self.start_btn.clicked.connect(self.ready_start) #@@@@@@@@@@@
        self.start_btn.clicked.connect(self.select_g)
        self.start_btn.clicked.connect(self.select_a)
        self.start_btn.clicked.connect(self.db_starter)
        self.start_btn.clicked.connect(self.us_starter)
        self.start_btn.clicked.connect(self.gp_starter)
        self.start_btn.clicked.connect(self.gp_updater)
        self.start_btn.clicked.connect(self.dialog_open)
        self.start_btn.clicked.connect(self.d_su_starter)

        self.graphic_hide.clicked.connect(lambda: self.hide_graphic(MainWindow))
        self.graphic_show.clicked.connect(lambda: self.show_graphic(MainWindow))

    def ready_start(self): #@@@@@@@@@@@@@@@@@@@@
        thread.exit_condition = False
        time.sleep(0.1)

    def show_graphic(self, MainWindow):
        self.graphic_hide.setEnabled(True)
        self.graphic_show.setEnabled(False)
        self.widget.show()
        self.centralwidget.setFixedSize(738, 852)
        MainWindow.setFixedSize(738, 872)

    def hide_graphic(self, MainWindow):
        self.graphic_hide.setEnabled(False)
        self.graphic_show.setEnabled(True)
        self.widget.hide()
        self.centralwidget.setFixedSize(738, 408)
        MainWindow.setFixedSize(738, 428)

    def dialog_open(self):
        self.hide()
        self.dialog.setWindowTitle('Dialog')
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(363, 232)

        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()
        widget = self.dialog.geometry()
        x = ag.width() - widget.width()
        y = 2 * ag.height() - sg.height() - widget.height()
        self.dialog.move(x, y)

        self.labDialog = QtWidgets.QLabel(self.dialog)
        self.labDialog.setGeometry(10, 10, 341, 141)
        self.labDialog.setText("")
        self.labDialog.setObjectName("labDialog")
        self.labDialog.setAlignment(QtCore.Qt.AlignCenter)

        self.btnDialog = QtWidgets.QPushButton("측정 종료", self.dialog)
        self.btnDialog.setGeometry(110, 180, 151, 41)
        self.btnDialog.setObjectName("btnDialog")
        self.btnDialog.clicked.connect(self.dialog_close)

        self.dialog.show()

    def dialog_close(self):
        thread.exit_condition = True #@@@@@@@@@@@@@
        Thread2.vid.stopVideo() #@@@@@@@@@@@@@@
        self.dialog.close()
        self.show()

    def dialog_status_update(self):
        while(not thread.exit_condition):#@@@@@@@@@@@@@@@@
            time.sleep(10)
            cnt_blink = thread.cnt_blink
            if(cnt_blink <=1):
                self.labDialog.setPixmap(QtGui.QPixmap("resource\image\Bad.png"))
            elif(1 < cnt_blink <=3):
                self.labDialog.setPixmap(QtGui.QPixmap("resource\image\Soso.png"))
            elif(cnt_blink >3):
                self.labDialog.setPixmap(QtGui.QPixmap("resource\image\Good.png"))

    def d_su_starter(self):
        d_x = Thread(target = self.dialog_status_update, args=())
        d_x.start()

    def db_starter(self):
        x = Thread1(self)
        x.start()
    def us_starter(self):
        y = Thread(target = self.update_status, args=())
        y.start()
    def gp_starter(self):
        z = Thread2(self)
        z.start()
    def gp_updater(self):
        w = Thread(target = self.update_gp, args=())
        w.start()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gender.setItemText(0, _translate("MainWindow", "여성"))
        self.gender.setItemText(1, _translate("MainWindow", "남성"))
        self.age.setItemText(0, _translate("MainWindow", "10대"))
        self.age.setItemText(1, _translate("MainWindow", "20대"))
        self.age.setItemText(2, _translate("MainWindow", "30대"))
        self.age.setItemText(3, _translate("MainWindow", "40대"))
        self.age.setItemText(4, _translate("MainWindow", "50대"))
        self.age.setItemText(5, _translate("MainWindow", "60대"))
        self.age.setItemText(6, _translate("MainWindow", "70대"))
        self.age.setItemText(7, _translate("MainWindow", "80대"))
        self.age.setItemText(8, _translate("MainWindow", "90대"))
        self.start_btn.setText(_translate("MainWindow", "측정 시작"))
        self.stop_btn.setText(_translate("MainWindow", "측정 중지"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">현재 상태</p></body></html>"))
    
    def change_profile(self):
        global photo1, photo2, phototemp
        self.label.setPixmap(QtGui.QPixmap(photo2))
        phototemp=photo1
        photo1=photo2
        photo2=phototemp
    
    def select_g(self):
        global gender
        gender=self.gender.currentText()
        print(self.gender.currentText())
    
    def select_a(self):
        global age
        age=self.age.currentText()
        print(self.age.currentText())
        
    def update_status(self):
        while(not thread.exit_condition):#@@@@@@@@@@@@@@@
            time.sleep(10)
            cnt_blink = thread.cnt_blink
            if(cnt_blink <=1):
              self.label_3.setPixmap(QtGui.QPixmap("resource\image\Bad.png"))
            elif(1 < cnt_blink <=3):
              self.label_3.setPixmap(QtGui.QPixmap("resource\image\Soso.png"))
            elif(cnt_blink >3):
              self.label_3.setPixmap(QtGui.QPixmap("resource\image\Good.png"))
              
    def update_gp(self):
        while(not thread.exit_condition):#@@@@@@@@@@@@@@
            time.sleep(10)
            self.graphicsView.setPixmap(QtGui.QPixmap("dataset/graph.jpg"))
        
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
