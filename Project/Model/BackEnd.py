import json

class BackEnd:
    def __init__(self):
        with open('LastSession/LastSession.json') as json_data:
            data = json.load(json_data)

        self.data = data

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