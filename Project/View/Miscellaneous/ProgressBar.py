import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc

class ProgressBar(qtw.QProgressDialog):
    def __init__(self):
        super().__init__()
        dlg = qtw.QProgressDialog('Working...', "Iets", 0, 100)
        self.setMinimumHeight(100)
        self.setMinimumWidth(300)
        self.setAutoReset(True)
        self.setAutoClose(True)
        self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | self.windowFlags() | qtc.Qt.WindowCloseButtonHint)
        self.setWindowModality(qtc.Qt.WindowModal)
        dlg.setMinimumDuration(0)
        dlg.setMinimum(0)
        dlg.setMaximum(100)
        self.setWindowTitle("Processing audio files")
        self.setLabelText("Please wait while the audio files are being processed")
        self.setCancelButton(None)

    def setUpProgressDialog(self):
        self.show()
        self.setValue(0)
        qtw.QApplication.processEvents()

    def updateProgressDialog(self, value):
        self.setValue(value)
        qtw.QApplication.processEvents()

    def finalizeProgressDialog(self):
        self.setValue(100)
        qtw.QApplication.processEvents()