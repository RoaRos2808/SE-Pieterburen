from Project.Model.CNN import feature_extractor2

# save the audio path and get the CNN results
def parseWavFiles(files):
    for file in files:
        audio_path = file
        result = feature_extractor2.weight_results(file)
        # TODO: InputHandler to Backend as dictionary(?)