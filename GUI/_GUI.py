"""
date : 2020/10/23
copy from https://webnautes.tistory.com/1290
next thing I have to do is combine Grapic_User_interface.py & _GUI.py module
"""
#from IPython.utils import capture
import numpy as np
import cv2
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon

def convert_window_freestyle(name: str) -> None:
    """
    to visualize, make window flexible
    :param
        name: window's name
    :return
        None
    """
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    return None


class ShowVideo(QtCore.QObject):
    camera = cv2.VideoCapture(0)

    ret, image = camera.read()

    height, width = image.shape[:2] # 사진의 픽셀을 확인함.

    VideoSignal1 = QtCore.pyqtSignal(QtGui.QImage)

    run_video = True

    def __init__(self, parent=None):
        super(ShowVideo, self).__init__(parent)

    def stopVideo(self):
        self.run_video = False
        return None

    @QtCore.pyqtSlot()
    def startVideo(self):
        
        self.run_video = True

        self.capture_variable = False # if capture_variable is 1 -> capture and convert to language

        while self.run_video:
            ret, image = self.camera.read()
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            if self.capture_variable == True:
                print("image Captured")
                external_function(image)
            
            qt_image1 = QtGui.QImage(color_swapped_image.data, # ndarray data attribute 버퍼객체의 시작을 가르킨다는데 잘 모르겠음.
                                    self.width,
                                    self.height,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)
            self.VideoSignal1.emit(qt_image1)
            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(90, loop.quit) #90 ms

            self.capture_variable = False
            loop.exec_()
    

    def _senseCapture(self) -> bool:
        """If Capture button is clicked, return True else return False"""
        if self.run_video != True:
            print("You should turn on the video")
        self.capture_variable = True


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
        self.setWindowTitle('DESIGN THINKING PROJECT')
        self.setWindowIcon(QIcon('resource/image/eye.png'))
        self.move(300,300)
        self.resize(500,800)
    
    @QtCore.pyqtSlot(QtGui.QImage)
    def setImage(self, image):
        if image.isNull():
            print("Viewer Dropped frame!")

        self.image = image
        if image.size() != self.size():
            self.setFixedSize(image.size())
        self.update()


def external_function(image: np.ndarray):
    print(image)

def main():
    app = QtWidgets.QApplication(sys.argv)

    thread = QtCore.QThread()
    thread.start()

    vid = ShowVideo()
    vid.moveToThread(thread)

    image_viewer1 = ImageViewer()
    
    vid.VideoSignal1.connect(image_viewer1.setImage)

    push_button1 = QtWidgets.QPushButton('Start Video')
    push_button2 = QtWidgets.QPushButton('Stop Video')
    push_button3 = QtWidgets.QPushButton('Capture')

    push_button1.clicked.connect(vid.startVideo)
    push_button2.clicked.connect(vid.stopVideo)
    push_button3.clicked.connect(vid._senseCapture)

    vertical_layout = QtWidgets.QVBoxLayout()
    horizontal_layout = QtWidgets.QHBoxLayout()
    
    vertical_layout.addLayout(horizontal_layout)
    vertical_layout.addWidget(push_button1)
    vertical_layout.addWidget(push_button2)
    vertical_layout.addWidget(push_button3)
    horizontal_layout.addWidget(image_viewer1)

    layout_widget = QtWidgets.QWidget()
    layout_widget.setLayout(vertical_layout)

    main_window = QtWidgets.QMainWindow()
    main_window.setWindowTitle('DESIGN THINKING PROJECT')
    main_window.setWindowIcon(QIcon('resource/image/eye.png'))
    main_window.move(300,300)
    main_window.resize(500,500)
    main_window.setCentralWidget(layout_widget)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()