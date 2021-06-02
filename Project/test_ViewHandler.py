import unittest
import PyQt5.QtWidgets as qtw
from Project.View.Miscellaneous import SplashScreen
from Project.View.ViewCards import ViewHandler
from Project.Model.BackEnd import BackEnd as be
import threading
from Project.View.ViewCards import ViewHandler
from Project.main import backEnd as be


class MyTestCase(unittest.TestCase):
    def setUp(self):
        app = qtw.QApplication([])
        # get screen resolution of system used
        screenResolution = app.desktop().screenGeometry()
        # fractions of the screen dimensions to use as dimensions for app
        windowHeightToScreen, windowWidthToScreen = 0.8, 0.7
        width, height = int(screenResolution.width() * windowWidthToScreen), int(
            screenResolution.height() * windowHeightToScreen)
        self.backEnd = be.BackEnd()
        self.mw = ViewHandler.MainWindow(width, height, self.backEnd)

    def test_switchViews(self):
        # check if starts at table view
        self.assertEqual(self.mw.mainWidget.layout().getCurrentIndex(), 0)

        # Change to statistics view
        self.mw.switchViews("statistics")
        self.assertEqual(self.mw.mainWidget.layout().getCurrentIndex(), 1)

        # change back to table view
        self.mw.switchViews("table")
        self.assertEqual(self.mw.mainWidget.layout().getCurrentIndex(), 0)

        self.backEnd.setRunningFlag(False)

if __name__ == '__main__':
    unittest.main()
