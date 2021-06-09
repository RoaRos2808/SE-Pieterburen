def uponActionPerformed(tableWindow):
    deleteColumn(tableWindow)

def deleteColumn(tableWindow):
    indexes = tableWindow.table.selectionModel().selectedColumns()
    for index in sorted(indexes):
        idx = index.column()
    tableWindow.table.removeColumn(idx)
    del tableWindow.columnHeaders[idx]
    #if indexes is not empty, a deletion has taken place, so refresh backend
    if indexes:
        tableWindow.getBackEnd().refresh()

def deleteColumn_test(tableWindow, idx):
    tableWindow.table.removeColumn(idx)
    del tableWindow.columnHeaders[idx]
    tableWindow.getBackEnd().refresh()
