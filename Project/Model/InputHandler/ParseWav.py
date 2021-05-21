from Project.Model.CNN import feature_extractor2
import os
import math
from Project.View.Miscellaneous.ProgressBar import ProgressBar
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
import time


# save the audio path and get the CNN results
def parseWavFiles(files, mainWindow):
    # added code for a progress dialog. We have to discuss whether we want this though. Maybe a progressbar embedded
    # into the gui instead of a pop-up dialog would look better.
    progressBar = ProgressBar()
    progressBar.setUpProgressDialog()
    progressPercentage = 0

    mainWindow.setEnabled(False)
    for file in files:
        data = pd.DataFrame
        audio_path = file
        fileName = os.path.basename(audio_path)
        leftOrRight = fileName[-5]

        #check if filename has convention of ending in either L or R (have to discuss this), otherwise show error
        if leftOrRight in ['L', 'R']:
            fileName = fileName[:-5]
            # TODO apply model
            result = feature_extractor2.weight_results(file)
            if result == 1:
                result = "Good"
            else:
                result = "Bad"
            #give name without the 'L.wav' or 'R.wav' of string
            be = mainWindow.getBackEnd()

            #not yet implemented, need Cristians model
            type = ""

            be.update(type, fileName, leftOrRight, result)
            bound = progressPercentage + math.floor((1 / len(files)) * 100)
            #allows progress to smoothly increments instead of jumping in large interval percentages
            while progressPercentage <= bound:
                progressPercentage = progressPercentage + 1
                progressBar.updateProgressDialog(progressPercentage)
                time.sleep(0.005)
        else:
            print("wrong file name convention")
            msg = QMessageBox()
            msg.setWindowTitle("Wrong File Name Convention")
            msg.setText("\""+fileName+"\" does not specify if it is a right or left lung!")

    progressBar.finalizeProgressDialog()
    mainWindow.setEnabled(True)
