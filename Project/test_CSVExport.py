import unittest
import pandas as pd
import Project.Model.BackEnd.BackEnd as be
from Project.Controller.Actions.FileExportAction import fileExportAction
from Project.Controller.Actions.OpenAction import CSVUpload
from Project.View.ViewCards import ViewHandler
import PyQt5.QtWidgets as qtw
from Project.Controller.Actions import FileUploadAction

class TestCSVExport(unittest.TestCase):
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

    #
    def test_fileExportAction(self):
        # make empty table and check if it is indeed empty
        self.backend.clear()
        self.assertTrue(self.backend.data.empty)

        # add left and right lung of audio file info and confirm table is not empty
        self.backend.update('PV12345_678901_L.wav', 'L', 'Yes', 'Moderate')
        self.backend.update('PV12345_678901_L.wav', 'R', 'Yes', 'Moderate')
        self.assertFalse(self.backend.data.empty)

        # export the table to .csv file
        fileExportAction(self.mw, qtw)

        # clear the table and confirm it is empty
        self.backend.clear()
        self.assertTrue(self.backend.data.empty)

        # upload the just exported .csv file
        CSVUpload(self.mw, qtw)
        index = 0

        # check if all info is indeed correct
        actual = self.backend.data.loc[index, ["Left Lung Whistle"]].values[0]
        result = "Yes"
        self.assertTrue(actual == result)

        actual = self.backend.data.loc[index, ["Left Lung Whistle"]].values[0]
        result = "No"
        self.assertFalse(actual == result)

        actual = self.backend.data.loc[index, ["Left Lung Rhonchus"]].values[0]
        result = "Moderate"
        self.assertTrue(actual == result)

        actual = self.backend.data.loc[index, ["Left Lung Rhonchus"]].values[0]
        result = "Severe"
        self.assertFalse(actual == result)

        actual = self.backend.data.loc[index, ["Right Lung Whistle"]].values[0]
        result = "Yes"
        self.assertTrue(actual == result)

        actual = self.backend.data.loc[index, ["Right Lung Whistle"]].values[0]
        result = "No"
        self.assertFalse(actual == result)

        actual = self.backend.data.loc[index, ["Right Lung Rhonchus"]].values[0]
        result = "Moderate"
        self.assertTrue(actual == result)

        actual = self.backend.data.loc[index, ["Right Lung Rhonchus"]].values[0]
        result = "Severe"
        self.assertFalse(actual == result)


if __name__ == '__main__':
    unittest.main()
