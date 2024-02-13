import streamlit as st
import pickle
import numpy as np

def predict_stress_level(model, input_values):
    prediction = model.predict(input_values.reshape(1, -1))
    stress_level = int(np.round(prediction[0])) % 5
    return stress_level

st.title("HUMAN STRESS DETECTION")

snoring_rate = st.text_input("Snoring Rate")
respiration_rate = st.text_input("Respiration Rate")
body_temperature = st.text_input("Body Temperature")
limb_movement = st.text_input("Limb Movement")
blood_oxygen = st.text_input("Blood Oxygen")
eye_movement = st.text_input("Eye Movement")
sleeping_hours = st.text_input("Sleeping Hours")
heart_rate = st.text_input("Heart Rate")

submit_button = st.button("Submit")

with open('SAYO.pickle', 'rb') as f:
    model = pickle.load(f)

if submit_button:
    try:
        input_values = np.array([float(snoring_rate), float(respiration_rate), float(body_temperature),
                                 float(limb_movement), float(blood_oxygen), float(eye_movement),
                                 float(sleeping_hours), float(heart_rate)])

        stress_level_prediction = predict_stress_level(model, input_values)

        if stress_level_prediction is not None:
            st.write("Stress Level Prediction:", stress_level_prediction)
    except ValueError:
        st.error("Invalid input. Please enter numeric values.")
