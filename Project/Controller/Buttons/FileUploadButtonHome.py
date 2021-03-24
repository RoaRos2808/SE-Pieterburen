from Project.Controller.Actions import FileUploadAction

def fileUploadButtonHome(homeView, qtw, qtg, mainWindow):
    uploadButton = qtw.QPushButton(homeView)

    uploadButton.setStyleSheet("QPushButton{"
                                    "background-color:lightblue; "
                                    "border:4px solid white; "
                                    "color:white; "
                                    "padding:0px"
                                    "} "
                                    "QPushButton::pressed{"
                                    "border: 4px solid gray; "
                                    "color: gray"
                                    "}")
    uploadButton.setFont(qtg.QFont('Times', 20))
    uploadButton.setText("Upload Sound\n File(s)")
    uploadButton.setFixedHeight(160)
    uploadButton.clicked.connect(lambda: FileUploadAction.uponActionPerformed(mainWindow, qtw))
    uploadButton.clicked.connect(lambda: mainWindow.switchViews("table"))
    return uploadButton