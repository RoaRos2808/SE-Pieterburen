from Project.Controller.Actions import CSVFileUploadAction

def spreadSheetButtonHome(homeView, qtw, qtg, parent):
    spreadsheetButton = qtw.QPushButton(homeView)

    spreadsheetButton.setStyleSheet("QPushButton{"
                                         "background-color:lightblue; "
                                         "border:4px solid white; "
                                         "color:white; "
                                         "padding:0px"
                                         "} "
                                         "QPushButton::pressed{"
                                         "border: 4px solid gray; "
                                         "color: gray"
                                         "}")
    spreadsheetButton.setFont(qtg.QFont('Times', 20))
    spreadsheetButton.setText("Upload\n Spreadsheet")
    spreadsheetButton.setFixedHeight(160)
    spreadsheetButton.clicked.connect(lambda: CSVFileUploadAction.uponActionPerformed(homeView, qtw))
    spreadsheetButton.clicked.connect(lambda: parent.switchViews("table"))
    return spreadsheetButton