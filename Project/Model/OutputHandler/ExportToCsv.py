import csv

def exportCSV(mainWindow, fileName):
    export_data = mainWindow.getBackEnd().getData()
    export_data.to_csv(fileName, index=False)

    print('saving is completed')