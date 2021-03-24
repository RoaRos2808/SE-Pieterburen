import csv

def uponActionPerformed(mainWindow, qtw):
    fileExportAction(mainWindow, qtw)

def fileExportAction(mainWindow, qtw):
    dialogFileName = qtw.QInputDialog()
    dialogFileName.setStyleSheet("color:white")
    fileName, ok = dialogFileName.getText(mainWindow, "Enter file name", "Enter file name:")

    if ok:
        file = fileName+".csv"
        dict_data = mainWindow.getBackEnd().getData()

        with open(file, 'a') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in dict_data.items():
                writer.writerow([key, ','.join(value)])
        csv_file.close()
        print('saving is complete')




