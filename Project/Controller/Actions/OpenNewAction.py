import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
from Project.Controller.Actions import FileExportAction


def uponActionPerformed(mainWindow, qtw):
    openNewAction(mainWindow, qtw)


def openNewAction(mainWindow, qtw):
    print("clicked")
    saveOption = qtw.QMessageBox.question(mainWindow, 'Save',
                                          'Would you like to save before opening another file?',
                                          qtw.QMessageBox.Yes, qtw.QMessageBox.No)
    if saveOption == qtw.QMessageBox.Yes:
        FileExportAction.uponActionPerformed(mainWindow, qtw)
        mainWindow.tableView.backEnd.clear()

    else:
        print("no")
        mainWindow.tableView.backEnd.clear()
