**Human Multiple Disease Recognition**
This project aims to recognize and predict multiple human diseases using Machine Learning (ML) and Deep Learning techniques. 
The diseases covered include Heart Disease, Pneumonia, Diabetes, and Malaria. The system leverages Python, a pre-trained VGG16 
model for image-based disease recognition, and a Tkinter-based graphical user interface (GUI).

Table of Contents
Features
Requirements
Installation
Usage
Model Training
Data Preparation
File Structure
Credits
License


Features
Heart Disease Prediction: Binary classification (yes/no) based on clinical data.
Pneumonia Detection: Image-based detection using chest X-rays.
Diabetes Prediction: Binary classification (yes/no) based on clinical data.
Malaria Detection: Image-based detection using blood smear images.
User-friendly GUI: Simple and intuitive interface built with Tkinter.


Requirements
Python 3.6+
TensorFlow
Keras
scikit-learn
pandas
numpy
matplotlib
customtkinter
Tkinter (usually comes pre-installed with Python)


Installation
Clone the repository:

bash
Copy code
git clone https://github.com/pyare00/Human-Multiple-Disease-Recognition.git
cd Myproject

Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install the required packages:

pip install requirements


Usage:
Run the application
python main.py


Interact with the GUI:

Load images for pneumonia and malaria detection.
Enter clinical data for heart disease and diabetes prediction.
Click on the respective buttons to get predictions.
Model Training
Heart Disease and Diabetes


Prepare the dataset/Train the model:
  No need to do this as already trained and saved the model.(formats: .joblib ,.h5)
  If you want to do your own training just look at script file(.ipynb ,.py)


Prepare the dataset:
Ensure your images are organized in directories for each class as it is in sample uploaded. Given dataset is just sample not that was used originally.
if you want to train the model again use use either your own dataset or refer some other sources like Kaggle, etc.


File Structure
  Keep it as it is uploaded in repository
MyProject/
│
├── project/
│   ├── heart_disease.csv
│   ├── diabetes.csv
│   ├── pneumonia/
│   │   ├── train/
│   │   └── test/
│   └── malaria/
│       ├── train/
│       └── test/
│
├── 
│   ├── heart_disease_model.h5
│   ├── diabetes_model.h5
│   ├── pneumonia_model.h5
│   └── malaria_model.h5
│
├── scripts/
│   ├── train_heart_disease.py
│   ├── train_diabetes.py
│   ├── train_pneumonia.py
│   └── train_malaria.py
│
├── main.py
├── gui.py
├── utils.py
├── all Images directly
└── 
├── Data/
    ..............
    ..............

    
Credits
This project utilizes the VGG16 model, a well-known convolutional neural network, and several datasets for training and validation purposes. 
Acknowledgements to the creators and maintainers of these resources.
