from Project.Model.OutputHandler.ExportToCsv import exportCSV

def uponActionPerformed(mainWindow, qtw):
    options = qtw.QFileDialog.Options()
    dialogFileName, ok = qtw.QFileDialog.getSaveFileName(mainWindow, "Select File Save Location",
                                                         "default", "CSV file (*.csv)", options=options)
    if ok:
        exportCSV(mainWindow, dialogFileName)






