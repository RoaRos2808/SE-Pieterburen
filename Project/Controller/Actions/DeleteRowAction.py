def uponActionPerformed(tableWindow):
        deleteRow(tableWindow)

def deleteRow(tableWindow):
        indexes = tableWindow.table.selectionModel().selectedRows()
        for index in sorted(indexes):
                #print(index.row())
                tableWindow.table.removeRow(index.row())
        # if indexes is not empty, a deletion has taken place, so refresh backend
        if indexes:
                tableWindow.getBackEnd().refresh()
