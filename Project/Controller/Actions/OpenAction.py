from Project.Model.InputHandler.ParseCSV import parseCSVFiles

def uponActionPerformed(mainWindow, qtw):
    CSVUpload(mainWindow, qtw)

#action for opening a .csv file in the table viewer
def CSVUpload(mainWindow, qtw):
    options = qtw.QFileDialog.Options()
    filePath, _ = qtw.QFileDialog.getOpenFileName(mainWindow, "QFileDialog.getOpenFileNames()",
                                                  "", "Table files (*.csv)", options=options)
    # If files are selected, send  these to the InputHandler
    if filePath:
       openAction(mainWindow, filePath)

def openAction(mainWindow, filePath):
    be = mainWindow.getBackEnd()
    mainWindow.setWindowTitle(filePath)
    parseCSVFiles(filePath, mainWindow)
    be.setLastFileName(filePath)

    if filePath not in be.getRecentFiles():
        be.updateRecentFiles(filePath)
