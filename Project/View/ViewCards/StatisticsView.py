import PyQt5.QtWidgets as qtw
import librosa
import librosa.display
import numpy as np
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

        self.figureLeftLung = plt.figure()
        self.canvasLeftLung = FigureCanvas(self.figureLeftLung)
        self.layout().addWidget(self.canvasLeftLung, 0, 0, 5, 3)

        self.figureRightLung = plt.figure()
        self.canvasRightLung = FigureCanvas(self.figureRightLung)
        self.layout().addWidget(self.canvasRightLung, 0, 3, 5, 3)

        self.figureLeftLungRhonchus = plt.figure()
        self.canvasLeftLungRhonchus = FigureCanvas(self.figureLeftLungRhonchus)
        self.layout().addWidget(self.canvasLeftLungRhonchus, 0, 6, 5, 3)

        self.figureRightLungRhonchus = plt.figure()
        self.canvasRightLungRhonchus = FigureCanvas(self.figureRightLungRhonchus)
        self.layout().addWidget(self.canvasRightLungRhonchus, 0, 9, 5, 3)

        # self.radioButtonNames = ['file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2', 'file 1', 'file 2']
        # self.radioButtonNames = []
        self.radioButtons = {}
        self.radioButtonFrame = qtw.QFrame()
        self.scrollArea = qtw.QScrollArea()
        # self.scrollArea.setSizeAdjustPolicy(AdjustToContents)
        self.scrollArea.setSizePolicy(qtw.QSizePolicy.Preferred, qtw.QSizePolicy.Preferred)
        self.scrollArea.setWidget(self.radioButtonFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet("QScrollBar{background-color: none}")
        self.radioButtonFrame.setStyleSheet("background-color:white")
        self.radioButtonFrame.setLayout(qtw.QVBoxLayout())
        self.radioButtonFrame.layout().setContentsMargins(10, 10, 20, 10)
        # self.layout().addWidget(self.radioButtonFrame, 1, 0, 1, 1)
        self.layout().addWidget(self.scrollArea, 5, 0, 4, 2)

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
        self.refreshRadioButtons()
        self.plot()

    def plot(self):
        self.plotHistograms()
        self.plotSpectogram()

    def plotHistograms(self):
        data = self.backEnd.getData()

        if data.empty:
            data = pd.DataFrame({})

        # before redrawing, empty current figure
        self.figureLeftLung.clear()
        # this is not an ideal workaround, we have to figure out something better.
        # with current method of plotting, it crashes when trying to plot empty pandas series
        # therefore, if a series is empty (i.e., the column is not present or is empty), we use another approach to draw
        # an empty plot that does have x and y axes
        # the line below checks if column name is present, or dataframe is empty, or if there are only empty strings
        # (note that the data kept in statistics view trims all whitespace value to empty strings)
        if not 'Left Lung Whistle' in data.columns or data.empty or len(
                list(filter(lambda a: a != "", data['Left Lung Whistle'].unique()))) == 0:
            axLeftLung = self.figureLeftLung.add_subplot(111)
            axLeftLung.set_xlabel("Assessment")
            axLeftLung.set_ylabel("Frequency")
            axLeftLung.set_title("Left Lung Whistle")
            axLeftLung.axes.xaxis.set_ticks([])
            axLeftLung.axes.yaxis.set_ticks([])
            axLeftLung.plot()
        else:
            axLeftLung = self.figureLeftLung.add_subplot(111)
            # this part removes empty strings from being counted in the graph
            leftLungHealth = data['Left Lung Whistle']
            leftLungHealth.replace("", float("NaN"), inplace=True)
            leftLungHealth.dropna()

            leftLungHealth.value_counts().sort_values(ascending=True).plot.bar(ax=axLeftLung, xlabel="Assessment",
                                                                               ylabel="Frequency",
                                                                               title="Left Lung Whistle", legend=False,
                                                                               rot=0)

        # exact same is done for right lung
        self.figureRightLung.clear()
        if not 'Right Lung Whistle' in data.columns or data.empty or len(
                list(filter(lambda a: a != "", data['Right Lung Whistle'].unique()))) == 0:
            ax = self.figureRightLung.add_subplot(111)
            ax.set_xlabel("Assessment")
            ax.set_ylabel("Frequency")
            ax.set_title("Right Lung Whistle")
            ax.axes.xaxis.set_ticks([])
            ax.axes.yaxis.set_ticks([])
            ax.plot()
        else:
            ax = self.figureRightLung.add_subplot(111)
            # this part removes empty strings from being counted in the graph
            rightLungHealth = data['Right Lung Whistle']
            rightLungHealth.replace("", float("NaN"), inplace=True)
            rightLungHealth.dropna()
            data['Right Lung Whistle'].value_counts().sort_values(ascending=True).plot.bar(ax=ax, xlabel="Assessment",
                                                                                           ylabel="Frequency",
                                                                                           title="Right Lung Whistle",
                                                                                           legend=False,
                                                                                           rot=0)

        # same for leftlungrhonchus
        self.figureLeftLungRhonchus.clear()
        if not 'Left Lung Rhonchus' in data.columns or data.empty or len(
                list(filter(lambda a: a != "", data['Left Lung Rhonchus'].unique()))) == 0:
            axLeftLungRhonchus = self.figureLeftLungRhonchus.add_subplot(111)
            axLeftLungRhonchus.set_xlabel("Assessment")
            axLeftLungRhonchus.set_ylabel("Frequency")
            axLeftLungRhonchus.set_title("Left Lung Rhonchus")
            axLeftLungRhonchus.axes.xaxis.set_ticks([])
            axLeftLungRhonchus.axes.yaxis.set_ticks([])
            axLeftLungRhonchus.plot()
        else:
            axLeftLungRhonchus = self.figureLeftLungRhonchus.add_subplot(111)
            # this part removes empty strings from being counted in the graph
            leftLungHealthRhonchus = data['Left Lung Rhonchus']
            leftLungHealthRhonchus.replace("", float("NaN"), inplace=True)
            leftLungHealthRhonchus.dropna()

            leftLungHealthRhonchus.value_counts().sort_values(ascending=True).plot.bar(ax=axLeftLungRhonchus,
                                                                                       xlabel="Assessment",
                                                                                       ylabel="Frequency",
                                                                                       title="Left Lung Rhonchus",
                                                                                       legend=False,
                                                                                       rot=0)

        # exact same is done for right lung rhonchus
        self.figureRightLungRhonchus.clear()
        if not 'Right Lung Rhonchus' in data.columns or data.empty or len(
                list(filter(lambda a: a != "", data['Right Lung Rhonchus'].unique()))) == 0:
            # print(len(list(filter(lambda a: a != "", data['Right Lung Rhonchus'].unique()))) == 0)
            axRhonchus = self.figureRightLungRhonchus.add_subplot(111)
            axRhonchus.set_xlabel("Assessment")
            axRhonchus.set_ylabel("Frequency")
            axRhonchus.set_title("Right Lung Rhonchus")
            axRhonchus.axes.xaxis.set_ticks([])
            axRhonchus.axes.yaxis.set_ticks([])
            axRhonchus.plot()
        else:
            axRhonchus = self.figureRightLungRhonchus.add_subplot(111)
            # this part removes empty strings from being counted in the graph
            rightLungHealthRhonchus = data['Right Lung Rhonchus']
            rightLungHealthRhonchus.replace("", float("NaN"), inplace=True)
            rightLungHealthRhonchus.dropna()
            data['Right Lung Rhonchus'].value_counts().sort_values(ascending=True).plot.bar(ax=axRhonchus,
                                                                                            xlabel="Assessment",
                                                                                            ylabel="Frequency",
                                                                                            title="Right Lung Rhonchus",
                                                                                            legend=False,
                                                                                            rot=0)

        self.canvasLeftLung.draw()
        self.canvasRightLung.draw()
        self.canvasLeftLungRhonchus.draw()
        self.canvasRightLungRhonchus.draw()

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

    def saveSpectogram(self):
        for buttonName in self.radioButtonNames:
            if self.radioButtons[buttonName].isChecked():
                options = qtw.QFileDialog.Options()
                dialogFileName, ok = qtw.QFileDialog.getSaveFileName(self.parent, "Select File Save Location",
                                                                     "default", "PNG file (*.png)", options=options)
                if ok:
                    # print(dialogFileName)
                    self.figureSpectogram.savefig('spec.png')

                break
