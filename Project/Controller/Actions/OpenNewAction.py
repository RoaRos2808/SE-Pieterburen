from Project.Model.InputHandler.ParseCSV import parseCSVFiles

def uponActionPerformed(mainWindow, qtw):
    openNewAction(mainWindow, qtw)

# opens a dialog with option to save, then clears the table window
def openNewAction(mainWindow, qtw):

    #check if data is empty before we give the option to save
    data = mainWindow.tableView.backEnd.getData()

    if not data.empty:
        msgBox = qtw.QMessageBox(mainWindow)
        msgBox.setText("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setWindowTitle("Save")
        msgBox.setStandardButtons(qtw.QMessageBox.Yes | qtw.QMessageBox.Discard | qtw.QMessageBox.Cancel)
        saveOption = msgBox.exec_()

        if saveOption == qtw.QMessageBox.Yes:
            options = qtw.QFileDialog.Options()
            filePath, _ = qtw.QFileDialog.getOpenFileName(mainWindow, "QFileDialog.getOpenFileNames()",
                                                          "", "Table files (*.csv)", options=options)

            # If files are selected, send  these to the InputHandler
            if filePath:
                mainWindow.setWindowTitle(filePath)
                parseCSVFiles(filePath, mainWindow)
                mainWindow.tableView.backEnd.clear()

        elif saveOption == qtw.QMessageBox.Discard:
            mainWindow.setWindowTitle("Untitled")
            be = mainWindow.getBackEnd()
            be.setLastFileName("Untitled")
            mainWindow.tableView.backEnd.clear()
