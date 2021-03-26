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
        print(self.data)
        for key in self.data.keys():
            if not key in newData.keys():
                self.data[key].append("")
        print(self.data)

        # auto update table view after updating backend
        self.tableView.populateTable()

    def getData(self):
        return self.data

    def addTableView(self, tableView):
        self.tableView = tableView

    def setRunningFlag(self, isRunning):
        self.isRunning = isRunning

    def autosave(self):
        while self.isRunning:
            time.sleep(5)
            self.data = self.tableView.getDataInTable()
            #write the data to the LastSession.json file
            with open("LastSession/LastSession.json", "w") as file:
                json.dump(self.data, file, indent=4, separators=(',', ': '))
            print("Performed autosave")
