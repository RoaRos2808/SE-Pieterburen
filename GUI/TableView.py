import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

class TableView(qtw.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setLayout(qtw.QGridLayout())
        self.setStyleSheet("background-color:lightblue")
        self.layout().setContentsMargins(20,20,20,20)
        self.table = qtw.QTableWidget(self)

        self.columnHeaders = []
        self.tableData = self.createTableData()
        self.populateTable(self.tableData)


        self.table.setStyleSheet("background-color:white")

        self.layout().addWidget(self.table,1,0,1,1)

    def addColumn(self):
        dialogColumnName = qtw.QInputDialog()
        dialogColumnName.setStyleSheet("color:white")
        columnName, ok = dialogColumnName.getText(self, "Enter column name", "Enter a column header:")
        if ok:
            self.columnHeaders.append(columnName)
            columnCount = self.table.columnCount()
            self.table.insertColumn(columnCount)
            print(self.columnHeaders)
            self.table.setHorizontalHeaderLabels(self.columnHeaders)

    def createTableData(self):
        data = {"File Name": ["12345.wav", "22345.wav", "54321.wav", "77890.wav"],
         "Health Score": ["2", "3", "1", "2"],
         "Notes": ["", "", "", ""]}
        return data

    #This function takes the table data in the form of a dictionary.
    #Keys act as column headers, the values are lists of strings which populate all rows under that column
    def populateTable(self, tableData):
        columnCount = len(tableData.keys())
        if columnCount != 0:
            rowCount = len(tableData[list(tableData.keys())[0]])

        self.table.setRowCount(rowCount)
        self.table.setColumnCount(columnCount)

        for key in tableData:
            self.columnHeaders.append(key)

        for columnIndex, column in enumerate(tableData.keys()):
            for rowIndex in range(rowCount):
                cellValue = tableData[column][rowIndex]
                cell = qtw.QTableWidgetItem(cellValue)
                #The following lines makes values for first two columns read only: we have to discuss this choice.
                #Should the user be allowed to change the file name value and health score value?
                if columnIndex == 0 or columnIndex == 1:
                    cell.setFlags(qtc.Qt.ItemIsSelectable | qtc.Qt.ItemIsEnabled)

                self.table.setItem(rowIndex, columnIndex, cell)

        self.table.setHorizontalHeaderLabels(self.columnHeaders)
        self.table.show()