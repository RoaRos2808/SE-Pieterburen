from Project.Model.InputHandler.ParseCSV import parseCSVFiles
from os import path
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui

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
    if path.exists(filePath):
        mainWindow.setWindowTitle(filePath)
        parseCSVFiles(filePath, mainWindow)
        be.setLastFileName(filePath)

        if filePath not in be.getRecentFiles():
            be.updateRecentFiles(filePath)
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("File path does not exist.")
        msg.setWindowIcon(QtGui.QIcon('View/Icons/warningSign.png'))
        msg.exec()
