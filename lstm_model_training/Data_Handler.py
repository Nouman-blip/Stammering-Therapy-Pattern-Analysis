import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.impute import SimpleImputer
from sklearn.utils import resample
from joblib import dump, load


class DataHandler:
    def __init__(self, stutter_labels_file, mfcc_features_file):
        self.stutter_labels_file = stutter_labels_file
        self.mfcc_features_file = mfcc_features_file
        self.combined_df = None
        self.X_train_scaled = None
        self.X_test_scaled = None
        self.y_train = None
        self.y_test = None
        self.scaler = StandardScaler()

    def load_data(self):
        stutter_labels_df = pd.read_csv(self.stutter_labels_file)
        mfcc_features_df = pd.read_csv(self.mfcc_features_file)
        assert stutter_labels_df.shape[0] == mfcc_features_df.shape[0], "Row counts do not match"

        label_encoder = LabelEncoder()
        stutter_labels_df['label'] = label_encoder.fit_transform(
            stutter_labels_df[['Prolongation', 'Block', 'SoundRep', 'WordRep', 'Interjection', 'NoStutteredWords']].idxmax(axis=1))

        combined_df = pd.concat([mfcc_features_df, stutter_labels_df['label']], axis=1)

        imputer = SimpleImputer(strategy='mean')
        self.combined_df = pd.DataFrame(imputer.fit_transform(combined_df), columns=combined_df.columns)

    def preprocess_data(self):
        df_majority = self.combined_df[self.combined_df.label == 2]
        df_minorities = [self.combined_df[self.combined_df.label == label] for label in range(6) if label != 2]

        df_minority_upsampled = [resample(df, replace=True, n_samples=df_majority.shape[0], random_state=123) for df in df_minorities]
        df_upsampled = pd.concat([df_majority] + df_minority_upsampled)

        X = df_upsampled.drop('label', axis=1).values
        y = to_categorical(df_upsampled['label'].values)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.X_train_scaled = self.scaler.fit_transform(X_train)
        self.X_test_scaled = self.scaler.transform(X_test)
        self.X_train_scaled = np.reshape(self.X_train_scaled, (self.X_train_scaled.shape[0], 1, self.X_train_scaled.shape[1]))
        self.X_test_scaled = np.reshape(self.X_test_scaled, (self.X_test_scaled.shape[0], 1, self.X_test_scaled.shape[1]))

        self.y_train = y_train
        self.y_test = y_test

    def get_data(self):
        return self.X_train_scaled, self.X_test_scaled, self.y_train, self.y_test

    def save_scaler(self, path):
        dump(self.scaler, path)