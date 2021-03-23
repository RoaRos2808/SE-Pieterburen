

def editActionAdd(mainWindow, tableWindow, qtw):
    mainWindow.editActionAdd = qtw.QAction('Add column', mainWindow, checkable=False)
    uponActionPerformed(mainWindow, tableWindow, qtw)
    #editMenu.addAction(self.editActionAdd)

def uponActionPerformed(mainWindow, tableWindow, qtw):
    mainWindow.editActionAdd.triggered.connect(lambda: addColumn(tableWindow, qtw))

def addColumn(tableWindow, qtw):
    dialogColumnName = qtw.QInputDialog()
    dialogColumnName.setStyleSheet("color:white")
    columnName, ok = dialogColumnName.getText(tableWindow, "Enter column name", "Enter a column header:")
    if ok:
        tableWindow.columnHeaders.append(columnName)
        columnCount = tableWindow.table.columnCount()
        tableWindow.table.insertColumn(columnCount)
        print(tableWindow.columnHeaders)
        tableWindow.table.setHorizontalHeaderLabels(tableWindow.columnHeaders)