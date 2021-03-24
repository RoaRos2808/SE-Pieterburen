

def infoAction(mainWindow, qtw):
    mainWindow.infoAction = qtw.QAction('Info', mainWindow, checkable=False)
    uponActionPerformed(mainWindow, qtw)


def uponActionPerformed(mainWindow, qtw):
    mainWindow.infoAction.triggered.connect(lambda: showInfoDialog(mainWindow, qtw))

def showInfoDialog(mainWindow, qtw):
    infoMessage = qtw.QMessageBox(mainWindow)
    infoMessage.setIcon(qtw.QMessageBox.Information)
    infoMessage.setText("How the system works")
    infoMessage.setInformativeText("Something understandable for vets about how the system analyses the sounds and "
                                   "produces the health score.")
    infoMessage.setWindowTitle("Info about software")
    infoMessage.exec_()