
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
import matplotlib.pyplot as plt
import seaborn as sns 

class ModelManager:
    def __init__(self, input_shape, number_of_classes):
        self.input_shape = input_shape
        self.number_of_classes = number_of_classes
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(LSTM(50, return_sequences=True, input_shape=self.input_shape))
        model.add(Dropout(0.3))
        model.add(LSTM(50, return_sequences=False))
        model.add(Dropout(0.3))
        model.add(Dense(self.number_of_classes, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def train_model(self, X_train, y_train, X_test, y_test):
        self.model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

    def evaluate_model(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        y_pred_classes = np.argmax(y_pred, axis=1)
        y_test_classes = np.argmax(y_test, axis=1)
        accuracy = accuracy_score(y_test_classes, y_pred_classes)
        report = classification_report(y_test_classes, y_pred_classes)

        print(f"Accuracy: {accuracy}")
        print(f"Classification Report:\n{report}")

        cm = confusion_matrix(y_test_classes, y_pred_classes)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title('Confusion Matrix')
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.show()

    def save_model(self, path):
        self.model.save(path)

