

def navigateActionHome(mainWindow, qtw):
    mainWindow.navigateActionHome = qtw.QAction('Go home page', mainWindow, checkable=False)
    uponActionPerformed(mainWindow)


def uponActionPerformed(mainWindow):
    mainWindow.navigateActionHome.triggered.connect(lambda: mainWindow.switchViews("home"))