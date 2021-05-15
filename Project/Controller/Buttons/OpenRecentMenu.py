from Project.Controller.Actions import OpenRecentAction


def openRecentMenu(mainWindow, qtw):
    mainWindow.OpenRecentMenu = qtw.QMenu("Open Recent")
    mainWindow.OpenRecentMenu.addAction("Something")
