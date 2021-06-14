import os
import time
import threading
import pandas as pd

class BackEnd:
    def __init__(self):
        if os.stat('../Project/Model/BackEnd/LastSession.csv').st_size == 0:
            data = self.makeEmptyDataFrame()
        else:
            data = pd.read_csv('../Project/Model/BackEnd/LastSession.csv')

        self.data = data
        self.spectogramInfo = {}
        self.recentFiles = self.readRecentFiles()
        self.lastFileName = self.readLastFileName()
        self.data = self.data.fillna("")
        self.isRunning = True
        self._lock = threading.Lock()

        #standard column names (have to discuss this)
        self.standardColumns = self.makeEmptyDataFrame()

    def makeEmptyDataFrame(self):
        df = pd.DataFrame(columns=['File Name', 'Left Lung Whistle', 'Right Lung Whistle', 'Left Lung Rhonchus',
                                   'Right Lung Rhonchus'])
        return df

    def clear(self):
        self.data = self.makeEmptyDataFrame()
        self.spectogramInfo = {}
        self.tableView.populateTable()

    def update(self, fileName, leftOrRight, whistleResult, rhonchusResult):
        #when you update, check if the standard column headers are present in data. If not, add them at correct position
        standard = self.standardColumns.keys()
        for i in range(0, len(standard)):
            if not standard[i] in self.data.keys():
                self.data.insert(i, standard[i], "")

        if fileName in self.data["File Name"].tolist():
            #index = self.data[self.data["File Name"] == fileName].index
            index = self.data.index[self.data["File Name"] == fileName]
            if leftOrRight == 'L':
                self.data.loc[index, ["Left Lung Whistle"]] = whistleResult
                self.data.loc[index, ["Left Lung Rhonchus"]] = rhonchusResult
            else:
                self.data.loc[index, ["Right Lung Whistle"]] = whistleResult
                self.data.loc[index, ["Right Lung Rhonchus"]] = rhonchusResult
        else:
            if leftOrRight == 'L':
                df = pd.DataFrame({"File Name": [fileName], "Left Lung Whistle": [whistleResult],
                                   "Left Lung Rhonchus": [rhonchusResult]})
            else:
                df = pd.DataFrame({"File Name": [fileName], "Right Lung Whistle": [whistleResult],
                                   "Right Lung Rhonchus": [rhonchusResult]})
            frames = [self.data, df]
            self.data = pd.concat(frames, ignore_index=True)
            self.data = self.data.fillna("")

        self.data = self.data.fillna("")

    # function for opening a previously saved table
    def openTable(self, newData):
        self.data = newData
        self.data = self.data.fillna("")
        self.tableView.populateTable()

    #refresh backend data with current data in table
    def refresh(self):
        self.data = self.tableView.getDataInTable()
        for column in self.data.columns:
            self.data[column] = self.data[column].apply(lambda x: x.strip())

    def insertSpectogramInfo(self, fileName, audio, sample_rate):
        self.spectogramInfo[fileName] = [audio, sample_rate]

    def getSpectogramInfo(self):
        return self.spectogramInfo

    def getData(self):
        return self.data

    def addTableView(self, tableView):
        self.tableView = tableView

    def updateRecentFiles(self, filePath):
        self.recentFiles.append(filePath)
        self.recentFiles = self.recentFiles[-4:]

    def getRecentFiles(self):
        return self.recentFiles

    def getLastFileName(self):
        return self.lastFileName

    def setLastFileName(self, name):
        self.lastFileName = name

    def setRunningFlag(self, isRunning):
        self.isRunning = isRunning

    def autosave(self):
        saveInterval = 20
        while self.isRunning:
            #check if isRunning is active every second
            for i in range(saveInterval):
                if self.isRunning:
                    time.sleep(1)
                #if isRunning is false, perform an autosave and end function
                else:
                    with self._lock:
                        self.data.to_csv('Model/BackEnd/LastSession.csv', index=False)
                    return
            #if 20 seconds have passed, perform autosave
            with self._lock:
                #remove whitespace at start and end of every value
                self.data.to_csv('Model/BackEnd/LastSession.csv', index=False)

    def writeRecentFiles(self):
        with open('Model/BackEnd/RecentFilesList.txt', 'w') as f:
            for file in self.recentFiles:
                f.write(file + '\n')

    def readRecentFiles(self):
        with open('Model/BackEnd/RecentFilesList.txt', 'r') as f:
            recentFileList = [line.rstrip('\n') for line in f]
        return recentFileList

    def writeLastFileName(self):
        with open('Model/BackEnd/LastFileName.txt', 'w') as f:
            f.write(self.lastFileName)

    def readLastFileName(self):
        with open('Model/BackEnd/LastFileName.txt', 'r') as f:
            lastFileName = f.read()
        return lastFileName

    def getStandardColumns(self):
        return self.standardColumns

    def getColumns(self):
        return self.data.columns

    def getTable(self):
        return self.tableView