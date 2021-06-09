import unittest
import pandas as pd
import Project.Model.BackEnd.BackEnd as be
from Project.Controller.Actions.AddColumnAction import addColumn
from Project.View.ViewCards import ViewHandler
import PyQt5.QtWidgets as qtw
from Project.Controller.Actions import FileUploadAction

class TestAddColumn(unittest.TestCase):
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

    def test_addColumn(self):
        self.backend.clear()
        self.assertTrue(self.backend.data.empty)

        # check if test is not yet in columns
        self.assertFalse('test' in self.tableView.getColumns())

        # fill in 'test' as column name and check if column is added
        addColumn(self.tableView, qtw)
        self.assertTrue('test' in self.tableView.getColumns())

        # check if 'test.1' is not yet in columns
        self.assertFalse('test.1' in self.tableView.getColumns())

        # fill in 'test' again to get column 'test.1' and check if column is added
        addColumn(self.tableView, qtw)
        self.assertTrue('test.1' in self.tableView.getColumns())

if __name__ == '__main__':
    unittest.main()
