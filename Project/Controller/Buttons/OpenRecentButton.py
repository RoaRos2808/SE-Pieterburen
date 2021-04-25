from Project.Controller.Actions import OpenRecentAction


def openRecentButton(mainWindow, qtw):
    mainWindow.OpenRecentButton = qtw.QAction('Open Recent', mainWindow, checkable=False)
    mainWindow.OpenRecentButton.triggered.connect(lambda: OpenRecentAction.uponActionPerformed(mainWindow, qtw))