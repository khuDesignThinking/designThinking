"""
dev : 김희성
date : 2020/11/12
This module show graph.jpg every 10second
dependency : draw_graph.py, 
Next thing I have to do is connect with main thread
"""
import cv2
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
import draw_graph as dg


class ShowVideo(QtCore.QObject):
    image_directory = "dataset/graph.jpg"
    dg.update_graph(image_directory)

    image = cv2.imread(image_directory, cv2.IMREAD_COLOR)

    height, width = image.shape[:2] # 사진의 픽셀을 확인함.

    VideoSignal1 = QtCore.pyqtSignal(QtGui.QImage)

    run_program = True

    def __init__(self, parent=None):
        super(ShowVideo, self).__init__(parent)

    def stopVideo(self):
        self.run_program = False
        return None

    @QtCore.pyqtSlot()
    def startVideo(self):
        self.run_program = True
        while self.run_program:
            dg.update_graph()
            image = cv2.imread(self.image_directory, cv2.IMREAD_COLOR)
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            qt_image1 = QtGui.QImage(color_swapped_image.data, # ndarray data attribute 버퍼객체의 시작을 가르킨다는데 잘 모르겠음.
                                    self.width,
                                    self.height,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)
            self.VideoSignal1.emit(qt_image1)
            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(1000, loop.quit) # every 10,000ms 10s update image
            loop.exec_()
    

class ImageViewer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.image = QtGui.QImage()
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)
        self.initUI()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()

    def initUI(self):
        pass
        # self.setWindowTitle('DESIGN THINKING PROJ')
        # self.setWindowIcon(QIcon('./resource/images/networking.png'))
        # self.move(300,300)
        # self.resize(300,600)
    
    @QtCore.pyqtSlot(QtGui.QImage)
    def setImage(self, image):
        if image.isNull():
            print("Viewer Dropped frame!")

        self.image = image
        if image.size() != self.size():
            self.setFixedSize(image.size())
        self.update()


def check_sourcefile():
    pass