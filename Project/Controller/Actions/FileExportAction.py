import csv

def uponActionPerformed(mainWindow, qtw):
    fileExportAction(mainWindow, qtw)

def fileExportAction(mainWindow, qtw):
    options = qtw.QFileDialog.Options()
    dialogFileName, ok = qtw.QFileDialog.getSaveFileName(mainWindow, "Select File Save Location",
                                                     "default", "CSV file (*.csv)", options=options)

    if ok:
        fileName = dialogFileName
        print(fileName)
        file = fileName
        dict_data = mainWindow.getBackEnd().getData()

        with open(file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            row = []
            for index, key in enumerate(dict_data.keys()):
                row.append(key)
            writer.writerow(row)

            #this can be written a lot better, but works for now. Get amount of rows under a column as index
            for index in range(len(list(dict_data.values())[0])):
                row = []
                for value in dict_data.values():
                    row.append(value[index])
                writer.writerow(row)

        csv_file.close()
        print('saving is completed')




