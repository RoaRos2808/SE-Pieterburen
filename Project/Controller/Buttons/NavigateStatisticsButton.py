from Project.Controller.Actions import NavigateStatisticsAction

def navigateStatisticsButton(mainWindow, qtw):
    mainWindow.NavigateStatisticsButton = qtw.QAction('Statistics', mainWindow, checkable=False)
    mainWindow.NavigateStatisticsButton.triggered.connect(lambda : NavigateStatisticsAction.uponActionPerformed(mainWindow, qtw))