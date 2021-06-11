import unittest
import pandas as pd
import Project.Model.BackEnd.BackEnd as be
from Project.Controller.Actions.AddColumnAction import addColumn
from Project.Controller.Actions.DeleteColumnAction import deleteColumn
from Project.Controller.Actions.DeleteRowAction import deleteRow, deleteRow_test
from Project.View.ViewCards import ViewHandler
import PyQt5.QtWidgets as qtw
from Project.Controller.Actions import FileUploadAction

class TestDeleteRow(unittest.TestCase):
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

    def test_deleteRow(self):
        # clear and add two columns for testing
        self.backend.clear()
        self.assertTrue(self.backend.data.empty)

        # fill with data and confirm this
        self.backend.update('PV12345_678901_L.wav', 'L', 'Yes', 'Moderate')
        self.assertFalse(self.backend.data.empty)

        # delete the just added row and check if this is correct
        deleteRow_test(self.tableView, 0)
        self.assertTrue(self.backend.data.empty)



if __name__ == '__main__':
    unittest.main()

