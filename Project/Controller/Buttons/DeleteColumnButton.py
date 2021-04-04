from Project.Controller.Actions import CSVFileUploadAction

def deleteColumnButton(mainWindow, tableWindow, qtw):
    mainWindow.DeleteColumnButton = qtw.QAction('Delete column', mainWindow, checkable=False)
    mainWindow.DeleteColumnButton.setEnabled(False)
    mainWindow.DeleteColumnButton.triggered.connect(lambda: test(tableWindow))

def test(tableWindow):
    print("row: " + str(tableWindow.table.selectionModel().selectedRows()))