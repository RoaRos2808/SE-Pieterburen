import unittest
import pandas as pd
import Project.Model.BackEnd.BackEnd as be
# from Project.View.ViewCards import ViewHandler
# import PyQt5.QtWidgets as qtw

class TestBackEnd(unittest.TestCase):
    def setUp(self):
        # app = qtw.QApplication([])
        # screenResolution = app.desktop().screenGeometry()
        # windowHeightToScreen, windowWidthToScreen = 0.7, 0.6
        # width, height = int(screenResolution.width() * windowWidthToScreen), int(
        #     screenResolution.height() * windowHeightToScreen)
        self.backend = be.BackEnd()
        # self.mw = ViewHandler.MainWindow(width, height, self.backend)
        # tableView = self.mw.getTableView()
        # self.backend.addTableView(tableView)

    def test_makeEmptyDataFrame(self):
        actual = self.backend.makeEmptyDataFrame()
        # Test if dataframe is empty
        self.assertTrue(actual.empty)

        expected = pd.DataFrame(columns=['File Name', 'Left Lung Health', 'Right Lung Health'])
        # Test if dataframes have the same columns (in order) with no indexes
        self.assertTrue(expected.equals(actual))

        notExpected = pd.DataFrame(columns=['File Name', 'Right Lung Health', 'Left Lung Health'])
        # Test when dataframes don't have the same columns (in order)
        self.assertFalse(notExpected.equals(actual))

        notExpected = pd.DataFrame(columns=[])
        # Test when dataframes don't have the same columns (in order)
        self.assertFalse(notExpected.equals(actual))

    # def test_update(self):
    #     before = self.backend.getData()
    #     self.backend.update("", 'test', 'L', 'Good')
    #     after = self.backend.getData()
    #     self.assertFalse(after.equals(before))



if __name__ == '__main__':
    unittest.main()
