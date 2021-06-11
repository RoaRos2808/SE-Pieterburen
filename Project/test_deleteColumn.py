import unittest
import pandas as pd
import Project.Model.BackEnd.BackEnd as be
from Project.Controller.Actions.AddColumnAction import addColumn
from Project.Controller.Actions.DeleteColumnAction import deleteColumn, deleteColumn_test
from Project.View.ViewCards import ViewHandler
import PyQt5.QtWidgets as qtw
from Project.Controller.Actions import FileUploadAction

class TestDeleteColumn(unittest.TestCase):
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

    def test_deleteColumn(self):
        # clear and add two columns for testing
        self.backend.clear()
        addColumn(self.tableView, qtw)
        addColumn(self.tableView, qtw)

        # check if fifth index is present
        columns = self.tableView.getColumns()
        self.assertTrue(columns[5])
        oldFifthIndex = columns[5]

        # delete 5th index and check if column name has been changed
        deleteColumn_test(self.tableView, 5)
        self.assertNotEquals(columns[5], oldFifthIndex)

        # check if first 5 columns remain the same by trying to remove index 3
        # these first 5 columns should always be in the program
        thirdIndex = columns[3]
        deleteColumn(self.tableView, 3)
        self.assertNotEquals(columns[3], thirdIndex)

if __name__ == '__main__':
    unittest.main()
