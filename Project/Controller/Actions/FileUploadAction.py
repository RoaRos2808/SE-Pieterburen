from Project.Model.InputHandler.ParseWav import parseWavFiles
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc


def uponActionPerformed(mainWindow, qtw):
    getFilesWav(mainWindow, qtw)


def getFilesWav(mainWindow, qtw):
    options = qtw.QFileDialog.Options()
    files, _ = qtw.QFileDialog.getOpenFileNames(mainWindow, "Select Audio Files", "", "Sound files (*.wav)",
                                                options=options)
    # If files are selected, send  these to the InputHandler
    if files:
        parseWavFiles(files, mainWindow)
        mainWindow.switchViews("table")

