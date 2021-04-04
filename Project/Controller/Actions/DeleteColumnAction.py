

def uponActionPerformed(mainWindow, qtw):
    mainWindow.deleteColumn("table")

def deleteColumn(tableWindow, qtw):
    dialogColumnName = qtw.QInputDialog()
    dialogColumnName.setStyleSheet("color:white")
    columnName, ok = dialogColumnName.getText(tableWindow, "Enter column name", "Enter a column header:")
    if ok:
        tableWindow.columnHeaders.append(columnName)
        columnCount = tableWindow.table.columnCount()
        rowCount = tableWindow.table.rowCount()
        tableWindow.table.insertColumn(columnCount)
        print(tableWindow.columnHeaders)
        tableWindow.table.setHorizontalHeaderLabels(tableWindow.columnHeaders)