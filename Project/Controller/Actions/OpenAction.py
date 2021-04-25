import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
from Project.Controller.Actions import CSVFileUploadAction

#action for opening a .csv file in the table viewer
def uponActionPerformed(mainWindow, qtw):
    CSVFileUploadAction.getFilesCSV(mainWindow, qtw)