import PyQt5.QtWidgets as qtw
import Project.View.HomeView as hv
import Project.View.TableView as tv
from Project.Controller.Buttons import NavigateHomeButton, FileUploadButton, InfoButton, AddColumnButton, \
    FileExportButton, NavigateTableButton, DeleteRowButton, DeleteColumnButton

#represents main app window and acts as canvas on which the different views are painted

class MainWindow(qtw.QMainWindow):
    def __init__(self, width, height, backEnd):
        super().__init__()

        self.setWindowTitle('Pieterburen ZeehondenCentrum')
        self.setGeometry(0, 0, width, height)
        self.mainWidget = qtw.QWidget(self)
        #create stack layout to get ability to switch between views
        self.mainWidget.setLayout(qtw.QStackedLayout())
        #layouts in pyqt have margins by default, so we turn these off
        self.mainWidget.layout().setContentsMargins(0, 0, 0, 0)

        self.homeView = hv.HomeView(self)
        self.tableView = tv.TableView(self, backEnd)

        self.mainWidget.layout().addWidget(self.homeView)
        self.mainWidget.layout().addWidget(self.tableView)
        self.setCentralWidget(self.mainWidget)

        self.menuBar = self.menuBarSetup()

        self.setMenuBar(self.menuBar)
        self.switchViews("home")
        self.show()

    #switch views based on viewname
    def switchViews(self, viewName):
        if viewName == "home":
            self.AddColumnButton.setEnabled(False)
            self.mainWidget.layout().setCurrentIndex(0)
        elif viewName == "table":
            self.AddColumnButton.setEnabled(True)
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
        AddColumnButton.addColumnButton(self, self.tableView, qtw)
        DeleteRowButton.deleteRowButton(self, self.tableView, qtw)
        DeleteColumnButton.deleteColumnButton(self, self.tableView, qtw)
        NavigateHomeButton.navigateHomeButton(self, qtw)
        NavigateTableButton.navigateTableButton(self, qtw)
        InfoButton.infoButton(self, qtw)

    def initializeMenuBar(self):
        menuBar = qtw.QMenuBar(self)

        fileMenu = menuBar.addMenu('File')
        editMenu = menuBar.addMenu('Edit')
        navigateMenu = menuBar.addMenu('Navigate')

        fileMenu.addAction(self.FileUploadButton)
        fileMenu.addAction(self.FileExportButton)
        editMenu.addAction(self.AddColumnButton)
        editMenu.addAction(self.DeleteRowButton)
        editMenu.addAction(self.DeleteColumnButton)
        navigateMenu.addAction(self.NavigateHomeButton)
        navigateMenu.addAction(self.NavigateTableButton)
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