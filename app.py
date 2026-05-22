from tensorflow.keras.models import load_model
import pickle

face_model = load_model('models/face_emotion_model.h5')
text_model = pickle.load(open('models/text_emotion_model.pkl','rb'))
vectorizer = pickle.load(open('models/vectorizer.pkl','rb'))
import cv2

cap = cv2.VideoCapture(0)
import streamlit as st

user_text = st.text_input("How are you feeling today?")
X_input = vectorizer.transform([user_text])
text_emotion = text_model.predict(X_input)[0]
final_emotion = text_emotion  # or combine face + text
response = generate_response(final_emotion)
st.write(response)
import pyttsx3

engine = pyttsx3.init()
engine.say(response)
engine.runAndWait()