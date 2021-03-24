from Project.Controller.Actions import NavigateHomeAction

def navigateHomeButton(mainWindow, qtw):
    mainWindow.NavigateHomeButton = qtw.QAction('Navigate to home', mainWindow, checkable=False)
    mainWindow.NavigateHomeButton.triggered.connect(lambda : NavigateHomeAction.uponActionPerformed(mainWindow, qtw))