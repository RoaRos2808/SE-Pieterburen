import PyQt5.QtCore as qtc

def uponActionPerformed(tableWindow, qtw):
    addColumn(tableWindow, qtw)

def isIn(columnName, list):
    for name in list:
        if columnName == name:
            return True

def checkColumns(columnName, list):
    names = list
    cnt = 1
    if columnName in list:
        while isIn((columnName + "." + str(cnt)), names):
            cnt += 1
        columnName = columnName + "." + str(cnt)

    return columnName


def addColumn(tableWindow, qtw):
    dialogColumnName = qtw.QInputDialog()
    dialogColumnName.setStyleSheet("QDialog {background-color:none}")
    columnName, ok = dialogColumnName.getText(tableWindow, "Enter column name", "Enter a column header:")
    if ok:
        columnName = columnName.strip()
        #check if the column is unique, else add a number to it.
        headers = tableWindow.getColumns()
        columnName = checkColumns(columnName, headers)

        tableWindow.columnHeaders.append(columnName)
        columnCount = tableWindow.table.columnCount()
        rowCount = tableWindow.table.rowCount()
        tableWindow.table.insertColumn(columnCount)
        tableWindow.table.setHorizontalHeaderLabels(tableWindow.columnHeaders)
        tableWindow.getBackEnd().refresh()