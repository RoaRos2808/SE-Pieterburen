

def uponActionPerformed(mainWindow, qtw):
    showInfoDialog(mainWindow, qtw)

def showInfoDialog(mainWindow, qtw):
    infoMessage = qtw.QMessageBox(mainWindow)
    infoMessage.setIcon(qtw.QMessageBox.Information)
    infoMessage.setText("How the system works")
    infoMessage.setInformativeText("Something understandable for vets about how the system analyses the sounds and "
                                   "produces the health score.")
    infoMessage.setWindowTitle("Info about software")
    infoMessage.exec_()