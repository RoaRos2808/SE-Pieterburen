

def uponActionPerformed(mainWindow, qtw):
    showInfoDialog(mainWindow, qtw)

def showInfoDialog(mainWindow, qtw):
    infoMessage = qtw.QMessageBox(mainWindow)
    infoMessage.setIcon(qtw.QMessageBox.Information)
    infoMessage.setText("How the system works")
    infoMessage.setInformativeText("Thank you for using Wavealyze. Here is a brief overview of how to use the program.\n\n"
                                   "To upload files, click on the edit menu and select \'Upload sound file(s)\'\n\n"
                                   "It is required that the last character of a file name should be either capitol \'L\' or \'R\'\n"
                                   "This will indicate whether the recording is of a left or right lung, and places results in the same row.\n\n"
                                   "To continue working on a already existing .csv file, use the open button in the file menu to upload.\n"
                                   "To let the program add new results to existing rows, use the following convention.\n\n"
                                   "Use the columns:\n File Name, Left Lung Whistle, Right Lung Whistle, Left Lung Rhonchus, Right Lung Rhonchus\n\n"
                                   "If these columns exist in a .csv file, the program will simply add newly generated results to these columns\n")
    infoMessage.setWindowTitle("Info about software")
    infoMessage.exec_()