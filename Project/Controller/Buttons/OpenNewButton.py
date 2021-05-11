from Project.Controller.Actions import OpenNewAction


def openNewButton(mainWindow, qtw):
    mainWindow.OpenNewButton = qtw.QAction('New', mainWindow, checkable=False)
    mainWindow.OpenNewButton.triggered.connect(lambda: OpenNewAction.uponActionPerformed(mainWindow, qtw))