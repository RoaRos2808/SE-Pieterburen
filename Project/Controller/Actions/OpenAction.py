import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
from Project.Controller.Actions import CSVFileUploadAction


def uponActionPerformed(mainWindow, qtw):
    CSVFileUploadAction.getFilesCSV(mainWindow, qtw)