import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import Project.img.resources


class SplashScreen(qtw.QSplashScreen):
    def __init__(self, app):
        picture = qtg.QPixmap(':/Brian_Zeehond_Border.png')
        super().__init__(picture, qtc.Qt.WindowStaysOnTopHint)
        self.setMask(picture.mask())
        self.app = app

    def showSplashScreen(self):
        self.show()
        self.app.processEvents()
        qtc.QTimer.singleShot(3000, self.close)