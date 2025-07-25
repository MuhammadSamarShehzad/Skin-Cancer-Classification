# Skin Disease Classification with Deep Learning

![banner](https://github.com/user-attachments/assets/0e530f55-14fb-4413-8c52-dbcb88a99e6e)

---

## 🚀 Project Overview
This project implements a **Skin Disease Classification** system using **Convolutional Neural Networks (CNN)** and **DenseNet201**.
It classifies images into malignant or benign categories, leveraging the **ISIC (International Skin Imaging Collaboration)** dataset.

---

## 📂 Dataset
The dataset includes **2,357 dermoscopic images** of the following skin conditions:
- Actinic Keratosis
- Basal Cell Carcinoma
- Dermatofibroma
- Melanoma
- Nevus
- Pigmented Benign Keratosis
- Seborrheic Keratosis
- Squamous Cell Carcinoma
- Vascular Lesion

**Dataset Source:** [Skin Cancer 9 Classes (ISIC) Dataset](https://www.kaggle.com/datasets/nodoubttome/skin-cancer9-classesisic)

---

## 📁 Project Structure
```
.
├── app.py                   # Streamlit app for real-time predictions
├── skin_disease_model.h5    # Trained CNN model
├── requirements.txt         # Python dependencies
├── Dockerfile               # Containerization configuration
├── README.md                # Project documentation
└── skin-disease-my-own-prepared.ipynb  # Model training notebook
```

---

## 🐳 Run with Docker
You can easily containerize and run the app using Docker:

### **Build the Docker image**
```bash
docker build -t skin_disease_classification .
```

### **Run the container**
```bash
docker run -p 8501:8501 skin_disease_classification
```

Once running, open: **http://localhost:8501**

---

## 🎯 Features
- **Interactive Streamlit dashboard** for image upload and real-time predictions.
- **Deep Learning model (DenseNet201)** with high classification accuracy.
- **Dockerized environment** for seamless deployment.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgments
- **ISIC Dataset** for the medical image dataset.
- TensorFlow and Keras for deep learning model development.