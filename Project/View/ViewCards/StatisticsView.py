import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from PyQt5.QtCore import pyqtSlot
import pandas as pd

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

#biggest problem with statistics thus far: after uploading sound files, the statistics page plots incorrect data.
#the data is correct after an autosave has occured. (probably because only then the backend is fully updated.
#might have to implement workaround that backend gets updated every time table is altered and not only when autosave occurs

class StatisticsView(qtw.QFrame):
    def __init__(self, parent, backEnd):
        super().__init__(parent)
        self.parent = parent
        self.setLayout(qtw.QGridLayout())
        self.setStyleSheet("background-color:lightblue")
        self.layout().setContentsMargins(20, 20, 20, 20)

        self.backEnd = backEnd
        self.data = self.backEnd.getData()

        self.figureLeftLung = plt.figure()
        self.canvasLeftLung = FigureCanvas(self.figureLeftLung)
        self.layout().addWidget(self.canvasLeftLung, 0, 0, 1, 3)

        self.figureRightLung = plt.figure()
        self.canvasRightLung = FigureCanvas(self.figureRightLung)
        self.layout().addWidget(self.canvasRightLung, 0, 3, 1, 3)

        self.radioButtonNames = ['file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2']
        #self.radioButtonNames = []
        self.radioButtonFrame = qtw.QFrame()
        self.scrollArea = qtw.QScrollArea()
        #self.scrollArea.setSizeAdjustPolicy(AdjustToContents)
        self.scrollArea.setSizePolicy(qtw.QSizePolicy.Preferred, qtw.QSizePolicy.Preferred)
        self.scrollArea.setWidget(self.radioButtonFrame)
        self.scrollArea.setWidgetResizable(True)
        self.radioButtonFrame.setStyleSheet("background-color:white")
        self.radioButtonFrame.setLayout(qtw.QVBoxLayout())
        self.radioButtonFrame.layout().setContentsMargins(20, 10, 20, 10)
        #self.layout().addWidget(self.radioButtonFrame, 1, 0, 1, 1)
        self.layout().addWidget(self.scrollArea, 1, 0, 1, 1)

        self.tempFrame = qtw.QFrame()
        self.tempFrame.setStyleSheet("background-color:white")
        self.layout().addWidget(self.tempFrame, 1, 1, 1, 5)

        #plot is function that handles drawing of graphs
        self.plot()

    def refreshStatisticPage(self):
        self.plot()
        self.refreshRadioButtons()


    def plot(self):
        data = self.backEnd.getData()

        if data.empty:
            data = pd.DataFrame({})

        #before redrawing, empty current figure
        self.figureLeftLung.clear()
        #this is not an ideal workaround, we have to figure out something better.
        #with current method of plotting, it crashes when trying to plot empty pandas series
        #therefore, if a series is empty (i.e., the column is not present or is empty), we use another approach to draw
        #an empty plot that does have x and y axes
        #the line below checks if column name is present, or dataframe is empty, or if there are only empty strings
        #(note that the data kept in statistics view trims all whitespace value to empty strings)
        if not 'Left Lung Health' in data.columns or data.empty or len(list(filter(lambda a: a != "", data['Left Lung Health'].unique()))) == 0:
            axLeftLung = self.figureLeftLung.add_subplot(111)
            axLeftLung.set_xlabel("Health Score")
            axLeftLung.set_ylabel("Frequency")
            axLeftLung.set_title("Left Lung Health")
            axLeftLung.axes.xaxis.set_ticks([])
            axLeftLung.axes.yaxis.set_ticks([])
            axLeftLung.plot()
        else:
            axLeftLung = self.figureLeftLung.add_subplot(111)
            #this part removes empty strings from being counted in the graph
            leftLungHealth = data['Left Lung Health']
            leftLungHealth.replace("", float("NaN"), inplace=True)
            leftLungHealth.dropna()

            leftLungHealth.value_counts().sort_values(ascending=True).plot.bar(ax=axLeftLung, xlabel="Health Score",
                                                             ylabel="Frequency", title="Left Lung Health", legend=False,
                                                             rot=0)

        #exact same is done for right lung
        self.figureRightLung.clear()
        if not 'Right Lung Health' in data.columns or data.empty or len(list(filter(lambda a: a != "", data['Right Lung Health'].unique()))) == 0:
            ax = self.figureRightLung.add_subplot(111)
            ax.set_xlabel("Health Score")
            ax.set_ylabel("Frequency")
            ax.set_title("Right Lung Health")
            ax.axes.xaxis.set_ticks([])
            ax.axes.yaxis.set_ticks([])
            ax.plot()
        else:
            ax = self.figureRightLung.add_subplot(111)
            #this part removes empty strings from being counted in the graph
            rightLungHealth = data['Right Lung Health']
            rightLungHealth.replace("", float("NaN"), inplace=True)
            rightLungHealth.dropna()
            data['Right Lung Health'].value_counts().sort_values(ascending=True).plot.bar(ax=ax, xlabel="Health Score",
                                                              ylabel="Frequency", title="Right Lung Health",
                                                              legend=False,
                                                              rot=0)


        self.canvasLeftLung.draw()
        self.canvasRightLung.draw()

    def refreshRadioButtons(self):
        for buttonName in self.radioButtonNames:
            button = qtw.QRadioButton(buttonName)
            self.radioButtonFrame.layout().addWidget(button)
