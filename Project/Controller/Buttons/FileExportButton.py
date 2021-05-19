from Project.Controller.Actions import FileExportAction

def fileExportButton(mainWindow, qtw):
    mainWindow.FileExportButton = qtw.QAction('Save as', mainWindow, checkable=False)
    mainWindow.FileExportButton.setShortcut('Ctrl+Alt+s')
    mainWindow.FileExportButton.triggered.connect(lambda : FileExportAction.uponActionPerformed(mainWindow, qtw))

