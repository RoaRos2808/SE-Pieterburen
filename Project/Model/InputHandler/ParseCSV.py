import csv
import pandas as pd

def parseCSVFiles(filePath, mainWindow):
    # place csv file in dictionary for TableView's use
    data = pd.read_csv(filePath)
    #data.rename(columns=lambda x: x.strip(), inplace=True)
    #print(data)
    be = mainWindow.getBackEnd()
    be.openTable(data)