import json
import time
import threading
import pandas as pd

class BackEnd:
    def __init__(self):
        data = pd.read_csv('Model/BackEnd/LastSession.csv')
        #TODO does not work when the file is empty

        self.data = data
        self.data = self.data.fillna("")
        self.isRunning = True
        self._lock = threading.Lock()
        self.recentFiles = self.readRecentFiles()

        #standard column names (have to discuss this)
        self.standardColumns = self.makeEmptyDataFrame()

    def makeEmptyDataFrame(self):
        df = pd.DataFrame(columns=['File Name', 'Type', 'Left Lung Health', 'Right Lung Health'])
        return df

    def clear(self):
        self.data = self.makeEmptyDataFrame()
        self.tableView.populateTable()

    def update(self, type, fileName, leftOrRight, result):
        #when you update, check if the standard column headers are present in data. If not, add them at correct position
        standard = self.standardColumns.keys()
        for i in range(0, len(standard)):
            if not standard[i] in self.data.keys():
                self.data.insert(i, standard[i], "")

        if fileName in self.data["File Name"].tolist():
            #index = self.data[self.data["File Name"] == fileName].index
            index = self.data.index[self.data["File Name"] == fileName]
            if leftOrRight == 'L':
                self.data.loc[index, ["Left Lung Health"]] = result
            else:
                self.data.loc[index, ["Right Lung Health"]] = result
            self.data = self.data.fillna("")
        else:
            if leftOrRight == 'L':
                df = pd.DataFrame({"Type": [type], "File Name": [fileName], "Left Lung Health": [result]})
            else:
                df = pd.DataFrame({"Type": [type], "File Name": [fileName], "Right Lung Health": [result]})
            frames = [self.data, df]
            self.data = pd.concat(frames, ignore_index=True)
            self.data = self.data.fillna("")

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

    def updateRecentFiles(self, filePath):
        self.recentFiles.append(filePath)
        self.recentFiles = self.recentFiles[-4:]

    def getRecentFiles(self):
        return self.recentFiles

    def setRunningFlag(self, isRunning):
        self.isRunning = isRunning

    def autosave(self):
        while self.isRunning:
            with self._lock:
                time.sleep(5)
                self.data = self.tableView.getDataInTable()
                self.data.to_csv('Model/BackEnd/LastSession.csv', index=False)
                print("Performed autosave")

    def writeRecentFiles(self):
        with open('Model/BackEnd/RecentFilesList.txt', 'w') as f:
            for file in self.recentFiles:
                f.write(file + '\n')

    def readRecentFiles(self):
        with open('Model/BackEnd/RecentFilesList.txt', 'r') as f:
            recentFileList = [line.rstrip('\n') for line in f]
        return recentFileList