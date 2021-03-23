import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

class HomeView(qtw.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setLayout(qtw.QGridLayout())
        self.layout().setContentsMargins(0,0,0,0)

        self.setStyleSheet('background-color: lightblue')

        self.labelLogo = qtw.QLabel(self)

        self.labelLogo.setStyleSheet('background-color: lightblue')
        self.pixmapLogo = qtg.QPixmap('img/logosmall.png')
        self.labelLogo.setPixmap(self.pixmapLogo)
        self.labelLogo.setAlignment(qtc.Qt.AlignCenter)

        #gridlayout allows widgets to be placed with following arguments widget to be placed, row index, column index,
        #number of rows stretched and number of columns stretched. We place first container on cell with index (0,0),
        # and stretch it 2 rows and 5 columns. Later, we add button containers on cells with index (2,1) and (2,3) and
        # stretch them 1 row and 1 column each. This way, the logo gets 2/3 window height and full width, and buttons
        # get 1/3 window height and 1/5 window width
        self.layout().addWidget(self.labelLogo, 0, 0, 2, 5)

        self.uploadButton = qtw.QPushButton(self)

        self.uploadButton.setStyleSheet("QPushButton{"
                                        "background-color:lightblue; "
                                        "border:4px solid white; "
                                        "color:white; "
                                        "padding:0px"
                                        "} "
                                        "QPushButton::pressed{"
                                        "border: 4px solid gray; "
                                        "color: gray"
                                        "}")
        self.uploadButton.setFont(qtg.QFont('Times', 20))
        self.uploadButton.setText("Upload Sound\n File(s)")
        self.uploadButton.setFixedHeight(160)
        self.uploadButton.clicked.connect(self.getFileswav)
        self.uploadButton.clicked.connect(lambda: parent.switchViews("table"))

        # create a new frame to set the padding for bottom row (done per button), otherwise buttons will be stuck to
        #bottom of screen
        containerSoundButton = qtw.QFrame(self)
        containerSoundButton.setLayout(qtw.QGridLayout())
        containerSoundButton.setContentsMargins(0, 0, 0, 0)
        containerSoundButton.layout().addWidget(self.uploadButton, 0, 0, 1, 1)
        containerSoundButton.setStyleSheet("padding-bottom:30px; background:lightblue")
        self.layout().addWidget(containerSoundButton, 2, 1, 1, 1)


        self.spreadsheetButton = qtw.QPushButton(self)

        self.spreadsheetButton.setStyleSheet("QPushButton{"
                                             "background-color:lightblue; "
                                             "border:4px solid white; "
                                             "color:white; "
                                             "padding:0px"
                                             "} "
                                             "QPushButton::pressed{"
                                             "border: 4px solid gray; "
                                             "color: gray"
                                             "}")
        self.spreadsheetButton.setFont(qtg.QFont('Times', 20))
        self.spreadsheetButton.setText("Upload\n Spreadsheet")
        self.spreadsheetButton.setFixedHeight(160)
        self.spreadsheetButton.clicked.connect(self.getFilescsv)
        self.spreadsheetButton.clicked.connect(lambda: parent.switchViews("table"))

        containerSheetButton = qtw.QFrame(self)
        containerSheetButton.setLayout(qtw.QGridLayout())
        containerSheetButton.setContentsMargins(0, 0, 0, 0)
        containerSheetButton.layout().addWidget(self.spreadsheetButton, 0, 0, 1, 1)
        containerSheetButton.setStyleSheet("padding-bottom:30px; background:lightblue")
        self.layout().addWidget(containerSheetButton, 2, 3, 1, 1)


    def getFilesmp3(self):
        options = qtw.QFileDialog.Options()
        files, _ = qtw.QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","Sound files (*.mp3)", options=options)
        if files:
            print(files)

    def getFileswav(self):
        options = qtw.QFileDialog.Options()
        files, _ = qtw.QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","Sound files (*.wav)", options=options)
        if files:
            print(files)

    def getFilescsv(self):
        options = qtw.QFileDialog.Options()
        files, _ = qtw.QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","Csv files (*.csv)", options=options)
        if files:
            print(files)