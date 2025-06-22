# frontend/app.py
import streamlit as st
import requests

st.title("🌸 Iris Flower Prediction App")
st.markdown("Enter 4 features separated by commas (e.g. `5.1, 3.5, 1.4, 0.2`)")

user_input = st.text_input("Input Features")

if st.button("Predict"):
    try:
        features = [float(i.strip()) for i in user_input.split(",")]
        if len(features) != 4:
            st.error("Please enter exactly 4 numbers.")
        else:
            res = requests.post("https://your-api-url.onrailway.app/predict", json={"features": features})
            st.success(f"🌼 Predicted Class: {res.json()['prediction']}")
    except Exception as e:
        st.error(f"Invalid input: {e}")
