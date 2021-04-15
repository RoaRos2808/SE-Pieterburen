import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from PyQt5.QtCore import pyqtSlot


class TableView(qtw.QFrame):
    def __init__(self, parent, backEnd):
        super().__init__(parent)
        self.parent = parent
        self.setLayout(qtw.QGridLayout())
        self.setStyleSheet("background-color:lightblue")
        self.layout().setContentsMargins(20, 20, 20, 20)
        self.table = qtw.QTableWidget(self)

        # self.table.verticalHeader().sectionClicked.connect(lambda: print("hoi"))
        self.table.verticalHeader().selectionModel().selectionChanged.connect(lambda: self.activateDeleteRowButton())
        self.table.horizontalHeader().selectionModel().selectionChanged.connect(
            lambda: self.activateDeleteColumnButton())

        self.columnHeaders = []
        self.backEnd = backEnd
        self.populateTable()

        self.table.setStyleSheet("background-color:white")

        self.layout().addWidget(self.table, 1, 0, 1, 1)

    # This function takes the table data in the form of a dictionary.
    # Keys act as column headers, the values are lists of strings which populate all rows under that column
    def populateTable(self):
        tableData = self.backEnd.getData()
        self.columnHeaders = []
        columnCount = len(tableData.keys())
        if columnCount != 0:
            rowCount = len(tableData[list(tableData.keys())[0]])

        self.table.setRowCount(rowCount)
        self.table.setColumnCount(columnCount)

        for key in tableData:
            self.columnHeaders.append(key)

        for columnIndex, column in enumerate(tableData.keys()):
            for rowIndex in range(rowCount):
                # print(str(rowIndex))
                cellValue = tableData[column][rowIndex]
                cell = qtw.QTableWidgetItem(cellValue)
                # The following lines makes values for first two columns read only: we have to discuss this choice.
                # Should the user be allowed to change the file name value and health score value?
                if columnIndex == 0 or columnIndex == 1:
                    cell.setFlags(qtc.Qt.ItemIsSelectable | qtc.Qt.ItemIsEnabled)

                self.table.setItem(rowIndex, columnIndex, cell)

        self.table.setHorizontalHeaderLabels(self.columnHeaders)
        self.table.show()

    # function returns a dictionary with the data currently in table
    def getDataInTable(self):
        numberRows = self.table.rowCount()
        data = {}
        for columnIndex, header in enumerate(self.columnHeaders):
            rowValues = []
            for rowIndex in range(numberRows):
                cell = self.table.item(rowIndex, columnIndex)
                if cell is not None:
                    value = cell.text()
                    if value is not None:
                        # print("row: " + str(rowIndex) + ", column: " + str(columnIndex) + ", value: " + value)
                        rowValues.append(cell.text())
                    else:
                        # if a cell has no text (so not even an empty string), we add empty string to data
                        rowValues.append("")
                else:
                    # if due to concurrency issues, the cell is not yet made, we add an empty string
                    rowValues.append("")
            data.update({header: rowValues})
        return data

    def getBackEnd(self):
        print("hello")
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
