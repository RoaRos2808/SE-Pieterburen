import csv
from collections import defaultdict

def parseCSVFiles(filePath, mainWindow):
    # place csv file in dictionary for TableView's use
    data = defaultdict(list)
    with open(filePath) as csv_file:
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
            for key in row:
                data[key].append(row[key])

    print(data)
    be = mainWindow.getBackEnd()
    be.openTable(data)