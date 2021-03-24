

def fileActionExport(mainWindow, qtw):
    mainWindow.fileActionExport = qtw.QAction('Export to .csv', mainWindow, checkable=False)
    uponActionPerformed(mainWindow)


def uponActionPerformed(mainWindow):
    mainWindow.fileActionExport.triggered.connect(lambda : print("doe even iets"))