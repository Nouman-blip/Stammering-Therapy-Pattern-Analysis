# feature.py
import joblib
import librosa
import numpy as np
import tensorflow as tf

class StutterFeatureExtractor:
    def __init__(self, model_path, scaler_path):
        self.model = tf.keras.models.load_model(model_path)
        self.scaler = joblib.load(scaler_path)
        

    def extract_mfcc_features(self, audio_file, n_mfcc=1000):
        y, sr = librosa.load(audio_file, sr=None)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
        mfcc_scaled = np.mean(mfcc.T, axis=0)
        mfcc_scaled = mfcc_scaled.reshape(1, -1)
        return mfcc_scaled

    def predict_stutter_type(self, audio_file):
        mfcc_features = self.extract_mfcc_features(audio_file)
        mfcc_features_scaled = self.scaler.transform(mfcc_features)
        mfcc_features_scaled = mfcc_features_scaled.reshape(1, 1, -1)
        prediction = self.model.predict(mfcc_features_scaled)
        predicted_class = np.argmax(prediction, axis=1)
        return predicted_class[0]
