from Project.Controller.Actions import OpenAction


def openButton(mainWindow, qtw):
    mainWindow.OpenButton = qtw.QAction('Open', mainWindow, checkable=False)
    mainWindow.OpenButton.triggered.connect(lambda: OpenAction.CSVUpload(mainWindow, qtw))