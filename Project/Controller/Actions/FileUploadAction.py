
def uponActionPerformed(mainWindow, qtw):
    getFiles(mainWindow, qtw)

def getFileswav(mainWindow, qtw):
    options = qtw.QFileDialog.Options()
    files, _ = qtw.QFileDialog.getOpenFileNames(mainWindow,"QFileDialog.getOpenFileNames()", "","Sound files (*.wav)", options=options)
    if files:
        print(files)

def getFiles(mainWindow, qtw):
    getFileswav(mainWindow, qtw)
