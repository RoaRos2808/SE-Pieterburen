import PyQt5.QtWidgets as qtw
import Project.View.HomeView as hv
import Project.View.TableView as tv
from Project.Controller import editActionAdd
from Project.Controller import fileActionUpload
from Project.Controller import fileActionExport
from Project.Controller import navigateActionHome
from Project.Controller import navigateActionTable
from Project.Controller import infoAction
#represents main app window and acts as canvas on which the different views are painted



class MainWindow(qtw.QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.setWindowTitle('Pieterburen ZeehondenCentrum')
        self.setGeometry(0, 0, width, height)
        self.mainWidget = qtw.QWidget(self)
        #create stack layout to get ability to switch between views
        self.mainWidget.setLayout(qtw.QStackedLayout())
        #layouts in pyqt have margins by default, so we turn these off
        self.mainWidget.layout().setContentsMargins(0, 0, 0, 0)

        self.homeView = hv.HomeView(self)
        self.tableView = tv.TableView(self)

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
            self.editActionAdd.setEnabled(False)
            self.mainWidget.layout().setCurrentIndex(0)
        elif viewName == "table":
            self.editActionAdd.setEnabled(True)
            self.mainWidget.layout().setCurrentIndex(1)

    def menuBarSetup(self):
        self.initializeActions()
        menuBar = self.initializeMenuBar()
        return menuBar

    # add actions to buttons
    def initializeActions(self):

        # initialize actions
        fileActionUpload.fileActionUpload(self, qtw)
        fileActionExport.fileActionExport(self, qtw)
        editActionAdd.editActionAdd(self, self.tableView, qtw)
        navigateActionHome.navigateActionHome(self, qtw)
        navigateActionTable.navigateActionTable(self, qtw)
        infoAction.infoAction(self, qtw)

        # in for now to show how it was before
        self.editActionElse = qtw.QAction('Something else', self, checkable=False)

    def initializeMenuBar(self):
        menuBar = qtw.QMenuBar(self)

        fileMenu = menuBar.addMenu('File')
        editMenu = menuBar.addMenu('Edit')
        navigateMenu = menuBar.addMenu('Navigate')

        fileMenu.addAction(self.fileActionUpload)
        fileMenu.addAction(self.fileActionExport)
        editMenu.addAction(self.editActionAdd)
        editMenu.addAction(self.editActionElse)
        navigateMenu.addAction(self.navigateActionHome)
        navigateMenu.addAction(self.navigateActionTable)
        menuBar.addAction(self.infoAction)

        return menuBar