from Project.Controller.Actions import AddColumnAction

def addColumnButton(mainWindow, tableWindow, qtw):
    mainWindow.AddColumnButton = qtw.QAction('Add column', mainWindow, checkable=False)
    mainWindow.AddColumnButton.triggered.connect(lambda: AddColumnAction.uponActionPerformed(tableWindow, qtw))
