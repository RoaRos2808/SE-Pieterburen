from Project.Controller.Actions import FileUploadAction

def fileUploadButton(mainWindow, qtw):
    mainWindow.FileUploadButton = qtw.QAction('Upload sound file(s)', mainWindow, checkable=False)
    mainWindow.FileUploadButton.setShortcut('Ctrl+u')
    mainWindow.FileUploadButton.triggered.connect(lambda: FileUploadAction.uponActionPerformed(mainWindow, qtw))