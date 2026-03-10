# 🧠 Multi-Language Emotion & Stress Detection System

A **Natural Language Processing (NLP)** project that detects **emotion, stress score, and stress level** from user text input in **English, Hindi, and Gujarati**.

This project uses **Deep Learning (LSTM)** and provides a **Streamlit web interface** for real-time emotion and stress prediction.

---

# 🚀 Features

* 🌍 **Multi-language support**

  * English
  * Hindi
  * Gujarati

* 😊 **Emotion Detection**

  * Joy
  * Sadness
  * Anger
  * Fear
  * Neutral
  * Surprise

* 🧠 **Stress Analysis**

  * Stress Score Prediction
  * Stress Level Classification

    * Low Stress
    * Medium Stress
    * High Stress

* 📊 **Confidence Score Display**

* 💻 **Interactive Streamlit Web App**

---

# 🧠 Project Workflow

1. Data Collection
2. Text Preprocessing
3. Tokenization
4. Sequence Padding
5. Model Training (LSTM)
6. Emotion Prediction
7. Stress Score Calculation
8. Web App Deployment using Streamlit

---

# 🗂 Project Structure

```
emotion-stress-detector
│
├── dataset
│   └── emotion_dataset.csv
│
├── model
│   ├── model.h5
│   ├── tokenizer.pkl
│   └── label_encoder.pkl
│
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Technologies Used

| Technology         | Purpose                |
| ------------------ | ---------------------- |
| Python             | Programming Language   |
| TensorFlow / Keras | Deep Learning          |
| LSTM               | Emotion Classification |
| Pandas / NumPy     | Data Processing        |
| Scikit-Learn       | Label Encoding         |
| Streamlit          | Web Application        |

---

# 📊 Dataset Information

Dataset contains **30,000 multilingual text samples** with the following columns:

| Column       | Description            |
| ------------ | ---------------------- |
| text         | User input text        |
| language     | Language of text       |
| emotion      | Emotion label          |
| stress_level | Stress category        |
| stress_score | Stress intensity score |

Languages supported:

* English
* Hindi
* Gujarati

---

# 🧠 Model Architecture

```
Embedding Layer
       ↓
LSTM Layer (128 units)
       ↓
Dropout Layer
       ↓
Dense Layer
       ↓
Softmax Output Layer
```

Loss Function:

```
Sparse Categorical Crossentropy
```

Optimizer:

```
Adam
```

---

# 💻 Streamlit Web Application

The project includes a **Streamlit interface** where users can input text and receive:

* Detected Emotion
* Confidence Score
* Stress Score
* Stress Level

Example Input:

```
I feel very stressed about my exams
```

Example Output:

```
Emotion: Fear
Confidence: 82%
Stress Score: 68
Stress Level: High Stress
```

---

# ▶️ How to Run the Project

### 1️⃣ Clone Repository

```
git clone https://github.com/urvashi772/emotion-stress-detector.git
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Train the Model

```
python train_model.py
```

---

### 4️⃣ Run Streamlit App

```
streamlit run app.py
```

---

# 📦 Requirements

```
tensorflow
streamlit
pandas
numpy
scikit-learn
pickle
```

---

# 📈 Future Improvements

* BERT-based emotion detection
* Transformer models for higher accuracy
* Voice-based emotion detection
* Mental health recommendation system
* Real-time chatbot integration

---

# 🎯 Applications

* Mental Health Monitoring
* Social Media Sentiment Analysis
* Customer Feedback Analysis
* Stress Detection Systems
* AI-based Wellbeing Tools

---


Please consider giving it a **star ⭐ on GitHub**.
