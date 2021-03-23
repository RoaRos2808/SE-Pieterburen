

def fileActionUpload(mainWindow, qtw):
    mainWindow.fileActionUpload = qtw.QAction('Upload sound file(s)', mainWindow, checkable=False)
    uponActionPerformed(mainWindow)

def uponActionPerformed(mainWindow):
    mainWindow.fileActionUpload.triggered.connect(lambda : print("doe even iets"))