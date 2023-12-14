


# Stutter Detection Project

## Overview

This project aims to detect and classify various types of stuttering patterns in speech using machine learning. It utilizes a Long Short-Term Memory (LSTM) neural network for multi-class classification and provides a user interface for stutter detection.

## Project Structure

### 1. Data Handling (Class)

- **File:** `Data_Handler.py`
- **Purpose:** Manages loading, preprocessing, and scaling of the dataset.
- **Example Usage:**
  ```python
  data_handler = DataHandler('data/SEP-28k_labels_updated.csv', 'data/mfcc_features_new_1.csv')
  data_handler.load_data()
  data_handler.preprocess_data()
  ```

### 2. Model Management (Class)

- **File:** `Model_Manager.py`
- **Purpose:** Manages the LSTM model, including construction, training, evaluation, and saving.
- **Example Usage:**
  ```python
  input_shape = (1, 128)  # Modify based on actual input data shape
  model_manager = ModelManager(input_shape=input_shape, number_of_classes=y_train.shape[1])
  model_manager.train_model(X_train_scaled, y_train, X_test_scaled, y_test)
  ```

### 3. Stutter Feature Extraction(Class)

- **File:** `features.py`
- **Purpose:** Extracts MFCC features and predicts stutter types using the trained LSTM model.
- **Example Usage:**
  ```python
  stutter_extractor = StutterFeatureExtractor(model_path, scaler_path)
  predicted_class = stutter_extractor.predict_stutter_type(audio_file_path)
  ```

### 4. User Interface(Class)

- **File:** `stutter_detection_app_multimodel.py`
- **Purpose:** Kivy-based GUI for selecting an audio file and detecting stuttering.
- **Example Usage:**
  ```python
  if __name__ == '__main__':
      StutterDetectionApp().run()
  ```

### 5. Model Training(Class)

- **File:** `lstm_test_code_multiclass.ipynb`
- **Purpose:** Jupyter Notebook containing the code for training the LSTM model.
- **Dataset Used:** `data/mfcc_features_new_1.csv` for feature extraction.

## Requirements

- Install dependencies: `pip install -r requirements.txt`.

## How to Run

1. Install required dependencies.
2. Run the main script: `python stutter_detection_app_multimodel.py`.

## Additional Information

Explore `stutter_info` in `stutter_detection_app_multimodel.py` for detailed explanations of stutter types, therapy suggestions, and related resources.

## License

This project is licensed under the [MIT License](LICENSE).
```

