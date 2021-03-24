from Project.Model.InputHandler.ParseWav import parseWavFiles

def uponActionPerformed(mainWindow, qtw):
    getFilesCSV(mainWindow, qtw)

def getFilesCSV(mainWindow, qtw):
    options = qtw.QFileDialog.Options()
    files, _ = qtw.QFileDialog.getOpenFileNames(mainWindow,"QFileDialog.getOpenFileNames()", "","Sound files (*.csv)", options=options)
    # If files are selected, send  these to the InputHandler