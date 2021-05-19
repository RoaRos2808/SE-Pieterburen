from Project.Controller.Actions import DeleteRowAction


def deleteRowButton(mainWindow, tableWindow, qtw):
    mainWindow.DeleteRowButton = qtw.QAction('Delete row', mainWindow, checkable=False)
    mainWindow.DeleteRowButton.setShortcut('Ctrl+r')
    mainWindow.DeleteRowButton.setEnabled(False)
    mainWindow.DeleteRowButton.triggered.connect(lambda: DeleteRowAction.uponActionPerformed(tableWindow))
