import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from PyQt5.QtCore import pyqtSlot
import pandas as pd


class TableView(qtw.QFrame):
    def __init__(self, parent, backEnd):
        super().__init__(parent)
        self.parent = parent
        self.setLayout(qtw.QGridLayout())
        self.setStyleSheet("TableView{ background-color:lightblue}")
        #self.setStyleSheet("background-color: #053045;")
        self.layout().setContentsMargins(20, 20, 20, 20)
        self.makeTable()

        self.columnHeaders = []
        self.backEnd = backEnd
        self.populateTable()

    def makeTable(self):
        self.table = qtw.QTableWidget(self)
        #self.activateItemChangedSignal()
        self.table.horizontalHeader().setDefaultSectionSize(150)
        self.table.horizontalHeader().setStyleSheet("QHeaderView {font-size: 9pt;}")
        self.table.verticalHeader().setStyleSheet("QHeaderView {font-size: 9pt;}")

        self.table.verticalHeader().selectionModel().selectionChanged.connect(lambda: self.activateDeleteRowButton())
        self.table.horizontalHeader().selectionModel().selectionChanged.connect(
            lambda: self.activateDeleteColumnButton())
        self.table.setStyleSheet("QFrame{ background-color:white}"
                                 "QScrollBar{ background-color: none } ")
        # self.table.resizeColumnsToContents()
        self.layout().addWidget(self.table, 1, 0, 1, 1)

    # This function takes the table data in the form of a dictionary.
    # Keys act as column headers, the values are lists of strings which populate all rows under that column
    def populateTable(self):
        item = self.layout().takeAt(0)
        item.widget().deleteLater()
        self.makeTable()

        self.columnHeaders.clear()
        #self.table.clear()
        tableData = self.backEnd.getData()
        for col in tableData.columns:
            self.columnHeaders.append(col)
        columnCount = len(tableData.columns)
        rowCount = tableData.shape[0]

        self.table.setRowCount(rowCount)
        self.table.setColumnCount(columnCount)

        increment = 0
        for columnIndex, column in enumerate(tableData.keys()):
            for rowIndex in range(rowCount):
                increment += 1
                cellValue = tableData[column][rowIndex]
                cell = qtw.QTableWidgetItem(str(cellValue))
                #print(cellValue)
                # The following lines makes values for first two columns read only: we have to discuss this choice.
                # Should the user be allowed to change the file name value and health score value?
                # Removed for now, based on advice of client
                #if columnIndex == 0 or columnIndex == 1:
                #    cell.setFlags(qtc.Qt.ItemIsSelectable | qtc.Qt.ItemIsEnabled)

                #item = self.table.itemAt(rowIndex, columnIndex)
                #self.table.removeItemWidget(item)
                self.table.setItem(rowIndex, columnIndex, cell)

        self.table.setHorizontalHeaderLabels(self.columnHeaders)
        self.table.show()
        self.activateItemChangedSignal()

    # function returns a dictionary with the data currently in table
    def getDataInTable(self):
        numberRows = self.table.rowCount()
        data = pd.DataFrame(columns=self.columnHeaders)

        for columnIndex, header in enumerate(self.columnHeaders):
            for rowIndex in range(numberRows):
                cell = self.table.item(rowIndex, columnIndex)
                if cell is not None:
                    value = cell.text()
                    if value is not None:
                        # print("row: " + str(rowIndex) + ", column: " + str(columnIndex) + ", value: " + value)
                        data.loc[rowIndex, header] = cell.text()
                    else:
                        # if a cell has no text (so not even an empty string), we add empty string to data
                        data.loc[rowIndex, header] = ""
                else:
                    # if due to concurrency issues, the cell is not yet made, we add an empty string
                    data.loc[rowIndex, header] = ""
        #print(data)
        return data

    def getBackEnd(self):
        return self.backEnd

    def activateDeleteRowButton(self):
        if len(self.table.selectionModel().selectedRows()) == 0:
            self.parent.activateDeleteRowButton(False)
        else:
            self.parent.activateDeleteRowButton(True)

    def activateDeleteColumnButton(self):
        if len(self.table.selectionModel().selectedColumns()) == 0:
            self.parent.activateDeleteColumnButton(False)
        else:
            self.parent.activateDeleteColumnButton(True)

    def activateItemChangedSignal(self):
        self.table.itemChanged.connect(lambda: self.backEnd.refresh())

    def getColumns(self):
        #print("hello2")
        #print(self.columnHeaders)
        return self.columnHeaders
