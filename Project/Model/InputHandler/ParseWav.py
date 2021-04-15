from Project.Model.CNN import feature_extractor2
import os
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import math
from Project.View.ProgressBar import ProgressBar


# save the audio path and get the CNN results
def parseWavFiles(files, mainWindow):
    # added code for a progress dialog. We have to discuss whether we want this though. Maybe a progressbar embedded
    # into the gui instead of a pop-up dialog would look better.
    progressBar = ProgressBar()
    progressBar.setUpProgressDialog()
    progressPercentage = 0

    for file in files:
        data = {}
        audio_path = file
        fileName = os.path.basename(audio_path)

        # TODO apply model
        result = feature_extractor2.weight_results(file)
        data.update({"Health Score": str(result)})

        # TODO set results in dictionary
        data.update({"File Name": fileName})

        be = mainWindow.getBackEnd()
        be.update(data)
        progressPercentage = progressPercentage + math.floor((1 / len(files)) * 100)
        progressBar.updateProgressDialog(progressPercentage)

    progressBar.finalizeProgressDialog()
