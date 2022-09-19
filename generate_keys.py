# -- Importing necessary modules

import pickle
import streamlit_authenticator as stauth

# -- Names, Usernames and passwords

names =["lokesh", "prathap", "suchitra", "eswar"]
usernames = ["lokeshkr", "prathap", "suchitra", 'eswar']
passwords =["lokesh123", "prathap123", "suchitra123", "eswar123"]

# -- Hashing the passwords which uses bycrypt

hashed_passwds = stauth.Hasher(passwords).generate()
with open('passwords.pkl', 'wb') as file:
    pickle.dump(hashed_passwds, file)

