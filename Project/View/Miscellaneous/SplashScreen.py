import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc


class SplashScreen(qtw.QSplashScreen):
    def __init__(self, app):
        picture = qtg.QPixmap('../Project/img/seal.jpg')
        super().__init__(picture, qtc.Qt.WindowStaysOnTopHint)
        self.setMask(picture.mask())
        self.app = app

    def showSplashScreen(self):
        self.show()
        self.app.processEvents()
        qtc.QTimer.singleShot(1000, self.close)