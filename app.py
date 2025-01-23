import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import time
from io import BytesIO
import requests

# Load the trained model
MODEL_PATH = 'skin_disease_model.h5'
model = load_model(MODEL_PATH)

# Define the label map and refined descriptions
label_map = {
    0: 'Pigmented Benign Keratosis',
    1: 'Melanoma',
    2: 'Vascular Lesion',
    3: 'Actinic Keratosis',
    4: 'Squamous Cell Carcinoma',
    5: 'Basal Cell Carcinoma',
    6: 'Seborrheic Keratosis',
    7: 'Dermatofibroma',
    8: 'Nevus'
}

disease_info = {
    'Pigmented Benign Keratosis': (
        "Pigmented benign keratosis is a non-cancerous skin lesion that often appears as brown or black spots. "
        "It is harmless but may resemble melanoma, requiring evaluation to rule out malignancy."
    ),
    'Melanoma': (
        "Melanoma is a serious form of skin cancer that originates in melanocytes, the pigment-producing cells. "
        "It is aggressive and can spread rapidly, but early detection and treatment greatly improve outcomes."
    ),
    'Vascular Lesion': (
        "Vascular lesions are abnormalities of blood vessels that may appear as red or purple marks on the skin. "
        "They are typically benign and include conditions like hemangiomas and spider veins."
    ),
    'Actinic Keratosis': (
        "Actinic keratosis is a rough, scaly patch caused by long-term sun exposure. "
        "It is considered precancerous and can potentially develop into squamous cell carcinoma if untreated."
    ),
    'Squamous Cell Carcinoma': (
        "Squamous cell carcinoma is a common skin cancer arising from the squamous cells of the epidermis. "
        "It often presents as a persistent sore or scaly red patch, particularly in sun-exposed areas."
    ),
    'Basal Cell Carcinoma': (
        "Basal cell carcinoma is the most common type of skin cancer, typically appearing as a pearly or translucent bump. "
        "While it grows slowly and rarely spreads, prompt treatment is necessary to prevent deeper tissue damage."
    ),
    'Seborrheic Keratosis': (
        "Seborrheic keratosis is a benign skin growth with a waxy or scaly appearance. "
        "These lesions are harmless and commonly appear with aging, requiring no treatment unless symptomatic."
    ),
    'Dermatofibroma': (
        "Dermatofibroma is a benign, fibrous nodule often found on the lower legs. "
        "It is firm and slightly raised, usually painless, and requires no treatment unless for cosmetic reasons."
    ),
    'Nevus': (
        "A nevus, or mole, is a benign growth of melanocytes. "
        "While most moles are harmless, changes in size, shape, or color should be evaluated to rule out melanoma."
    )
}

# Streamlit app
def main():
    st.set_page_config(
        page_title="Skin Disease Classifier",
        page_icon="🩺",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    # Custom CSS for enhanced styling
    st.markdown(
        """
        <style>
        body {
            background-color: #f8f9fa;
            font-family: 'Segoe UI', sans-serif;
        }
        .stButton button {
            background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
            color: white;
            border-radius: 12px;
            padding: 10px 20px;
            font-size: 18px;
            font-weight: bold;
            border: none;
            transition: all 0.3s ease;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .stButton button:hover {
            background: linear-gradient(90deg, #2575fc 0%, #6a11cb 100%);
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("🩺 Skin Disease Classification Dashboard")
    st.markdown("Upload an image of your skin lesion or provide an image URL to classify it.")

    st.sidebar.header("Upload or Provide URL")

    # Option to upload or input URL
    uploaded_file = st.sidebar.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    image_url = st.sidebar.text_input("Or enter an image URL")

    if image_url:
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            st.image(img, caption="Fetched Image from URL", use_container_width=True)
        except Exception as e:
            st.error("Failed to fetch the image from the provided URL. Please check the URL.")
            img = None
    elif uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    else:
        img = None

    if img and st.button("📊 Predict Skin Disease"):
        with st.spinner("Analyzing..."):
            start_time = time.time()

            # Load the image and preprocess it
            img_resized = image.img_to_array(img)
            img = image.smart_resize(img_resized, (75, 100))  # Maintain current logic
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)

            # Normalize the image as per the training data preprocessing
            img_array = (img_array - np.mean(img_array)) / np.std(img_array)

            predictions = model.predict(img_array)
            predicted_class = np.argmax(predictions, axis=1)

            # Map the predicted class index to the class label
            predicted_label = label_map[predicted_class[0]]
            confidence = predictions[0][predicted_class] * 100

            end_time = time.time()

            st.success(f"🩻 **Prediction:** {predicted_label}")
            st.write(f"📊 **Confidence:** {confidence[0]:.2f}%")
            st.markdown(f"📖 **About {predicted_label}:** {disease_info[predicted_label]}")
            st.write(f"🕒 **Prediction Time:** {end_time - start_time:.2f} seconds")
    else:
        st.info("Please upload an image or provide a URL to start the prediction.")

    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; font-size: 14px;'>
        <b>Empowering healthcare through technology.</b>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
