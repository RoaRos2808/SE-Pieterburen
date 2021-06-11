import unittest
import pandas as pd
import Project.Model.BackEnd.BackEnd as be
from Project.View.ViewCards import ViewHandler
import PyQt5.QtWidgets as qtw

# Test each method separately, when running this entire class it gives a weird access violation error
class TestBackEnd(unittest.TestCase):
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

    def test_makeEmptyDataFrame(self):
        actual = self.backend.makeEmptyDataFrame()
        # Test if dataframe is empty
        self.assertTrue(actual.empty)

        expected = pd.DataFrame(columns=['File Name', 'Left Lung Whistle', 'Right Lung Whistle', 'Left Lung Rhonchus',
                                         'Right Lung Rhonchus'])
        # Test if dataframes have the same columns (in order) with no indexes
        self.assertTrue(expected.equals(actual))

        notExpected = pd.DataFrame(columns=['File Name', 'Right Lung Whistle', 'Left Lung Whistle',  'Left Lung Rhonchus',
                                         'Right Lung Rhonchus'])

        # Test when dataframes don't have the same columns (in order)
        self.assertFalse(notExpected.equals(actual))

        notExpected = pd.DataFrame(columns=[])
        # Test when dataframes don't have the same columns (in order)
        self.assertFalse(notExpected.equals(actual))


    def test_clear(self):
        # Fill the data and make sure it is not empty
        self.backend.data.loc[1, ["Left Lung Whistle"]] = 'Yes'
        actualData = self.backend.data
        self.assertFalse(actualData.empty)

        # clear the data
        self.backend.clear()

        # check if data is empty now
        actualData = self.backend.data
        self.assertTrue(actualData.empty)

    def test_update(self):
        # make empty data set
        self.backend.clear()
        self.assertTrue(self.backend.data.empty)

        self.backend.update('PV12345_678901_L.wav', 'L', 'Yes', 'Moderate')

        # check if data is now not empty
        data = self.backend.data
        self.assertFalse(data.empty)

        # check if the update for a left lung was good
        index = self.backend.data.index[self.backend.data["File Name"] == "PV12345_678901_L.wav"]
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

        # check if right lung rhonchus is still empty
        actual = self.backend.data.loc[index, ["Right Lung Rhonchus"]].values[0]
        result = ""
        self.assertTrue(actual == result)

        # update for a right lung
        self.backend.update('PV12345_678901_R.wav', 'R', 'Yes', 'Moderate')

        index = index = self.backend.data.index[self.backend.data["File Name"] == "PV12345_678901_R.wav"]
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

        # update the same file as previously done, with new values
        self.backend.update('PV12345_678901_L.wav', 'L', 'No', 'Severe')

        index = index = self.backend.data.index[self.backend.data["File Name"] == "PV12345_678901_L.wav"]
        actual = self.backend.data.loc[index, ["Left Lung Whistle"]].values[0]
        result = "Yes"
        self.assertFalse(actual == result)

        actual = self.backend.data.loc[index, ["Left Lung Whistle"]].values[0]
        result = "No"
        self.assertTrue(actual == result)

        actual = self.backend.data.loc[index, ["Left Lung Rhonchus"]].values[0]
        result = "Moderate"
        self.assertFalse(actual == result)

        actual = self.backend.data.loc[index, ["Left Lung Rhonchus"]].values[0]
        result = "Severe"
        self.assertTrue(actual == result)

        # update for a right lung for previously uploaded file
        self.backend.update('PV12345_678901_R.wav', 'R', 'No', 'Severe')

        index = index = self.backend.data.index[self.backend.data["File Name"] == "PV12345_678901_R.wav"]
        actual = self.backend.data.loc[index, ["Right Lung Whistle"]].values[0]
        result = "Yes"
        self.assertFalse(actual == result)

        actual = self.backend.data.loc[index, ["Right Lung Whistle"]].values[0]
        result = "No"
        self.assertTrue(actual == result)

        actual = self.backend.data.loc[index, ["Right Lung Rhonchus"]].values[0]
        result = "Moderate"
        self.assertFalse(actual == result)

        actual = self.backend.data.loc[index, ["Right Lung Rhonchus"]].values[0]
        result = "Severe"
        self.assertTrue(actual == result)

        # reset everything
        self.backend.clear()

    def test_openTable(self):
        self.backend.update('PV12345_678901_L.wav', 'L', 'Yes', 'Moderate')

        # check if the update for a left lung was good
        index1 = self.backend.data.index[self.backend.data["File Name"] == "PV12345_678901_L.wav"]
        actual = self.backend.data.loc[index1, ["Left Lung Whistle"]].values[0]
        result = "Yes"
        self.assertTrue(actual == result)

        actual = self.backend.data.loc[index1, ["Left Lung Whistle"]].values[0]
        result = "No"
        self.assertFalse(actual == result)

        actual = self.backend.data.loc[index1, ["Left Lung Rhonchus"]].values[0]
        result = "Moderate"
        self.assertTrue(actual == result)

        actual = self.backend.data.loc[index1, ["Left Lung Rhonchus"]].values[0]
        result = "Severe"
        self.assertFalse(actual == result)

        data = pd.DataFrame({"File Name": ['PV12345_123456_L.wav'], "Left Lung Whistle": ['Yes'],
                                   "Left Lung Rhonchus": ['Severe']})

        self.backend.openTable(data)
        # check if the new data is in the program
        index2 = self.backend.data.index[self.backend.data["File Name"] == "PV12345_123456_L.wav"]
        actual = self.backend.data.loc[index2, ["Left Lung Whistle"]].values[0]
        result = "Yes"
        self.assertTrue(actual == result)

        actual = self.backend.data.loc[index2, ["Left Lung Whistle"]].values[0]
        result = "No"
        self.assertFalse(actual == result)

        actual = self.backend.data.loc[index2, ["Left Lung Rhonchus"]].values[0]
        result = "Moderate"
        self.assertFalse(actual == result)

        actual = self.backend.data.loc[index2, ["Left Lung Rhonchus"]].values[0]
        result = "Severe"
        self.assertTrue(actual == result)

if __name__ == '__main__':
    unittest.main()
