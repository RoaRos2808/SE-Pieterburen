import json
import time
import threading
import pandas as pd

class BackEnd:
    def __init__(self):
        data = pd.read_csv('Model/BackEnd/LastSession.csv')

        self.data = data
        self.isRunning = True
        self._lock = threading.Lock()

        #standard column names (have to discuss this)
        self.standardColumns = ['File Name', 'Left Lung Health', 'Right Lung Health']

    def clear(self):
        for key in self.data:
            self.data[key] = []
            self.tableView.populateTable()

    def update(self, fileName, leftOrRight, result):
        if leftOrRight == 'L':
            df = pd.DataFrame({"File Name": [fileName], "Left Lung Health": [result]})
        else:
            df = pd.DataFrame({"File Name": [fileName], "Right Lung Health": [result]})
        frames = [self.data, df]
        self.data = pd.concat(frames, ignore_index=True)
        self.data = self.data.fillna("")

        # #if current spreadsheet does not contain standard column name, add this
        # for standardColumn in self.standardColumns:
        #     if not standardColumn in self.data.keys():
        #         self.data.update({standardColumn: []})

        #if a column is in spreadsheet and new data, add the row entries
        # for col in self.data.columns:
        #     for newCol in newData.columns:
        #         if col == newCol:
        #             print("columns match")

        # #this accounts for columns that are in spreadsheet but not present in new data, it adds "" as an empty entry
        # for key in self.data.keys():
        #     if not key in newData.keys():
        #         self.data[key].append("")

        # auto update table view after updating backend
        self.tableView.populateTable()

    # function for opening a previously saved table
    def openTable(self, newData):
        self.data = newData
        self.tableView.populateTable()

    def getData(self):
        return self.data

    def addTableView(self, tableView):
        self.tableView = tableView

    def setRunningFlag(self, isRunning):
        self.isRunning = isRunning

    def autosave(self):
        while self.isRunning:
            with self._lock:
                time.sleep(5)
                self.data = self.tableView.getDataInTable()
                self.data.to_csv('Model/BackEnd/LastSession.csv', index=False)
                print("Performed autosave")