
from Project.Controller.Actions import InfoAction

def infoButton(mainWindow, qtw):
    mainWindow.InfoButton = qtw.QAction('Info', mainWindow, checkable=False)
    mainWindow.InfoButton.setShortcut('Ctrl+i')
    mainWindow.InfoButton.triggered.connect(lambda : InfoAction.uponActionPerformed(mainWindow, qtw))