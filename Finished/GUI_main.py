from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
import countBlink
import time
import csv
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
        MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        img = QImage("resource/image/backgroundColor.jpg")
        palette = QPalette()
        palette.setBrush(10,QBrush(img))
        MainWindow.setPalette(palette)

        self.gender = QtWidgets.QComboBox(self.centralwidget)
        self.gender.setGeometry(QtCore.QRect(19, 19, 134, 20))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 M")
        font.setPointSize(9)
        self.gender.setFont(font)
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.setStyleSheet("background-color: rgb(255,255,255);font: bold 14px;")

        self.age = QtWidgets.QComboBox(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(19, 45, 134, 20))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 M")
        font.setPointSize(9)
        self.age.setFont(font)
        self.age.setObjectName("age")
        self.age.addItem("")
        self.age.addItem("")
        self.age.setStyleSheet("background-color: rgb(255,255,255);font: bold 14px;")

        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(159, 19, 133, 20))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 B")
        font.setPointSize(12)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")
        self.start_btn.setStyleSheet("background-color: rgb(255,255,255); border-style: outset;    border-width: 2px;    border-radius: 7px;    font: bold 14px;")

        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(159, 45, 133, 20))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 B")
        font.setPointSize(12)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("start_btn")
        self.exit_btn.setStyleSheet("background-color: rgb(255,255,255); border-style: outset;    border-width: 2px;    border-radius: 7px;    font: bold 14px;")

        self.brightness_check = QtWidgets.QCheckBox(self.centralwidget)
        self.brightness_check.setGeometry(QtCore.QRect(20, 84, 125, 16))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 B")
        font.setPointSize(9)
        self.brightness_check.setFont(font)
        self.brightness_check.setObjectName("brightness_check")
        self.brightness_check.setStyleSheet("font : bold 14px")
        
        self.sound_alarm = QtWidgets.QCheckBox("음성 알림", self.centralwidget)
        self.sound_alarm.setGeometry(QtCore.QRect(20, 114, 125, 16))
        self.sound_alarm.setFont(font)
        self.sound_alarm.setObjectName("sound_alarm")
        self.sound_alarm.setStyleSheet("font : bold 14px")

        #눈건강 메뉴얼 
        self.manual = QtWidgets.QPushButton("눈건강 info", self.centralwidget)
        self.manual.setGeometry(QtCore.QRect(159, 110, 133, 24))
        font.setPointSize(9)
        self.manual.setFont(font)
        self.manual.setObjectName("manual")
        self.manual.setStyleSheet("background-color: rgb(180,197,222); border-style: outset;    border-width: 2px;    border-radius: 7px;    font: bold 14px;")

        self.graphic_show = QtWidgets.QPushButton("그래프 나타내기", self.centralwidget)
        self.graphic_show.setGeometry(QtCore.QRect(159, 80, 133, 24))
        font = QtGui.QFont()
        font.setFamily("한컴 백제 B")
        font.setPointSize(9)
        self.graphic_show.setFont(font)
        self.graphic_show.setObjectName("graphic_show")
        self.graphic_show.setEnabled(True)
        self.graphic_show.setStyleSheet("background-color: rgb(219,214,239); border-style: outset;    border-width: 2px;    border-radius: 7px;    font: bold 14px;")        
        
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

        #눈건강 info에 이용
        self.dialog2 = QDialog()

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
        self.dialogCur.setWindowTitle('Current Eye status')
        self.dialogCur.resize(140, 83)
        self.dialogCur.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.labDialog = QtWidgets.QLabel(self.dialogCur)
        self.labDialog.setGeometry(0, 0, 140, 83)
        self.labDialog.setText("")
        self.labDialog.setObjectName("labDialog")
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()
        widget = self.dialogCur.geometry()
        x = ag.width() - widget.width()
        y = 2 * ag.height() - sg.height() - widget.height()
        self.dialogCur.move(x, y)

        self.timer = QTimer()
        self.timer.timeout.connect(self.dia_open)

        self.start_btn.clicked.connect(self.ready_start)
        self.start_btn.clicked.connect(self.select_g)
        self.start_btn.clicked.connect(self.select_a)
        # 순서 
        # 1. countBlink에서 계속 카운트 기록 
        # 2. dialogCurstatusUpdate에서 10초 단위로 cnt_blink 초기화 & 파일 추가
        # 3. draw_graph에서 2단계에서 저장한 파일 불러와 그래프 그리고 업데이트 
        self.start_btn.clicked.connect(self.db_starter) # 1
        self.start_btn.clicked.connect(self.d_su_starter) # 2
        self.start_btn.clicked.connect(self.gp_starter) # 3
        self.start_btn.clicked.connect(self.gp_updater)# 3

        self.start_btn.clicked.connect(self.start_timer)
        self.start_btn.clicked.connect(self.tray_open)

        self.graphic_show.clicked.connect(lambda: self.show_graphic(MainWindow))
        self.manual.clicked.connect(self.dialogInfo_open)
        self.exit_btn.clicked.connect(self.exit)
    
    def exit(self):
        exit(100)

    def ready_start(self):
        countBlink.exit_condition = False
        time.sleep(0.1)

    def start_timer(self):
        self.timer.start(10000)

    def show_graphic(self, MainWindow):
        self.dialog.show()

    def dia_open(self):
        self.dialogCur.show()
        QtCore.QTimer.singleShot(1500, self.dia_close)

    def dia_close(self):
        self.dialogCur.hide()

    def dialogCur_status_update__fileAdd(self):
        cnt_blink_list = []
        while(not countBlink.exit_condition):
            countBlink.cnt_blink = 0
            time.sleep(10)
            cnt_blink = countBlink.cnt_blink
            print("10 sec past  ||  current countBlink : ", cnt_blink)
            # fileAdd
            cnt_blink_list.append(cnt_blink)
            file_name = "dataset/count_blink.csv"
            with open(file_name, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows([cnt_blink_list])
            # status_update
            self.bright_contrl()
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
        self.timer.stop()
        self.show()
    
    def d_su_starter(self):
        d_x = Thread(target = self.dialogCur_status_update__fileAdd, args=())
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
        self.exit_btn.setText(_translate("MainWindow", "프로그램 종료"))
        self.brightness_check.setText(_translate("MainWindow", "화면 밝기 조정"))
    
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
    
    def dialogInfo_open(self):
        #self.hide()
        self.dialog2.setObjectName("Dialog2")
        self.dialog2.resize(698, 529)
        self.dialog2.setWindowTitle("눈건강 INFO")
        self.tabWidget = QtWidgets.QTabWidget(self.dialog2)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 681, 511))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget(self.dialog2)
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 10, 661, 471))
        self.widget.setObjectName("widget")
        self.tabWidget.addTab(self.tab, "눈 건강의 중요성")

        self.tab_2 = QtWidgets.QWidget(self.dialog2)
        self.tab_2.setObjectName("tab")
        self.widget_2 = QtWidgets.QWidget(self.tab_2)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 661, 471))
        self.widget_2.setObjectName("widget_2")
        self.tabWidget.addTab(self.tab_2, "눈 운동방법")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget_3 = QtWidgets.QWidget(self.tab_3)
        self.widget_3.setGeometry(QtCore.QRect(10, 10, 661, 471))
        self.widget_3.setObjectName("widget")
        self.tabWidget.addTab(self.tab_3, "눈건강을 위한 생활 수칙")
        ### 더 추가 하고 싶은 부분은 이만큼 복붙해서 이름 바꾸면 됩니다.
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.widget_4=QtWidgets.QWidget(self.tab_4)
        self.widget_4.setGeometry(QtCore.QRect(10, 10, 661, 471))
        self.widget_4.setObjectName("widget_4")
        self.tabWidget.addTab(self.tab_4, "눈에 좋은 음식과 해로운 음식")
        ###
        self.tabweb_1=QWebEngineView(self.widget)
        profile = QWebEngineProfile(self.tabweb_1)
        profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
        page = QWebEnginePage(profile, self.tabweb_1)
        self.tabweb_1.setPage(page)
        self.tabweb_1.setUrl(QUrl("https://blog.yonseibon.co.kr/life/%EA%B7%B8%EB%8F%99%EC%95%88-%EB%AA%B0%EB%9E%90%EB%8D%98-%EB%88%88-%EA%B1%B4%EA%B0%95%EC%9D%B4-%EC%A4%91%EC%9A%94%ED%95%9C-%EC%9D%B4%EC%9C%A0/")) 
        ###
        self.tabweb_2=QWebEngineView(self.widget_2)
        profile = QWebEngineProfile(self.tabweb_2)
        profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
        page = QWebEnginePage(profile, self.tabweb_2)
        self.tabweb_2.setPage(page)
        self.tabweb_2.setUrl(QUrl("https://steptohealth.co.kr/7-exercise-for-your-eyes/"))
        ###
        self.tabweb_3=QWebEngineView(self.widget_3)
        profile = QWebEngineProfile(self.tabweb_3)
        profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
        page = QWebEnginePage(profile, self.tabweb_3)
        self.tabweb_3.setPage(page)
        self.tabweb_3.setUrl(QUrl("http://www.nrc.go.kr/portal/html/content.do?depth=ph&menu_cd=03_05"))
        ###
        self.tabweb_4=QWebEngineView(self.widget_4)
        profile = QWebEngineProfile(self.tabweb_4)
        profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
        page = QWebEnginePage(profile, self.tabweb_4)
        self.tabweb_4.setPage(page)
        self.tabweb_4.setUrl(QUrl("http://www.samsunghospital.com/upload/health/1438754922163_234165.jpg"))
        ###위에줄에도 추가한 항목 추가
        self.tabweb_1.setGeometry(QtCore.QRect(10, 10, 661, 471))
        self.tabweb_2.setGeometry(QtCore.QRect(10, 10, 661, 471))
        self.tabweb_3.setGeometry(QtCore.QRect(10, 10, 661, 471))
        self.tabweb_4.setGeometry(QtCore.QRect(10, 10, 661, 471))
        ###위에줄에도 추가한 항목 추가
        self.dialog2.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
