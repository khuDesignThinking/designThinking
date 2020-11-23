# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(738, 930)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(640, 480))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(300, 300))
        self.label.setLineWidth(0)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget_5)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_5)
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/image/change.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 1, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.widget_5)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.start_btn = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())
        self.start_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(12)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")
        self.gridLayout_3.addWidget(self.start_btn, 0, 0, 1, 1)
        self.stop_btn = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_btn.sizePolicy().hasHeightForWidth())
        self.stop_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(12)
        self.stop_btn.setFont(font)
        self.stop_btn.setObjectName("stop_btn")
        self.gridLayout_3.addWidget(self.stop_btn, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_3, 0, 1, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("배달의민족 도현")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("배달의민족 도현")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setMinimumSize(QtCore.QSize(170, 59))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3.setPixmap(QtGui.QPixmap("resource\\image\\Soso.png"))
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setMinimumSize(QtCore.QSize(170, 59))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.widget_4, 1, 0, 1, 2)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gender = QtWidgets.QComboBox(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(10)
        self.gender.setFont(font)
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gridLayout_2.addWidget(self.gender, 0, 0, 1, 1)
        self.age = QtWidgets.QComboBox(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
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
        self.gridLayout_2.addWidget(self.age, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget, 0, 2, 4, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_2.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resource/image/dropdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_5.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget_5)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_3.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resource/image/dropup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_5.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.gridLayout_6.addWidget(self.widget_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/profile.png\"/></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "사진을 변경하려면 다음 버튼을 누르십시오."))
        self.label_8.setText(_translate("MainWindow", "그래프를 안 보이게 하려면 다음 버튼을 누르십시오."))
        self.start_btn.setText(_translate("MainWindow", "측정 시작"))
        self.stop_btn.setText(_translate("MainWindow", "측정 중지"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">현재 상태</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">현재 상태</p></body></html>"))
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
        self.label_9.setText(_translate("MainWindow", "그래프를 보이게 하려면 다음 버튼을 누르십시오."))
        self.pushButton.clicked.connect(self.change_profile)
        self.start_btn.clicked.connect(self.select_g)
        self.start_btn.clicked.connect(self.select_a)
        self.start_btn.clicked.connect(self.db_starter)
        self.start_btn.clicked.connect(self.us_starter)
        self.start_btn.clicked.connect(self.gp_starter)
        self.start_btn.clicked.connect(self.gp_updater)

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
        while(True):
            time.sleep(10)
            cnt_blink = thread.cnt_blink
            if(cnt_blink <=1):
              self.label_3.setPixmap(QtGui.QPixmap("resource\\image\\red.png"))
            elif(1 < cnt_blink <=3):
              self.label_3.setPixmap(QtGui.QPixmap("resource\\image\\yellow.png"))
            elif(cnt_blink >3):
              self.label_3.setPixmap(QtGui.QPixmap("resource\\image\\green.png"))
    def update_gp(self):
        while(True):
            time.sleep(10)
            self.graphicsView.setPixmap(QtGui.QPixmap("dataset/graph.jpg"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())