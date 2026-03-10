import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model
model = load_model("model.h5")

# Load tokenizer
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Load label encoder
with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

max_length = 100


# Function to calculate stress score
def calculate_stress(emotion, confidence):

    stress_map = {
        "joy": 10,
        "happy": 10,
        "neutral": 30,
        "sadness": 70,
        "fear": 80,
        "anger": 90
    }

    base = stress_map.get(emotion, 30)

    score = base * confidence

    return round(score,2)


# Streamlit UI
st.title("🧠 Multi-Language Emotion & Stress Detector")

st.write("You can enter text in **English, Hindi, or Gujarati**.")

user_input = st.text_area(
    "Enter Text",
    placeholder="Example: I feel very happy today / मुझे आज बहुत अच्छा लग रहा है / આજે મને બહુ સારું લાગે છે"
)


if st.button("Predict"):

    if user_input.strip() != "":

        seq = tokenizer.texts_to_sequences([user_input])
        padded = pad_sequences(seq, maxlen=max_length)

        prediction = model.predict(padded)

        confidence = float(np.max(prediction))

        emotion = le.inverse_transform([np.argmax(prediction)])[0]

        # Stress score
        stress_score = calculate_stress(emotion, confidence)

        # Stress level
        if stress_score < 30:
            stress_level = "Low Stress 😊"
        elif stress_score < 60:
            stress_level = "Medium Stress 😐"
        else:
            stress_level = "High Stress 😟"

        st.subheader("Prediction Result")

        st.write(f"**Emotion:** {emotion}")

        st.write(f"**Confidence:** {round(confidence*100,2)} %")

        st.write(f"**Stress Score:** {stress_score}")

        st.write(f"**Stress Level:** {stress_level}")

    else:
        st.warning("Please enter some text.")