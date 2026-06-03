import streamlit as st
import pandas as pd
import joblib

# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="YouTube Performance Predictor",
    layout="wide"
)

# ==========================
# Title
# ==========================
st.title("📺 YouTube Performance Predictor")
st.write(
    "Enter video details to predict expected views using the trained ML model."
)

# ==========================
# Load Model
# ==========================
try:
    model = joblib.load("youtube_RandomForest_Regressor_Model.pkl")
except Exception:
    st.error(
        "❌ Model file not found! Make sure the model file is in the same folder."
    )
    st.stop()

# ==========================
# Encoding Maps
# ==========================
category_map = {
    "Education": 0,
    "Music": 1,
    "Gaming": 2,
    "Entertainment": 3,
    "Sports": 4
}

language_map = {
    "English": 0,
    "Arabic": 1,
    "Hindi": 2,
    "Urdu": 3
}

# ==========================
# Input Section
# ==========================
st.header("🎬 Video Details")

col1, col2 = st.columns(2)

with col1:
    category = st.selectbox(
        "Video Category",
        list(category_map.keys())
    )

    language = st.selectbox(
        "Language",
        list(language_map.keys())
    )

    duration = st.number_input(
        "Video Duration (Seconds)",
        min_value=1,
        value=60,
        step=1
    )

    sentiment = st.slider(
        "Sentiment Score",
        min_value=-1.0,
        max_value=1.0,
        value=0.0,
        step=0.01
    )

with col2:
    likes = st.number_input(
        "Expected Likes",
        min_value=0,
        value=100,
        step=1
    )

    comments = st.number_input(
        "Expected Comments",
        min_value=0,
        value=10,
        step=1
    )

    shares = st.number_input(
        "Expected Shares",
        min_value=0,
        value=5,
        step=1
    )

# ==========================
# Predict Button
# ==========================
if st.button("🚀 Predict Performance"):

    # ==========================
    # Feature Engineering
    # ==========================
    engagement = likes + comments + shares

    if engagement == 0:
        like_ratio = 0
        comment_ratio = 0
        share_ratio = 0
    else:
        like_ratio = likes / engagement
        comment_ratio = comments / engagement
        share_ratio = shares / engagement

    # ==========================
    # Calculated Metrics
    # ==========================
    st.subheader("📊 Calculated Metrics")

    st.write(f"Total Engagement: {engagement}")
    st.write(f"Like Ratio: {like_ratio:.3f}")
    st.write(f"Comment Ratio: {comment_ratio:.3f}")
    st.write(f"Share Ratio: {share_ratio:.3f}")

    # ==========================
    # Prepare Input Data
    # ==========================
    input_data = pd.DataFrame([[
        category_map[category],
        language_map[language],
        duration,
        likes,
        comments,
        shares,
        sentiment,
        engagement,
        like_ratio,
        comment_ratio,
        share_ratio
    ]])

    # ==========================
    # Prediction
    # ==========================
    try:
        prediction = model.predict(input_data)[0]

        st.success("✅ Prediction Generated!")

        st.subheader("📈 Prediction Result")

        st.metric(
            label="Predicted Views",
            value=f"{int(prediction):,}"
        )

        # ==========================
        # Performance Level
        # ==========================
        if prediction > 100000:
            level = "🔥 High Performance"

        elif prediction > 30000:
            level = "⚡ Medium Performance"

        else:
            level = "📉 Low Performance"

        st.write(f"Performance Level: {level}")

    except Exception as e:
        st.error(f"Prediction Error: {e}")
