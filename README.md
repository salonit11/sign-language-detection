# Sign Language Detection

This project demonstrates how to detect sign language alphabets using a webcam. The system captures frames from the webcam, processes them to create a custom dataset, trains a model using Random Forest, and tests the model in real-time using webcam input. The model achieves 100% accuracy on trained gestures (A, B, and L) but can be extended to detect custom hand gestures as well.

---

## Project Overview

1. **Data Collection**:
   - The system first captures images of hand gestures using the `collect_imgs.py` script.
   - It processes the captured frames to extract hand landmarks using **MediaPipe** and stores them for further use.

2. **Dataset Creation**:
   - After capturing the hand gesture images, the `create_dataset.py` script generates the dataset from the saved images.
   - The dataset consists of the X and Y coordinates of hand landmarks, which are used to train the model.

3. **Model Training**:
   - The dataset is used to train a **Random Forest classifier**.
   - The model achieves 100% accuracy on the gestures (A, B, and L), but it can be extended to train on custom hand gestures.

4. **Testing**:
   - The trained model is used for real-time predictions from the webcam.
   - The system will predict the sign language alphabet based on the hand gesture shown in front of the webcam.

5. **Customizable**:
   - The system can easily be customized for detecting custom hand gestures. New gestures can be added by capturing more images and retraining the model.

---

## Requirements

- **Python 3.x**
- **OpenCV**: For webcam access and image manipulation.
- **MediaPipe**: For hand tracking and landmark detection.
- **NumPy**: For numerical operations.
- **scikit-learn**: For training the Random Forest model.
- **Pickle**: For saving and loading the trained model.

You can install the required libraries using the following command:

```bash
pip install opencv-python mediapipe numpy scikit-learn
```

---

## How It Works

1. **Data Collection**:
   - The `collect_imgs.py` script captures hand gestures using the webcam.
   - It detects hand landmarks using **MediaPipe** and stores the hand gestures as image files with corresponding labels.

2. **Dataset Creation**:
   - The `create_dataset.py` script reads the captured images and extracts the hand landmarks (X, Y coordinates).
   - The data is labeled based on the hand gestures and saved into a dataset for training.

3. **Training the Model**:
   - The dataset is used to train a **Random Forest classifier**.
   - The model is saved as `model.p` for future use.

4. **Testing with Webcam**:
   - The webcam is used to predict the gesture in real-time by processing the live feed and feeding the frame to the trained model.
   - The model's predictions are displayed on the frame with a bounding box around the hand and the predicted alphabet.

---

## Running the Project

### Step 1: Capture Hand Gestures

Run the following script to capture hand gestures:

```bash
python collect_imgs.py
```

This script will:
- Capture data from the webcam.
- Detect hand landmarks using MediaPipe.
- Save the captured images with appropriate labels.

### Step 2: Create the Dataset

After collecting the images, run the following script to create the dataset:

```bash
python create_dataset.py
```

This script will:
- Read the captured images.
- Extract the hand landmarks (X and Y coordinates).
- Create a dataset for training.

### Step 3: Train the Model

Once the dataset is created, you can train the model using the dataset:

```bash
python train_classifier.py  # It also trains the model here
```

This script will:
- Train the model on the collected dataset.
- Save the trained model as `model.p`.

### Step 4: Real-time Testing Using Webcam

After training the model, you can test it using real-time webcam input:

```bash
python inference_classifier.py
```

This script will:
- Load the trained model (`model.p`).
- Continuously capture webcam frames.
- Predict the hand gesture being shown.
- Display the predicted alphabet on the frame.

---

## Customizing for Other Gestures

To train the model on custom hand gestures, follow these steps:

1. **Add New Labels**:
   - Add new gestures (hand signs) by updating the `labels_dict` in the `inference_classifier.py` file and increment the number_of_classes variable in collect_imgs.py. For example:
     ```python
     labels_dict = {0: 'A', 1: 'B', 2: 'L', 3: 'C', 4: 'D'}
     ```

2. **Capture New Data**:
   - Run the `collect_imgs.py` script again to capture new gestures in front of the webcam. Ensure each gesture is mapped to a new label.

3. **Re-train the Model**:
   - After capturing the new data, re-run the `create_dataset.py` script to generate the new dataset and retrain the model.

---

## Project Structure

```bash
|-- collect_imgs.py          # Script to collect hand gesture images
|-- data(folder)            # Folder containing data for all gestures
|-- create_dataset.py       # Script to create dataset
|-- train_classifier.py     # Script to train model
|-- inference_classifier.py  # Script to test the model using webcam
|-- model.p                  # Trained Random Forest model (saved)
|-- README.md                # Project overview and instructions
```

---

## Acknowledgments

- **MediaPipe**: Used for hand tracking and landmark detection.
- **OpenCV**: Used for accessing the webcam and image manipulation.
- **scikit-learn**: Used for training the Random Forest classifier.

---

Feel free to modify the project and add more gestures. If you encounter any issues or have suggestions, please open an issue in the repository.
