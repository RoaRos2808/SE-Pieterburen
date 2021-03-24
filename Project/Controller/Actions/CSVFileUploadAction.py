from Project.Model.InputHandler.ParseCSV import parseCSVFiles

def uponActionPerformed(mainWindow, qtw):
    getFilesCSV(mainWindow, qtw)

def getFilesCSV(mainWindow, qtw):
    options = qtw.QFileDialog.Options()
    filePath, _ = qtw.QFileDialog.getOpenFileName(mainWindow,"QFileDialog.getOpenFileNames()", "","Sound files (*.csv)", options=options)
    # If files are selected, send  these to the InputHandler
    if filePath:
        parseCSVFiles(filePath, mainWindow)