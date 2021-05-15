from Project.Controller.Actions import OpenRecentAction
import PyQt5.QtWidgets as qtw
import os

def openRecentMenu(mainWindow, qtw):
    mainWindow.OpenRecentMenu = qtw.QMenu("Open Recent")
    mainWindow.OpenRecentMenu.addAction("Something")

def update(mainWindow, qtw):
    print("hi")
    for file in mainWindow.recentFiles:
        mainWindow.OpenRecentMenu.addAction(os.path.basename(file))
    # mainWindow.OpenRecentMenu.triggered.connect(lambda: print(mainWindow.recentFiles))
