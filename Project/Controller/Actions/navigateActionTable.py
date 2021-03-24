

def navigateActionTable(mainWindow, qtw):
    mainWindow.navigateActionTable = qtw.QAction('Go table page', mainWindow, checkable=False)
    uponActionPerformed(mainWindow)


def uponActionPerformed(mainWindow):
    mainWindow.navigateActionTable.triggered.connect(lambda: mainWindow.switchViews("table"))