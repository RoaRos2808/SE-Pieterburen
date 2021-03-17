import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import HomeView as hv
import TableView as tv

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

    def showInfoDialog(self):
        infoMessage = qtw.QMessageBox(self)
        infoMessage.setIcon(qtw.QMessageBox.Information)
        infoMessage.setText("How the system works")
        infoMessage.setInformativeText("Something understandable for vets about how the system analyses the sounds and "
                                       "produces the health score.")
        infoMessage.setWindowTitle("Info about software")
        infoMessage.exec_()

    def menuBarSetup(self):
        menuBar = qtw.QMenuBar(self)

        fileMenu = menuBar.addMenu('File')
        editMenu = menuBar.addMenu('Edit')
        navigateMenu = menuBar.addMenu('Navigate')

        self.fileActionUpload = qtw.QAction('Upload sound file(s)', self, checkable=False)
        self.fileActionExport = qtw.QAction('Export to .csv', self, checkable=False)
        # k.triggered.connect(lambda : print("doe even iets"))

        self.editActionAdd = qtw.QAction('Add column', self, checkable=False)
        self.editActionElse = qtw.QAction('Something else', self, checkable=False)
        self.editActionAdd.triggered.connect(lambda: self.tableView.addColumn())

        self.navigateActionHome = qtw.QAction('Go home page', self, checkable=False)
        self.navigateActionTable = qtw.QAction('Go table page', self, checkable=False)
        self.navigateActionHome.triggered.connect(lambda: self.switchViews("home"))
        self.navigateActionTable.triggered.connect(lambda: self.switchViews("table"))

        #info action is in menubar and should perform action without displaying submenu:
        #to achieve this, directly add a QAction to menubar instead of a menu
        self.infoAction = qtw.QAction('Info', self, checkable=False)
        self.infoAction.triggered.connect(lambda: self.showInfoDialog())
        menuBar.addAction(self.infoAction)

        #add actions to submenu's
        fileMenu.addAction(self.fileActionUpload)
        fileMenu.addAction(self.fileActionExport)
        editMenu.addAction(self.editActionAdd)
        editMenu.addAction(self.editActionElse)
        navigateMenu.addAction(self.navigateActionHome)
        navigateMenu.addAction(self.navigateActionTable)

        return menuBar