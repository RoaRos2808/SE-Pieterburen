import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import Project.View.ViewCards.TableView as tv
import Project.View.ViewCards.StatisticsView as sv
import os
from Project.Controller.Actions.OpenAction import openAction
from Project.Controller.Buttons import FileUploadButton, InfoButton, AddColumnButton, \
    FileExportButton, NavigateTableButton, NavigateStatisticsButton, DeleteRowButton, DeleteColumnButton, OpenNewButton, \
    OpenButton, SaveButton
# represents main app window and acts as canvas on which the different views are painted

class MainWindow(qtw.QMainWindow):
    def __init__(self, width, height, backEnd):
        super().__init__()

        self.recentFiles = []
        self.setWindowIcon(qtg.QIcon(qtg.QPixmap(':/windowiconsmall.png')))

        self.setGeometry(0, 0, width, height)
        self.mainWidget = qtw.QWidget(self)
        # create stack layout to get ability to switch between views
        self.mainWidget.setLayout(qtw.QStackedLayout())
        # layouts in pyqt have margins by default, so we turn these off
        self.mainWidget.layout().setContentsMargins(0, 0, 0, 0)

        qtRectangle = self.frameGeometry()
        centerPoint = qtw.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        qtRectangle = self.frameGeometry()
        centerPoint = qtw.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.tableView = tv.TableView(self, backEnd)
        self.statisticsView = sv.StatisticsView(self, backEnd)

        self.setWindowTitle(self.getBackEnd().getLastFileName())

        self.mainWidget.layout().addWidget(self.tableView)
        self.mainWidget.layout().addWidget(self.statisticsView)

        self.setCentralWidget(self.mainWidget)

        self.menuBar = self.menuBarSetup()

        self.setMenuBar(self.menuBar)
        self.switchViews("table")
        self.show()

    # switch views based on viewname
    def switchViews(self, viewName):
        if viewName == "table":
            self.AddColumnButton.setEnabled(True)
            self.mainWidget.layout().setCurrentIndex(0)
            self.activateNavigateTableButton(False)
            self.activateNavigateStatisticsButton(True)
        elif viewName == "statistics":
            self.statisticsView.refreshStatisticPage()
            self.AddColumnButton.setEnabled(False)
            self.mainWidget.layout().setCurrentIndex(1)
            self.activateNavigateTableButton(True)
            self.activateNavigateStatisticsButton(False)


    def menuBarSetup(self):
        self.initializeActions()
        menuBar = self.initializeMenuBar()
        return menuBar

    # add actions to buttons
    def initializeActions(self):

        # initialize actions
        FileUploadButton.fileUploadButton(self, qtw)
        FileExportButton.fileExportButton(self, qtw)
        SaveButton.saveButton(self, qtw)
        OpenButton.openButton(self, qtw)
        OpenNewButton.openNewButton(self, qtw)
        AddColumnButton.addColumnButton(self, self.tableView, qtw)
        DeleteRowButton.deleteRowButton(self, self.tableView, qtw)
        DeleteColumnButton.deleteColumnButton(self, self.tableView, qtw)
        NavigateTableButton.navigateTableButton(self, qtw)
        NavigateStatisticsButton.navigateStatisticsButton(self, qtw)
        InfoButton.infoButton(self, qtw)

    def initializeMenuBar(self):
        menuBar = qtw.QMenuBar(self)

        fileMenu = menuBar.addMenu('File')
        editMenu = menuBar.addMenu('Edit')
        navigateMenu = menuBar.addMenu('Navigate')

        fileMenu.addAction(self.OpenNewButton)
        fileMenu.addAction(self.OpenButton)

        #TODO migrate to right place
        self.recentMenu = fileMenu.addMenu("Open Recent")
        self.recentMenu.aboutToShow.connect(self.updateRecentMenu)
        self.recentMenu.triggered.connect(self.openFileFromRecent)

        fileMenu.addAction(self.SaveButton)
        fileMenu.addAction(self.FileExportButton)

        editMenu.addAction(self.FileUploadButton)
        editMenu.addAction(self.AddColumnButton)
        editMenu.addAction(self.DeleteRowButton)
        editMenu.addAction(self.DeleteColumnButton)

        # navigateMenu.addAction(self.NavigateHomeButton) -- deprecated
        navigateMenu.addAction(self.NavigateTableButton)
        navigateMenu.addAction(self.NavigateStatisticsButton)
        menuBar.addAction(self.InfoButton)
        return menuBar

    def updateRecentMenu(self):
        self.recentMenu.clear()
        be = self.getBackEnd()
        for file in be.getRecentFiles():
            recentAction = self.recentMenu.addAction(os.path.basename(file))
            recentAction.setData(file)

    def openFileFromRecent(self, action):
        openAction(self, action.data())

    def getTableView(self):
        return self.tableView

    def getBackEnd(self):
        return self.tableView.getBackEnd()

    def activateDeleteRowButton(self, boolean):
        self.DeleteRowButton.setEnabled(boolean)

    def activateDeleteColumnButton(self, boolean):
        self.DeleteColumnButton.setEnabled(boolean)

    def activateNavigateTableButton(self, boolean):
        self.NavigateTableButton.setEnabled(boolean)

    def activateNavigateStatisticsButton(self, boolean):
        self.NavigateStatisticsButton.setEnabled(boolean)

    def closeEvent(self, *args, **kwargs):
        super(qtw.QMainWindow, self).closeEvent(*args, **kwargs)
        be = self.getBackEnd()
        be.writeRecentFiles()
        be.writeLastFileName()
