import PyQt5.QtWidgets as qtw
from Project.View.Miscellaneous import SplashScreen
from Project.View.ViewCards import ViewHandler
from Project.Model.BackEnd import BackEnd as be
import threading

runningFlag = True

app = qtw.QApplication([])

splash = SplashScreen.SplashScreen(app)
splash.showSplashScreen()


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

#Thread is not working fully properly yet. When program is closed while writing to session file, can cause problems
thread = threading.Thread(target=backEnd.autosave, daemon=False)
thread.start()

#Running is set in backend to make sure that the thread for autosaving can finish when app is closed
backEnd.setRunningFlag(True)
app.exec_()


#Running flag is checked by autosave thread
backEnd.setRunningFlag(False)

