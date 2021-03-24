

def fileActionUpload(mainWindow, qtw):
    mainWindow.fileActionUpload = qtw.QAction('Upload sound file(s)', mainWindow, checkable=False)
    uponActionPerformed(mainWindow, qtw)

def uponActionPerformed(mainWindow, qtw):
    mainWindow.fileActionUpload.triggered.connect(lambda : getFiles(mainWindow, qtw))

def getFileswav(mainWindow, qtw):
    options = qtw.QFileDialog.Options()
    files, _ = qtw.QFileDialog.getOpenFileNames(mainWindow,"QFileDialog.getOpenFileNames()", "","Sound files (*.wav)", options=options)
    if files:
        print(files)

def getFiles(mainWindow, qtw):
    getFileswav(mainWindow, qtw)
