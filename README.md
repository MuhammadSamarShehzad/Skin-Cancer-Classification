# Skin Disease Classification Using Deep Learning

![banner](https://github.com/user-attachments/assets/0e530f55-14fb-4413-8c52-dbcb88a99e6e)

---

## 🚀 Overview
This project presents a deep learning-based solution for **Skin Disease Classification** using **Convolutional Neural Networks (CNN)**, specifically the **DenseNet201** architecture. The model distinguishes between **benign** and **malignant** skin conditions, trained on the **ISIC (International Skin Imaging Collaboration)** dataset.

---

## 📂 Dataset
The dataset consists of **2,357 dermoscopic images** across the following 9 skin disease classes:

- Actinic Keratosis
- Basal Cell Carcinoma
- Dermatofibroma
- Melanoma
- Nevus
- Pigmented Benign Keratosis
- Seborrheic Keratosis
- Squamous Cell Carcinoma
- Vascular Lesion

**Source:** [Kaggle - Skin Cancer 9 Classes (ISIC)](https://www.kaggle.com/datasets/nodoubttome/skin-cancer9-classesisic)

---

## 📁 Directory Structure
```
.
├── app.py                                # Streamlit web app for predictions
├── skin_disease_model.h5                 # Pretrained DenseNet201 model
├── requirements.txt                      # Dependency list
├── Dockerfile                            # Docker setup for deployment
├── README.md                             # Project documentation
└── skin-disease-my-own-prepared.ipynb    # Model training and evaluation notebook
```

---

## 🐳 Docker Deployment
Run the application in a Docker container:

### Step 1: Build the Docker image
```bash
docker build -t skin_disease_classification .
```

### Step 2: Run the Docker container
```bash
docker run -p 8501:8501 skin_disease_classification
```

Visit **http://localhost:8501** in your browser.

---

## 🎯 Key Features
- **User-friendly Streamlit interface** for image upload and prediction
- **Accurate classification** using DenseNet201
- **Fully containerized** setup for portability and deployment ease

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgments
- **ISIC** for providing the medical image dataset
- **TensorFlow** and **Keras** for deep learning support
