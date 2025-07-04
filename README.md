# Teachable_machine-Task
# README

Teachable Machine Image Classification Project

This project demonstrates a simple image classification workflow using Google Teachable Machine, TensorFlow, and Google Colab.

Task Description:

- Train an image recognition model using Teachable Machine with two classes: Bananna and Apple.
- Export the trained model in TensorFlow SavedModel format.
- Load and run the model in Google Colab using TFSMLayer (Keras 3).
- Write a Python script to load a test image, preprocess it, run prediction, and display the result.
- Submit the model files, Python script, and a screenshot of the prediction output.

Files Included:

- /model.savedmodel/ — exported SavedModel folder with saved_model.pb and variables/
- a7.jpg — test image to classify
- predict.py — Python script to load the model and predict
- output_screenshot.png — screenshot showing the prediction result

How to Run:

1. Upload the model.savedmodel folder and your test image to Google Colab.
2. Run predict.py or the provided notebook cells.
3. The script loads the model, preprocesses the image, predicts the class, and prints:
   - Raw prediction tensor
   - Predicted class name (Bananna or Apple)

Requirements:

- TensorFlow 2.19+
- Keras 3.x
- Google Colab or local Python environment
- Python 3

Notes:

- The model was trained using Teachable Machine’s web interface.
- Prediction works with TFSMLayer to support the SavedModel in Keras 3.
- Ensure the class names in the script match your training order.

Author: [Abdullah Albar]
Date: [30/6/2025]


