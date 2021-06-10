from Project.Model.OutputHandler.ExportToCsv import exportCSV
from Project.Controller.Actions.FileExportAction import fileExportAction

def uponActionPerformed(mainWindow, qtw):
    saveAction(mainWindow, qtw)

def saveAction(mainWindow, qtw):
    path = mainWindow.windowTitle()
    if path != "Wavealyze":
        exportCSV(mainWindow, path)
        #mainWindow.tableView.populateTable()
        #print("saved")
    else:
        fileExportAction(mainWindow, qtw)  # show file dialog if no name yet
