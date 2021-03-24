from Project.Model.CNN import feature_extractor2

def uponActionPerformed(mainWindow, qtw):
    getFileswav(mainWindow, qtw)

def getFileswav(mainWindow, qtw):
    options = qtw.QFileDialog.Options()
    files, _ = qtw.QFileDialog.getOpenFileNames(mainWindow,"QFileDialog.getOpenFileNames()", "","Sound files (*.wav)", options=options)
    if files:
        print(files)
        for file in files:
            feature_extractor2.weight_results()
