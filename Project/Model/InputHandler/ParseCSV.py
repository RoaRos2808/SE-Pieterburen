import csv
#TODO it is bugged atm, does not work
def parseCSVFiles(filePath, mainWindow):
    print(filePath)
    with open(filePath, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)
    csv_file.close()

    be = mainWindow.getBackEnd()
    #be.update(data)