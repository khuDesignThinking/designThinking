from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import countBlink
import time
import source
from threading import Thread
import GUI_graph
import winsound
import control_brightness as bright

class Thread1(QThread):
    def __init__(self, parent):
        super().__init__(parent)
    def run(self):
        countBlink.detect_blink()

class Thread2(QThread):
    vid = GUI_graph.ShowVideo()
    image_viewer1 = GUI_graph.ImageViewer()
    vid.VideoSignal1.connect(image_viewer1.setImage)
    def __init__(self, parent):
        super().__init__(parent)
    def run(self):
        self.vid.startVideo()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 165)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gender = QtWidgets.QComboBox(self.centralwidget)
        self.gender.setGeometry(QtCore.QRect(19, 19, 134, 20))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 M")
        font.setPointSize(9)
        self.gender.setFont(font)
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.addItem("")

        self.age = QtWidgets.QComboBox(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(19, 45, 134, 20))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 M")
        font.setPointSize(9)
        self.age.setFont(font)
        self.age.setObjectName("age")
        self.age.addItem("")
        self.age.addItem("")

        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(159, 19, 133, 46))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 B")
        font.setPointSize(12)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")

        self.brightness_check = QtWidgets.QCheckBox(self.centralwidget)
        self.brightness_check.setGeometry(QtCore.QRect(28, 84, 125, 16))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 B")
        font.setPointSize(9)
        self.brightness_check.setFont(font)
        self.brightness_check.setObjectName("brightness_check")

        self.sound_alarm = QtWidgets.QCheckBox("음성 알림", self.centralwidget)
        self.sound_alarm.setGeometry(QtCore.QRect(28, 114, 125, 16))
        self.sound_alarm.setFont(font)
        self.sound_alarm.setObjectName("sound_alarm")

        #눈건강 메뉴얼 
        self.manual = QtWidgets.QPushButton("눈건강 info", self.centralwidget)
        self.manual.setGeometry(QtCore.QRect(159, 110, 124, 24))
        font.setPointSize(10)
        self.manual.setFont(font)
        self.manual.setObjectName("manual")

        self.graphic_show = QtWidgets.QPushButton("그래프 나타내기", self.centralwidget)
        self.graphic_show.setGeometry(QtCore.QRect(159, 80, 124, 24))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 B")
        font.setPointSize(10)
        self.graphic_show.setFont(font)
        self.graphic_show.setObjectName("graphic_show")
        self.graphic_show.setEnabled(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #tray로 숨기기에 이용
        icon = QtGui.QIcon("resource/image/icon.png")
        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setVisible(False)
        self.menu = QtWidgets.QMenu()
        self.quit = QtWidgets.QAction("측정종료")
        self.menu.addAction(self.quit)
        self.tray.setContextMenu(self.menu)
        self.quit.triggered.connect(self.tray_close)

        #그래프 나타내기에 이용
        self.dialog = QDialog()
        self.dialog.setWindowTitle('BlinkCount Graph')
        self.dialog.resize(643, 483)
        self.dialog_graphic = QtWidgets.QLabel(self.dialog)
        self.dialog_graphic.setGeometry(3, 3, 643, 483)
        self.dialog_graphic.setText("")
        self.dialog_graphic.setObjectName("dialog_graphic")
        self.dialog_graphic.setPixmap(QtGui.QPixmap("dataset/graph.jpg"))
        self.dialog.move(300,300)

        #현재 상태 나타내기에 이용
        self.dialogCur = QDialog()

        self.start_btn.clicked.connect(self.ready_start)
        self.start_btn.clicked.connect(self.select_g)
        self.start_btn.clicked.connect(self.select_a)
        self.start_btn.clicked.connect(self.db_starter)
        self.start_btn.clicked.connect(self.gp_starter)
        self.start_btn.clicked.connect(self.gp_updater)
                                            #수정함
        self.start_btn.clicked.connect(self.dialogCur_open)
        self.start_btn.clicked.connect(self.d_su_starter)

        self.graphic_show.clicked.connect(lambda: self.show_graphic(MainWindow))

    def ready_start(self):
        countBlink.exit_condition = False
        time.sleep(0.1)

    def show_graphic(self, MainWindow):
        self.dialog.show()

    #레이아웃 조정 필요 
    def dialogCur_open(self):
        self.hide()
        self.dialogCur.setWindowTitle('Current Eye status')
        self.dialogCur.setWindowModality(Qt.ApplicationModal)
        self.dialogCur.resize(140, 83)

        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()
        widget = self.dialogCur.geometry()
        x = ag.width() - widget.width()
        y = 2 * ag.height() - sg.height() - widget.height()
        self.dialogCur.move(x, y)

        self.labDialog = QtWidgets.QLabel(self.dialogCur)
        self.labDialog.setGeometry(0, 0, 140, 83)
        self.labDialog.setText("")
        self.labDialog.setObjectName("labDialog")
        self.labDialog.setAlignment(QtCore.Qt.AlignCenter)
        
        self.dialogCur.show()

    def dialogCur_status_update(self):
        while(not countBlink.exit_condition):
            time.sleep(10)
            self.bright_contrl()
            cnt_blink = countBlink.cnt_blink
            if (self.gender.currentText() == "남성" or self.age.currentText() == "청소년"):
                if(cnt_blink <=1):
                    if self.sound_alarm.isChecked():
                        winsound.Beep(493, 200)
                    self.labDialog.setPixmap(QtGui.QPixmap("resource/image/bad.jpg"))
                elif(1 < cnt_blink <=3):
                    self.labDialog.setPixmap(QtGui.QPixmap("resource/image/soso.jpg"))
                elif(cnt_blink >3):
                    self.labDialog.setPixmap(QtGui.QPixmap("resource/image/good.jpg"))
            else:
                if(cnt_blink <=2):
                    if self.sound_alarm.isChecked():
                        winsound.Beep(493, 200)
                    self.labDialog.setPixmap(QtGui.QPixmap("resource/image/bad.jpg"))
                elif(2 < cnt_blink <=5):
                    self.labDialog.setPixmap(QtGui.QPixmap("resource/image/soso.jpg"))
                elif(cnt_blink >5):
                    self.labDialog.setPixmap(QtGui.QPixmap("resource/image/good.jpg"))

    def bright_contrl(self):
        if self.brightness_check.isChecked():
            bright.update_bright(path = "dataset/count_blink.csv")
        else:
            pass   
    def tray_open(self):
        self.hide()
        self.tray.setVisible(True)

    def tray_close(self):
        countBlink.exit_condition = True
        Thread2.vid.stopVideo()
        self.tray.setVisible(False)
        self.show()

    def d_su_starter(self):
        d_x = Thread(target = self.dialogCur_status_update, args=())
        d_x.start()
    def db_starter(self):
        x = Thread1(self)
        x.start()
    def gp_starter(self):
        z = Thread2(self)
        z.start()
    def gp_updater(self):
        w = Thread(target = self.update_gp, args=())
        w.start()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EyeProtector"))
        self.gender.setItemText(0, _translate("MainWindow", "여성"))
        self.gender.setItemText(1, _translate("MainWindow", "남성"))
        self.age.setItemText(0, _translate("MainWindow", "청소년"))
        self.age.setItemText(1, _translate("MainWindow", "성인"))
        self.start_btn.setText(_translate("MainWindow", "측정 시작"))
        self.brightness_check.setText(_translate("MainWindow", "화면 밝기 자동 조정"))
    
    def select_g(self):
        global gender
        gender=self.gender.currentText()
        print(self.gender.currentText())
    
    def select_a(self):
        global age
        age=self.age.currentText()
        print(self.age.currentText())

    def update_gp(self):
        while(not countBlink.exit_condition):
            time.sleep(10)
            self.dialog_graphic.setPixmap(QtGui.QPixmap("dataset/graph.jpg"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
