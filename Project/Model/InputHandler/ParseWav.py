from Project.Model.CNN import feature_extractor2
import os
# save the audio path and get the CNN results
def parseWavFiles(files, mainWindow):
    for file in files:
        audio_path = file
        fileName = os.path.basename(audio_path)

        #TODO apply model
        #result = feature_extractor2.weight_results(file)

        #TODO set results in dictionary
        data = {"File Name": fileName}

        be = mainWindow.getBackEnd()
        be.update(data)
