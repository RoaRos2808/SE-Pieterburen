import os

def openRecentMenu(mainWindow, qtw):
    mainWindow.OpenRecentMenu = qtw.QMenu("Open Recent")
    mainWindow.OpenRecentMenu.addAction("Something")

def update(mainWindow, qtw):
    for file in mainWindow.recentFiles:
        mainWindow.OpenRecentMenu.addAction(os.path.basename(file))
    # mainWindow.OpenRecentMenu.triggered.connect(lambda: print(mainWindow.recentFiles))
