from Project.Model.OutputHandler.ExportToCsv import exportCSV

def uponActionPerformed(mainWindow, qtw):
    fileExportAction(mainWindow, qtw)

def fileExportAction(mainWindow, qtw):
    options = qtw.QFileDialog.Options()
    dialogFileName, ok = qtw.QFileDialog.getSaveFileName(mainWindow, "Select File Save Location",
                                                         "default", "CSV file (*.csv)", options=options)
    if ok:
        mainWindow.setWindowTitle(dialogFileName)
        be = mainWindow.getBackEnd()
        be.setLastFileName(dialogFileName)
        if dialogFileName not in be.getRecentFiles():
            be.updateRecentFiles(dialogFileName)
        exportCSV(mainWindow, dialogFileName)


