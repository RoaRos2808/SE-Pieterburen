import unittest
import pandas as pd
import Project.Model.BackEnd.BackEnd as be
from Project.Model.CNN import feature_extractor2, feature_extractor3
from Project.View.ViewCards import ViewHandler
import PyQt5.QtWidgets as qtw
from Project.Controller.Actions import FileUploadAction

class TestGetFilesWav(unittest.TestCase):
    def setUp(self):
        self.app = qtw.QApplication([])
        screenResolution = self.app.desktop().screenGeometry()
        windowHeightToScreen, windowWidthToScreen = 0.7, 0.6
        width, height = int(screenResolution.width() * windowWidthToScreen), int(
             screenResolution.height() * windowHeightToScreen)
        self.backend = be.BackEnd()
        self.mw = ViewHandler.MainWindow(width, height, self.backend, 0)
        self.tableView = self.mw.getTableView()
        self.backend.addTableView(self.tableView)

    def test_feature_extractors(self):
        options = qtw.QFileDialog.Options()
        files, _ = qtw.QFileDialog.getOpenFileNames(self.mw, "Select Audio Files", "", "Sound files (*.wav)",
                                                    options=options)
        for file in files:
            result = feature_extractor2.weight_results(file)
            self.assertTrue(result in [0, 1])

            result = feature_extractor3.weight_results(file)
            self.assertTrue(result in [0, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
