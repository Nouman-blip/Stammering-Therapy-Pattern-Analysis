# Stutter Detection Project

## Overview

This project aims to detect and classify stuttering patterns in speech using machine learning techniques. The system utilizes a Long Short-Term Memory (LSTM) neural network for multi-class classification of different types of stuttering.

## Project Structure

The project is organized into several key components:

### 1. Data Handling (OOP)

- **File:** `Data_Handler.py`
- **OOP Usage:** The `DataHandler` class is responsible for loading, preprocessing, and scaling the dataset.
- **Example:**
  ```python
  class DataHandler:
      # ... (class definition)

  # Example Usage
  data_handler = DataHandler('data/SEP-28k_labels_updated.csv', 'data/mfcc_features_new_1.csv')
  data_handler.load_data()
  data_handler.preprocess_data()
2. Model Management (OOP)
File: Model_Manager.py
OOP Usage: The ModelManager class manages the LSTM model, including construction, training, evaluation, and saving.

class ModelManager:
    # ... (class definition)

# Example Usage
input_shape = (1, 128)  # Modify this based on your actual input data shape
model_manager = ModelManager(input_shape=input_shape, number_of_classes=y_train.shape[1])
model_manager.train_model(X_train_scaled, y_train, X_test_scaled, y_test)

3. Stutter Feature Extraction
File: features.py
OOP Usage: The StutterFeatureExtractor class extracts MFCC features and predicts stutter types using the trained LSTM model.
Example:
python
Copy code
class StutterFeatureExtractor:
    # ... (class definition)

# Example Usage
stutter_extractor = StutterFeatureExtractor(model_path, scaler_path)
predicted_class = stutter_extractor.predict_stutter_type(audio_file_path)
4. User Interface
File: stutter_detection_app_multimodel.py
Overview: This script contains a simple Kivy-based GUI for selecting an audio file and detecting stuttering.
Example:
python
Copy code
class StutterDetectionApp(App):
    # ... (class definition)

# Example Usage
if __name__ == '__main__':
    StutterDetectionApp().run()
Requirements
The project requires the following Python libraries. You can install them using the provided requirements.txt file:

ipykernel==6.25.2
ipython==8.12.3
jupyter-client==8.3.1
jupyter-core==5.3.2
matplotlib==3.7.3
numpy==1.24.3
tensorflow==2.9.1
tqdm
transformers
How to Run
Install the required dependencies using pip install -r requirements.txt.
Run the main script: python stutter_detection_app_multimodel.py.
Feel free to explore and contribute to the project!



This README provides a structured explanation of the project.
