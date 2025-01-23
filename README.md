# Skin Disease Classification with Deep Learning

![banner](https://github.com/user-attachments/assets/0e530f55-14fb-4413-8c52-dbcb88a99e6e)


## Project Overview
This repository contains the implementation of skin disease classification using **Convolutional Neural Networks (CNN)** and **DenseNet201**. The project leverages deep learning techniques to accurately classify malignant and benign skin diseases based on images from **The International Skin Imaging Collaboration (ISIC)** dataset.

## Dataset
The dataset consists of **2,357 images** of various skin conditions, including:
- Actinic Keratosis  
- Basal Cell Carcinoma  
- Dermatofibroma  
- Melanoma  
- Nevus  
- Pigmented Benign Keratosis  
- Seborrheic Keratosis  
- Squamous Cell Carcinoma  
- Vascular Lesion  

For more details, visit the dataset source: [Skin Cancer 9 Classes (ISIC) Dataset](https://www.kaggle.com/datasets/nodoubttome/skin-cancer9-classesisic)

## Project Files
- **app.py**: Streamlit dashboard for interactive visualization and real-time prediction of skin diseases.
- **cnn_densenet_model.ipynb**: Jupyter Notebook for building and training the CNN with DenseNet201 model.
- **data_preprocessing.py**: Code for data loading, augmentation, and preprocessing.
- **requirements.txt**: Necessary dependencies for running the project.
- **README.md**: This file.

## Installation
To set up the environment:
```bash
git clone https://github.com/yourusername/skin-disease-classification.git
cd skin-disease-classification
pip install -r requirements.txt
