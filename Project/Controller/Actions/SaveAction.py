from Project.Model.OutputHandler.ExportToCsv import exportCSV

def uponActionPerformed(mainWindow, qtw):
    path = mainWindow.windowTitle()
    if path != "Untitled":
        exportCSV(mainWindow, path)
        mainWindow.tableView.populateTable()
        print("saved")
    else:
        print("can't save")


