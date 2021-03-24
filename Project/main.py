import PyQt5.QtWidgets as qtw
from Project.View import ViewHandler
from Project.Model import BackEnd as be

app = qtw.QApplication([])
#get screen resolution of system used
screenResolution = app.desktop().screenGeometry()
#fractions of the screen dimensions to use as dimensions for app
windowHeightToScreen, windowWidthToScreen = 0.8, 0.6
width, height = int(screenResolution.width()*windowWidthToScreen), int(screenResolution.height()*windowHeightToScreen)

# add backend to tableview and tableview to backend
backEnd = be.BackEnd()
mw = ViewHandler.MainWindow(width, height, backEnd)
tableView = mw.getTableView()
backEnd.addTableView(tableView)

app.exec_()