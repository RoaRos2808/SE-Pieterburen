from Project.Controller.Actions import DeleteColumnAction

def deleteColumnButton(mainWindow, tableWindow, qtw):
    mainWindow.DeleteColumnButton = qtw.QAction('Delete column', mainWindow, checkable=False)
    mainWindow.DeleteColumnButton.setShortcut('Ctrl+c')
    mainWindow.DeleteColumnButton.setEnabled(False)
    mainWindow.DeleteColumnButton.triggered.connect(lambda: DeleteColumnAction.uponActionPerformed(tableWindow))

def test(tableWindow):
    tableWindow.table.removeColumn(3)

