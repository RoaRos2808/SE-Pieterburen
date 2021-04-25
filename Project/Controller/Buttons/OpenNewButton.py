from Project.Controller.Actions import OpenNewAction


def openNewButton(mainWindow, qtw):
    mainWindow.OpenNewButton = qtw.QAction('New Spreadsheet', mainWindow, checkable=False)
    mainWindow.OpenNewButton.triggered.connect(lambda: OpenNewAction.uponActionPerformed(mainWindow, qtw))