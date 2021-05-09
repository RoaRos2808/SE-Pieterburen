from Project.Model.CNN import feature_extractor2
import os
import math
from Project.View.Miscellaneous.ProgressBar import ProgressBar
from PyQt5.QtWidgets import QMessageBox


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
        leftOrRight = fileName[-5]
        print(leftOrRight)

        #check if filename has convention of ending in either L or R (have to discuss this), otherwise show error
        if leftOrRight in ['L', 'R']:

            # TODO apply model
            result = feature_extractor2.weight_results(file)
            if leftOrRight == 'L':
                data.update({"Left Lung Health": str(result)})
            else:
                data.update({"Right Lung Health": str(result)})

            # TODO set results in dictionary
            #give name without the 'L.wav' or 'R.wav' of string
            fileName = fileName[:-5]
            data.update({"File Name": fileName})

            be = mainWindow.getBackEnd()
            be.update(data)
            progressPercentage = progressPercentage + math.floor((1 / len(files)) * 100)
            progressBar.updateProgressDialog(progressPercentage)
        else:
            print("wrong file name convention")
            msg = QMessageBox()
            msg.setWindowTitle("Wrong File Name Convention")
            msg.setText("\""+fileName+"\" does not specify if it is a right or left lung!")

    progressBar.finalizeProgressDialog()
