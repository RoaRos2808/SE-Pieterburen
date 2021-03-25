import json
import time

class BackEnd:
    def __init__(self):
        with open('LastSession/LastSession.json') as json_data:
            data = json.load(json_data)

        self.data = data
        self.isRunning = True

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

    def setRunningFlag(self, isRunning):
        self.isRunning = isRunning

    def autosave(self):
        while True:
            if self.isRunning is True:
                time.sleep(5)
                data = self.tableView.getDataInTable()
                #write the data to the LastSession.json file
                with open("LastSession/LastSession.json", "w") as file:
                    json.dump(data, file, indent=4, separators=(',', ': '))
                print("Performed autosave")
            else:
                break
