
def editActionAdd(mainWindow, tableWindow, qtw):
    mainWindow.editActionAdd = qtw.QAction('Add column', mainWindow, checkable=False)
    uponActionPerformed(mainWindow, tableWindow, qtw)
    #editMenu.addAction(self.editActionAdd)

def uponActionPerformed(mainWindow, tableWindow, qtw):
    mainWindow.editActionAdd.triggered.connect(lambda: addColumn(tableWindow, qtw))