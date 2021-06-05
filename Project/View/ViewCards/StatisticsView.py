import PyQt5.QtWidgets as qtw
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from PyQt5.QtCore import pyqtSlot
import pandas as pd

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class StatisticsView(qtw.QFrame):
    def __init__(self, parent, backEnd):
        super().__init__(parent)
        self.parent = parent
        self.setLayout(qtw.QGridLayout())
        self.setStyleSheet("StatisticsView {background-color:lightblue}")
        self.layout().setContentsMargins(20, 20, 20, 20)

        self.backEnd = backEnd
        self.data = self.backEnd.getData()

        self.figureSizeWidth = 4
        self.figureSizeHeight = 5
        #account for possible 'nan' values
        self.xAxisGraphLabelThreshold = (10 + 1)
        self.xAxisLabelLengthTreshold = 10

        self.checkBoxes = {}
        self.checkedCheckBoxes = []
        self.checkBoxFrame = qtw.QFrame()
        self.scrollAreaCheckBox = qtw.QScrollArea()
        self.scrollAreaCheckBox.setSizePolicy(qtw.QSizePolicy.Preferred, qtw.QSizePolicy.Preferred)
        self.scrollAreaCheckBox.setWidget(self.checkBoxFrame)
        self.scrollAreaCheckBox.setWidgetResizable(True)
        self.scrollAreaCheckBox.setStyleSheet("QScrollBar{background-color: none}")
        self.checkBoxFrame.setStyleSheet("background-color:white")
        self.checkBoxFrame.setLayout(qtw.QVBoxLayout())
        self.checkBoxFrame.layout().setContentsMargins(10, 10, 20, 10)
        self.layout().addWidget(self.scrollAreaCheckBox, 0, 0, 5, 1)

        self.histogramFrame = qtw.QFrame()
        self.scrollAreaHistograms = qtw.QScrollArea()
        self.scrollAreaHistograms.setSizePolicy(qtw.QSizePolicy.Minimum, qtw.QSizePolicy.Minimum)
        self.scrollAreaHistograms.setWidget(self.histogramFrame)
        self.scrollAreaHistograms.setWidgetResizable(True)
        self.scrollAreaHistograms.setStyleSheet("QScrollBar{background-color: none}")
        self.histogramFrame.setStyleSheet("background-color:white")
        self.histogramFrame.setLayout(qtw.QHBoxLayout())
        self.histogramFrame.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self.scrollAreaHistograms, 0, 1, 5, 11)


        self.graphFiguresAndCanvases = {}
        standardColumns = list(self.backEnd.getStandardColumns().columns)
        standardColumns.remove('File Name')
        print(standardColumns)
        for standardColumn in standardColumns:
            figure, canvas = self.createFigureAndCanvas()
            self.graphFiguresAndCanvases[standardColumn] = [figure, canvas]
            self.addCanvas(standardColumn)
            self.plotHistogram(standardColumn)

        self.radioButtons = {}
        self.radioButtonFrame = qtw.QFrame()
        self.scrollAreaRadio = qtw.QScrollArea()
        # self.scrollArea.setSizeAdjustPolicy(AdjustToContents)
        self.scrollAreaRadio.setSizePolicy(qtw.QSizePolicy.Preferred, qtw.QSizePolicy.Preferred)
        self.scrollAreaRadio.setWidget(self.radioButtonFrame)
        self.scrollAreaRadio.setWidgetResizable(True)
        self.scrollAreaRadio.setStyleSheet("QScrollBar{background-color: none}")
        self.radioButtonFrame.setStyleSheet("background-color:white")
        self.radioButtonFrame.setLayout(qtw.QVBoxLayout())
        self.radioButtonFrame.layout().setContentsMargins(10, 10, 20, 10)
        self.layout().addWidget(self.scrollAreaRadio, 5, 0, 4, 2)

        self.saveSpectogramButton = qtw.QPushButton('Save Spectogram')
        self.saveSpectogramButton.setStyleSheet("QPushButton{background-color: none}")
        self.saveSpectogramButton.clicked.connect(lambda: self.saveSpectogram())
        self.layout().addWidget(self.saveSpectogramButton, 9, 0, 1, 2)

        self.figureSpectogram = plt.figure()
        self.canvasSpectogram = FigureCanvas(self.figureSpectogram)
        self.layout().addWidget(self.canvasSpectogram, 5, 2, 5, 10)
        # self.spectogramFrame = qtw.QFrame()
        # self.spectogramFrame.setStyleSheet("background-color:white")
        # self.layout().addWidget(self.spectogramFrame, 1, 1, 1, 5)

        # plot is function that handles drawing of graphs
        self.plot()

    def refreshStatisticPage(self):
        self.refreshCheckBoxes()
        self.refreshRadioButtons()
        self.plot()

    def plot(self):
        self.plotHistograms()
        self.plotSpectogram()

    def createFigureAndCanvas(self):
        figure = plt.figure(constrained_layout=True, figsize=(self.figureSizeWidth, self.figureSizeHeight))
        # figure = plt.figure()
        canvas = FigureCanvas(figure)
        return figure, canvas

    def addCanvas(self, columnHeader):
        frame = qtw.QFrame()
        frame.setLayout(qtw.QVBoxLayout())
        frame.layout().setContentsMargins(0, 0, 0, 0)
        canvas = self.graphFiguresAndCanvases[columnHeader][1]
        frame.setSizePolicy(qtw.QSizePolicy.Minimum, qtw.QSizePolicy.Preferred)
        frame.layout().addWidget(canvas)
        #self.histogramFrame.layout().addWidget(canvas)
        self.histogramFrame.layout().addWidget(frame)

    def plotHistogram(self, columnHeader):
        data = self.backEnd.getData()

        if data.empty:
            data = pd.DataFrame({})

        # before redrawing, empty current figure
        #self.figureLeftLung.clear()

        figure = self.graphFiguresAndCanvases[columnHeader][0]
        canvas = self.graphFiguresAndCanvases[columnHeader][1]

        #figure.set_figwidth(20)

        figure.clear()


        if not columnHeader in data.columns or data.empty or len(
                list(filter(lambda a: a != "", data[columnHeader].unique()))) == 0:
            ax = figure.add_subplot(111)
            #ax.set_xlabel("Assessment")
            #ax.set_ylabel("Frequency")
            ax.set_title(columnHeader)
            ax.axes.xaxis.set_ticks([])
            ax.axes.yaxis.set_ticks([])
            ax.plot()
        else:
            ax = figure.add_subplot(111)
            # this part removes empty strings from being counted in the graph
            columnSpecificData = data[columnHeader]
            columnSpecificData.replace("", float("NaN"), inplace=True)
            columnSpecificData.dropna()

            #columnSpecificData.value_counts().sort_values(ascending=True).plot.bar(ax=ax, xlabel="Assessment",
            #                                                                   ylabel="Frequency",
            #                                                                   title=columnHeader, legend=False,
            #                                                                   rot=0)

            #if number of unique columns surpasses threshold, increase size of figure by (amount/threshold)+figureSizeWidth
            if len(columnSpecificData.unique()) > self.xAxisGraphLabelThreshold:
                newWidth = int((len(columnSpecificData.unique())/self.xAxisGraphLabelThreshold)+self.figureSizeWidth)
                figure.set_figwidth(newWidth)

            #turn every value in frame into a string, so it can be manipulated
            columnSpecificData = columnSpecificData.apply(str)
            #brief explanation following line: when labels of x axis get too long, the figure gets shorter.
            #to prevent labels from taking all the space of the figure, we make sure the label is divided into new lines.
            #that is what the lambda function does, it adds a newline character every interval of length threshold
            columnSpecificData = columnSpecificData.apply(lambda x: '-\n'.join(x[i:i+(self.xAxisLabelLengthTreshold)] for i in range(0, len(x), (self.xAxisLabelLengthTreshold))))
            #columnSpecificData.apply(self.insertNewLineInteval)


            columnSpecificData.value_counts().sort_values(ascending=True).plot.bar(ax=ax,title=columnHeader, legend=False)
            #figure.bar(ax=ax, title=columnHeader, legend=False)

            #figure.tight_layout()
        canvas.draw()

    def plotHistograms(self):
        for graph in self.graphFiguresAndCanvases.keys():
            self.plotHistogram(graph)

    def plotSpectogram(self):
        self.figureSpectogram.clear()
        fileName = None
        for key in list(self.radioButtons.keys()):
            if self.radioButtons[key].isChecked():
                fileName = key
                break
        axSpecto = self.figureSpectogram.add_subplot(111)
        if not fileName is None:
            spectogramInfo = self.backEnd.getSpectogramInfo()
            audio = spectogramInfo[fileName][0]
            sr = spectogramInfo[fileName][1]

            # fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
            # self.figureSpectogram = fig

            # axSpecto = self.figureSpectogram.add_subplot(nrows=2, ncols=1, sharex=True)
            D = librosa.amplitude_to_db(np.abs(librosa.stft(audio)), ref=np.max)
            img = librosa.display.specshow(D, y_axis='linear', x_axis='time', sr=sr, ax=axSpecto)
            self.figureSpectogram.colorbar(img, ax=axSpecto, format="%+2.f dB")
        else:
            # set up axis when no button is pressed
            axSpecto.set_xlabel('Time')
            axSpecto.set_ylabel('Hz')
            axSpecto.set_xticks(np.arange(0, 35, 5).tolist())
            axSpecto.set_yticks(np.arange(0, 2250, 250).tolist())

        axSpecto.set(title='Linear-frequency power spectrogram')
        axSpecto.label_outer()

        self.canvasSpectogram.draw()
        self.figureSpectogram.savefig('oke.png')

    def refreshRadioButtons(self):
        self.radioButtons = {}
        # first delete all radiobuttons from its frame
        while self.radioButtonFrame.layout().count():
            item = self.radioButtonFrame.layout().takeAt(0)
            item.widget().deleteLater()
        # now add the new list of radiobuttons
        self.radioButtonNames = list(self.backEnd.getSpectogramInfo().keys())
        for buttonName in self.radioButtonNames:
            button = qtw.QRadioButton(buttonName)
            button.toggled.connect(lambda: self.plotSpectogram())
            self.radioButtons[buttonName] = button
            self.radioButtonFrame.layout().addWidget(button)

    def refreshCheckBoxes(self):
        #self.checkBoxes = {}
        # first delete all checkboxes from its frame
        while self.checkBoxFrame.layout().count():
            item = self.checkBoxFrame.layout().takeAt(0)
            item.widget().deleteLater()
        # now add the new list of radiobuttons
        self.checkBoxNames = list(self.backEnd.getData().columns)
        #remove standard columns from this list, since we won't add them as checkboxes
        for standardColumn in list(self.backEnd.getStandardColumns().columns):
            if standardColumn in self.checkBoxNames:
                self.checkBoxNames.remove(standardColumn)
        #check if a checkbox in checkedCheckedBoxes is not anymore present in current possible checkboxNames (columns of dataframe)
        for checkBoxName in self.checkedCheckBoxes:
            if checkBoxName not in self.checkBoxNames:
                self.checkedCheckBoxes.remove(checkBoxName)
        #now go over every column header given by the dataframe after extracting the standard columns
        for checkBoxName in self.checkBoxNames:
            checkBox = qtw.QCheckBox(checkBoxName)
            checkBox.toggled.connect(lambda: self.uponCheckBoxInteraction())
            #these following lines simply check
            if checkBoxName in self.checkedCheckBoxes:
                checkBox.setChecked(True)
            self.checkBoxes[checkBoxName] = checkBox
            self.checkBoxFrame.layout().addWidget(checkBox)

    def saveSpectogram(self):
        for buttonName in self.radioButtonNames:
            if self.radioButtons[buttonName].isChecked():
                options = qtw.QFileDialog.Options()
                dialogFileName, ok = qtw.QFileDialog.getSaveFileName(self.parent, "Select File Save Location",
                                                                     "default", "PNG file (*.png)", options=options)
                if ok:
                    # print(dialogFileName)
                    self.figureSpectogram.savefig(dialogFileName)

                break

    def uponCheckBoxInteraction(self):
        #go through all the checkbox names
        for checkboxName in self.checkBoxes.keys():
            #get checkbox widget itself
            checkbox = self.checkBoxes[checkboxName]
            #if the checkbox widget is selected
            if checkbox.isChecked():
                if checkboxName not in self.checkedCheckBoxes:
                    self.checkedCheckBoxes.append(checkboxName)
                #if the checkbox name is not in the graphFiguresAndCanvases, it should be cause it needs to be drawn
                #if it is both checked, ánd also in the graphFiguresAndCanvases, nothing needs to be done
                if checkboxName not in self.graphFiguresAndCanvases:
                    figure, canvas = self.createFigureAndCanvas()
                    self.graphFiguresAndCanvases[checkboxName] = [figure, canvas]
                    self.addCanvas(checkboxName)
                    self.plotHistogram(checkboxName)
                    self.plotHistogram(checkboxName)
            #else, if the checkbox is not selected
            else:
                if checkboxName in self.checkedCheckBoxes:
                    self.checkedCheckBoxes.remove(checkboxName)
                #if it is not selected but it is in graphsFiguresAndCanvases, it should be removed
                if checkboxName in self.graphFiguresAndCanvases:
                    index = list(self.graphFiguresAndCanvases.keys()).index(checkboxName)
                    self.histogramFrame.layout().takeAt(index).widget().deleteLater()
                    del self.graphFiguresAndCanvases[checkboxName]
                    break

    def insertNewLineInteval(self, str):
        return '\n'.join(str[i:i + 3] for i in range(0, len(str), 3))

    def test(self):
        item = self.layout().takeAt(4)
        item.widget().deleteLater()
        #while self.radioButtonFrame.layout().count():
        #    item = self.radioButtonFrame.layout().takeAt(0)
        #    item.widget().deleteLater()

    def test2(self):
        columns = list(self.backEnd.getStandardColumns().columns)
        columns.remove('File Name')
        for column in columns:
            self.addCanvas(column)
            self.plotHistogram(column)