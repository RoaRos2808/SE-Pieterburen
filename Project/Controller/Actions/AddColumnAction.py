import PyQt5.QtCore as qtc

def uponActionPerformed(tableWindow, qtw):
    addColumn(tableWindow, qtw)

def addColumn(tableWindow, qtw):
    dialogColumnName = qtw.QInputDialog()
    dialogColumnName.setStyleSheet("QDialog {background-color:none}")
    columnName, ok = dialogColumnName.getText(tableWindow, "Enter column name", "Enter a column header:")
    if ok:
        tableWindow.columnHeaders.append(columnName)
        columnCount = tableWindow.table.columnCount()
        rowCount = tableWindow.table.rowCount()
        tableWindow.table.insertColumn(columnCount)
        tableWindow.table.setHorizontalHeaderLabels(tableWindow.columnHeaders)