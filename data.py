# -- Importing necessary modules

import face_recognition
import cv2

# -- Loading Images

img = face_recognition.load_image_file('Dataset/loki2.jpg')
img1 = face_recognition.load_image_file('Dataset/suchitra.jpeg')
img2 = face_recognition.load_image_file('Dataset/prathap.jpeg')
img3 = face_recognition.load_image_file('Dataset/eswar1.png')

# -- Converting Images into RGB from BGR

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rgb_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
rgb_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)

# -- Storing all the facial embeddings as list

lokeshkr = face_recognition.face_encodings(rgb_img)[0]
suchitra = face_recognition.face_encodings(rgb_img1)[0]
prathap = face_recognition.face_encodings(rgb_img2)[0]
eswar = face_recognition.face_encodings(rgb_img3)[0]

