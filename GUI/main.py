import PyQt5.QtWidgets as qtw
import ViewHandler as vh

app = qtw.QApplication([])
#get screen resolution of system used
screenResolution = app.desktop().screenGeometry()
#fractions of the screen dimensions to use as dimensions for app
windowHeightToScreen, windowWidthToScreen = 0.8, 0.6
width, height = int(screenResolution.width()*windowWidthToScreen), int(screenResolution.height()*windowHeightToScreen)
mw = vh.MainWindow(width, height)
app.exec_()