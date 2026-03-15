# ==============================
# YouTube Revenue Prediction App
# ==============================

import streamlit as st
import pandas as pd
import pickle

# ------------------------------
# Load Model
# ------------------------------
model = pickle.load(open("revenue_model.pkl", "rb"))

# ------------------------------
# App Title
# ------------------------------
st.title("YouTube Ad Revenue Prediction")

st.write("Predict the estimated YouTube advertisement revenue based on video performance metrics.")

st.divider()

# ------------------------------
# User Inputs
# ------------------------------

views = st.number_input("Views", min_value=0)

likes = st.number_input("Likes", min_value=0)

comments = st.number_input("Comments", min_value=0)

watch_time = st.number_input("Watch Time (minutes)", min_value=0)

video_length = st.number_input("Video Length (minutes)", min_value=0)

subscribers = st.number_input("Channel Subscribers", min_value=0)

category = st.selectbox(
    "Video Category",
    ["Entertainment","Music","Gaming","Education","Sports","Technology"]
)

device = st.selectbox(
    "Device Type",
    ["Mobile","Desktop","Tablet"]
)

country = st.selectbox(
    "Audience Country",
    ["India","USA","UK","Canada","Australia"]
)

month = st.slider("Upload Month",1,12)

day = st.slider("Upload Day",1,31)

# ------------------------------
# Feature Engineering
# ------------------------------

if views == 0:
    engagement_rate = 0
else:
    engagement_rate = (likes + comments) / views

# ------------------------------
# Prediction Button
# ------------------------------

if st.button("Predict Revenue"):

    input_data = pd.DataFrame({
        "views":[views],
        "likes":[likes],
        "comments":[comments],
        "watch_time_minutes":[watch_time],
        "video_length_minutes":[video_length],
        "subscribers":[subscribers],
        "engagement_rate":[engagement_rate],
        "month":[month],
        "day":[day],
        "category":[category],
        "device":[device],
        "country":[country]
    })

    prediction = model.predict(input_data)

    st.success(f"Estimated Ad Revenue: ${prediction[0]:.2f}")
