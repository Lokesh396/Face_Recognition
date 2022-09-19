# -- Importing Necessary Modules

import pickle
import time
import cv2
import face_recognition
from streamlit_autorefresh import st_autorefresh
import data
from data import *
import streamlit as st
import streamlit_authenticator as stauth
from numpy import dot
import numpy as np


# -- Function  when the image matches with image attached to that account

def valid():
    st.success("Login Success")
    st.text_input("UserID", key="id")
    st.number_input("Amount", key="amt")
    out = st.button("Transfer")
    if out:
        st.success("Transaction success")


# -- Function  when the image  doesn't match with image attached to that account


def invalid():
    st.error('Unauthorized Access')
    video.release()
    cv2.destroyAllWindows()
    st.stop()


names = ["lokesh", "prathap", "suchitra", "eswar"]
usernames = ["lokeshkr", "prathap", "suchitra","eswar"]

# -- Loading passwords with was encrypted and stored in the pickle file

with open('passwords.pkl', 'rb') as file:
    hashed_passwords = pickle.load(file)

# -- Configuring page
st.set_page_config(page_title="Banking secure", layout='wide')
st.header("Welcome to Rkv Bank")
authenticator = stauth.Authenticate(names, usernames, hashed_passwords, 'cookie_name', 'signature_key',
                                    cookie_expiry_days=0)
name, authentication_status, username = authenticator.login("Login", "main")
flag = 0

if authentication_status == False:
    st.error("Username/Password is incorrect")

if authentication_status is None:
    st.warning("please enter username and password")

if authentication_status:
    authenticator.logout("Logout", 'sidebar')
    st.sidebar.write(f"Welcome {name}")
    video = cv2.VideoCapture(cv2.CAP_DSHOW)
    result = None
    val = None
    while True:
        ret, frame = video.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        if face_encodings:
            if username == 'lokeshkr':
                result = face_recognition.compare_faces(data.lokeshkr, face_encodings)
                if result[0]:
                    if flag == 0:
                        valid()
                        flag = 1
                else:
                    invalid()

            elif username == 'suchitra':
                result = face_recognition.compare_faces(data.suchitra, face_encodings)
                if result[0]:
                    if flag == 0:
                        valid()
                        flag = 1
                else:
                    invalid()
            elif username == 'eswar':
                result = face_recognition.compare_faces(data.eswar, face_encodings)
                if result[0]:
                    if flag == 0:
                        valid()
                        flag = 1
                else:
                    invalid()
            else:
                result = face_recognition.compare_faces(data.prathap, face_encodings)
                if result[0]:
                    if flag == 0:
                        valid()
                        flag = 1
                else:
                    invalid()

            top, right, bottom, left = face_locations[0][0], face_locations[0][1], face_locations[0][2], \
                                       face_locations[0][3]
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            if result[0]:
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            else:
                cv2.putText(frame, "Unknown", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
