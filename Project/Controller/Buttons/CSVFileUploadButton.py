from Project.Controller.Actions import CSVFileUploadAction


def csvFileUploadButton(mainWindow, qtw):
    mainWindow.CSVFileUploadButton = qtw.QAction('Upload', mainWindow, checkable=False)
    mainWindow.CSVFileUploadButton.triggered.connect(lambda: CSVFileUploadAction.uponActionPerformed(mainWindow, qtw))