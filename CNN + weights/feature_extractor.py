import librosa
import numpy as np
import math
from keras.models import load_model

"""MFCC Feature Extractor

This script allows the user to extract the mel-cepstral coefficients array from a 
given audio file. It loads the audio file, gets the MFCC array and transforms it such 
that it is valid input for a CNN.

This tool accepts the file path to an audio file, the desired sampling rate and the number of MFCCs.
It returns the coefficients array of the given audio file.

I have also took the time to create a main() where you can see a example of how this tool can be used.

This file can also be imported as a module and contains the following
functions:
    * extract_features - Returns a list which contains the mfcc features of an audio file.
    * get_prediction   - Extracts the features of an audio file and inputs them into the model. 
                         Returns the predicted label
    * main             - Example on how you can load the model and use these functions.

"""

# In our case all audio files have the same length of 30
AUDIO_LENGTH = 30


def get_expected_len(audio_length, sampling_rate):
    sample_per_audio = sampling_rate * audio_length
    return math.ceil(sample_per_audio / 512)


def extract_features(file_path, n_mfcc, sampling_rate=None):
    """Returns a list which contains the mfcc features of each segment.
    :param file_path: Path to the audio file
    :param sampling_rate: Sampling rate value used to resample the audio. A default value of None
    will take the original sampling rate of the audio file (in our case is 4000Hz)
    :param n_mfcc: Number of mfcc which will be extracted over a period of time
    :return: A list containing the MFCC features of each segment in the original audio
    """

    # Because the extracted arrays have variable length we need to calculate the maximum possible
    # number of MFCCs that can be extracted from our audio files and then pad with 0 the arrays
    # which have a length < max length.
    expected_mfcc_len = get_expected_len(AUDIO_LENGTH, sampling_rate)

    try:
        audio, sample_rate = librosa.load(file_path, sr=sampling_rate, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_fft=2048, hop_length=512, n_mfcc=n_mfcc)
        pad_width = expected_mfcc_len - mfccs.shape[1]
        mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')

    except Exception as e:
        print("Error encountered while parsing file: ", file_path)
        return None

    return mfccs


def get_prediction(file_path, model, n_mfcc, sampling_rate=None):
    """
    :param file_path: Path to the audio
    :param model: The model to be used for prediction
    :param n_mfcc: The number of coefficients to be extracted
    :param sampling_rate: Sampling rate
    :return: Predicted label of the audio (i.e: 0 (OK) 1 (MILD) 2(MODERATE) 3(SEVERE)
    """

    num_rows = n_mfcc
    num_columns = get_expected_len(AUDIO_LENGTH, sampling_rate)
    # Always 1 for CNNs
    num_channels = 1

    # Extract the features
    prediction_feature = extract_features(file_path, n_mfcc, sampling_rate)
    # Make the input specific to that of a CNN
    prediction_feature = prediction_feature.reshape(1, num_rows, num_columns, num_channels)

    # Predict the label using model
    predicted_vector = model.predict_classes(prediction_feature)
    predicted_class = predicted_vector

    return predicted_class[0]


if __name__ == '__main__':
    # Load model using weights
    model = load_model("weights.best.basic_cnn.hdf5")

    # Uncomment this only if you are interested in the in-depth info about the model
    # model.summary()

    audio_path = "../Recordings/auscultation-recordings/PV18256/PV18256_291218_L.wav"

    print(get_prediction(audio_path, model, 20, 8000))
