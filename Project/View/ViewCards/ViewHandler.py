import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import Project.img.resources as resources
import Project.View.ViewCards.TableView as tv
import Project.View.ViewCards.StatisticsView as sv

from Project.Controller.Buttons import  FileUploadButton, InfoButton, AddColumnButton, \
    FileExportButton, NavigateTableButton, NavigateStatisticsButton, DeleteRowButton, DeleteColumnButton, CSVFileUploadButton, OpenNewButton, \
    OpenRecentMenu, OpenButton
# represents main app window and acts as canvas on which the different views are painted

class MainWindow(qtw.QMainWindow):
    def __init__(self, width, height, backEnd):
        super().__init__()

        self.maxFileNr = 4
        self.recentFiles = []

        self.setWindowIcon(qtg.QIcon(qtg.QPixmap(':/windowiconsmall.png')))

        self.setWindowTitle('Pieterburen ZeehondenCentrum')
        self.setGeometry(0, 0, width, height)
        self.mainWidget = qtw.QWidget(self)
        # create stack layout to get ability to switch between views
        self.mainWidget.setLayout(qtw.QStackedLayout())
        # layouts in pyqt have margins by default, so we turn these off
        self.mainWidget.layout().setContentsMargins(0, 0, 0, 0)

        self.tableView = tv.TableView(self, backEnd)
        self.statisticsView = sv.StatisticsView(self, backEnd)

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
        elif viewName == "statistics":
            self.AddColumnButton.setEnabled(False)
            self.mainWidget.layout().setCurrentIndex(1)


    def menuBarSetup(self):
        self.initializeActions()
        menuBar = self.initializeMenuBar()
        return menuBar

    # add actions to buttons
    def initializeActions(self):

        # initialize actions
        FileUploadButton.fileUploadButton(self, qtw)
        FileExportButton.fileExportButton(self, qtw)
        CSVFileUploadButton.csvFileUploadButton(self, qtw)
        OpenButton.openButton(self,qtw)
        OpenNewButton.openNewButton(self, qtw)
        OpenRecentMenu.openRecentMenu(self, qtw)
        AddColumnButton.addColumnButton(self, self.tableView, qtw)
        DeleteRowButton.deleteRowButton(self, self.tableView, qtw)
        DeleteColumnButton.deleteColumnButton(self, self.tableView, qtw)
        # NavigateHomeButton.navigateHomeButton(self, qtw) -- deprecated
        NavigateTableButton.navigateTableButton(self, qtw)
        NavigateStatisticsButton.navigateStatisticsButton(self, qtw)
        InfoButton.infoButton(self, qtw)

    def initializeMenuBar(self):
        menuBar = qtw.QMenuBar(self)

        fileMenu = menuBar.addMenu('File')
        editMenu = menuBar.addMenu('Edit')
        navigateMenu = menuBar.addMenu('Navigate')

        # before
        # fileMenu.addAction(self.FileUploadButton) v
        # fileMenu.addAction(self.FileExportButton) v
        # fileMenu.addAction(self.CSVFileUploadButton) x
        # fileMenu.addAction(self.OpenButton) v
        # fileMenu.addAction(self.OpenRecentButton) v
        # fileMenu.addAction(self.OpenNewButton) v

        # editMenu.addAction(self.AddColumnButton)
        # editMenu.addAction(self.DeleteRowButton)
        # editMenu.addAction(self.DeleteColumnButton)
        #
        # navigateMenu.addAction(self.NavigateHomeButton)
        # navigateMenu.addAction(self.NavigateTableButton)
        # menuBar.addAction(self.InfoButton)

        # after
        fileMenu.addAction(self.OpenNewButton)
        fileMenu.addAction(self.OpenButton)
        fileMenu.addMenu(self.OpenRecentMenu)  # TODO needs implementation
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

    def getTableView(self):
        return self.tableView

    def getBackEnd(self):
        return self.tableView.getBackEnd()

    def activateDeleteRowButton(self, boolean):
        self.DeleteRowButton.setEnabled(boolean)

    def activateDeleteColumnButton(self, boolean):
        self.DeleteColumnButton.setEnabled(boolean)
