from Project.Model.InputHandler.ParseCSV import parseCSVFiles
import os
from Project.Model.OutputHandler.ExportToCsv import exportCSV

def uponActionPerformed(mainWindow, qtw):
    openNewAction(mainWindow, qtw)


# opens a dialog with option to save, then clears the table window
def openNewAction(mainWindow, qtw):
    # check if data is empty before we give the option to save
    data = mainWindow.tableView.backEnd.getData()

    if not data.empty:
        be = mainWindow.getBackEnd()
        if mainWindow.windowTitle() == "Wavealyze":
            currentPath = "Wavealyze"
        else:
            currentPath = os.path.basename(mainWindow.windowTitle())

        msgBox = qtw.QMessageBox(mainWindow)
        msgBox.setText("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setWindowTitle("Save")
        msgBox.setStandardButtons(qtw.QMessageBox.Yes | qtw.QMessageBox.No | qtw.QMessageBox.Cancel)
        saveOption = msgBox.exec_()

        if saveOption == qtw.QMessageBox.Yes:
            options = qtw.QFileDialog.Options()
            dialogFileName, ok = qtw.QFileDialog.getSaveFileName(mainWindow, "Select File Save Location",
                                                                 currentPath, "CSV file (*.csv)", options=options)

            # If files are selected, send  these to the InputHandler
            if ok:
                mainWindow.setWindowTitle(dialogFileName)
                exportCSV(mainWindow, dialogFileName)
                be.setLastFileName(dialogFileName)
                if dialogFileName not in be.getRecentFiles():
                    be.updateRecentFiles(dialogFileName)
                be.clear()

        elif saveOption == qtw.QMessageBox.No:
            mainWindow.setWindowTitle("Wavealyze")
            be.setLastFileName("Wavealyze")
            mainWindow.tableView.backEnd.clear()
