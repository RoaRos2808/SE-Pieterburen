from Project.Controller.Actions import SaveAction

def saveButton(mainWindow, qtw):
    mainWindow.SaveButton = qtw.QAction('Save', mainWindow, checkable=False)
    mainWindow.SaveButton.setShortcut('Ctrl+s')
    mainWindow.SaveButton.triggered.connect(lambda: SaveAction.uponActionPerformed(mainWindow, qtw))
