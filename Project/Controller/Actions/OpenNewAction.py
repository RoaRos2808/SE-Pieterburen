from Project.Model.InputHandler.ParseCSV import parseCSVFiles

def uponActionPerformed(mainWindow, qtw):
    openNewAction(mainWindow, qtw)

# opens a dialog with option to save, then clears the table window

def openNewAction(mainWindow, qtw):
    # saveOption = qtw.QMessageBox.question(mainWindow, 'Save',
    #                                       'Would you like to save before creating a new spreadsheet?',
    #                                       qtw.QMessageBox.Yes, qtw.QMessageBox.No)

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
        mainWindow.tableView.backEnd.clear()



