# 🖼️ Face Recognition using Trained Images

This Python project is designed to perform face recognition by training a model on a set of images and then verifying if a given test image matches any of the trained images. The project utilizes the DeepFace library for face recognition tasks.

## 📜 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [License](#license)

## 🛠️ Installation

1. Clone the repository or download the project files.
2. Install the required dependencies by running the following command:

    ```bash
    pip install deepface
    ```

## 🚀 Usage

1. Place all the images you want to use for training the model in a folder named `TrainedImage` within the project directory.
2. Open the `main.py` file and locate the following line:

    ```python
    result = DeepFace.verify("<IMAGE_WHICH_HAS_TO_BE_MATCHED>", f"TrainedImage/{file}")
    ```

    Replace `<IMAGE_WHICH_HAS_TO_BE_MATCHED>` with the path to the image you want to test against the trained images. For example:

    ```python
    result = DeepFace.verify("test_image.jpg", f"TrainedImage/{file}")
    ```

3. Run the `main.py` script.

   The script will iterate through all the images in the `TrainedImage` folder and compare them with the test image. It will print the name of the person if an exact match is found, or the closest match if no exact match is found.

## 📁 Project Structure

- `main.py`: The main script that performs face recognition.
- `TrainedImage/`: A folder containing images used for training the model.

## ✨ Features

- Train a face recognition model using a set of images.
- Verify if a given test image matches any of the trained images.
- Identify the closest match if no exact match is found.
- User-friendly output displaying the match results.

## 📝 License

This project is open-source and licensed under the MIT License. Feel free to use, modify, and distribute the code as per the terms of the license.

