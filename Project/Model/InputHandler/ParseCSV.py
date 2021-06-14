import csv
import pandas as pd
import os

def parseCSVFiles(filePath, mainWindow):
    be = mainWindow.getBackEnd()
    # place csv file in dictionary for TableView's use, and check if csv file is empty or not
    if os.path.getsize(filePath) > 0:
        data = pd.read_csv(filePath)
    else:
        data = be.makeEmptyDataFrame()

    be.openTable(data)