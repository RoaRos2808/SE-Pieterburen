import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

class TableView(qtw.QFrame):
    def __init__(self, parent, backEnd):
        super().__init__(parent)
        self.setLayout(qtw.QGridLayout())
        self.setStyleSheet("background-color:lightblue")
        self.layout().setContentsMargins(20,20,20,20)
        self.table = qtw.QTableWidget(self)

        self.columnHeaders = []
        self.backEnd = backEnd
        self.populateTable()


        self.table.setStyleSheet("background-color:white")

        self.layout().addWidget(self.table,1,0,1,1)

    #This function takes the table data in the form of a dictionary.
    #Keys act as column headers, the values are lists of strings which populate all rows under that column
    def populateTable(self):
        tableData = self.backEnd.getData()
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

    def getBackEnd(self):
        return self.backEnd
