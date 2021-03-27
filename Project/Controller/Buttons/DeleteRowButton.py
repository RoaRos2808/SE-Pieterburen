from Project.Controller.Actions import AddColumnAction

def deleteRowButton(mainWindow, tableWindow, qtw):
    mainWindow.DeleteRowButton = qtw.QAction('Delete row', mainWindow, checkable=False)
    mainWindow.DeleteRowButton.setEnabled(False)
    mainWindow.DeleteRowButton.triggered.connect(lambda: test(tableWindow))

def test(tableWindow):
    print("row: " + str(tableWindow.table.selectionModel().selectedRows()))