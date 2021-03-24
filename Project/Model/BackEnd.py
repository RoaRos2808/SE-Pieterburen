class BackEnd:
    def __init__(self):
        self.data = {"File Name": ["12345.wav", "22345.wav", "54321.wav", "77890.wav"],
         "Health Score": ["2", "3", "1", "2"],
         "Notes": ["", "", "", ""]}

    def update(self, newData):
        for key in self.data:
            for newKey in newData:
                if key == newKey:
                    self.data[key].append(newData[newKey])
                else:
                    self.data[key].append("")

        # auto update table view after updating backend
        self.tableView.populateTable()

    def getData(self):
        return self.data

    def addTableView(self, tableView):
        self.tableView = tableView