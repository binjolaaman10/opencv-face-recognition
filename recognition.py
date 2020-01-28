#! Python3

"""
Python-based face recognition program
made using openCV and NumPy on Python 3.7
18th January 2020
"""

import cv2
import ctypes

print("This program is going to detect faces in images or live videos")

# saving screensize of user to output images in correct resolution irregardless of screensize.
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# openCV's "haarcascade_frontalface_default.xml" contains data of various faces.
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


img = cv2.imread("woman-wearing-blue-top-standing-in-front-of-yellow-balloons-3533228.jpg", 1)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor=1.3,
                                      minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), ((x + w), (y + h)), (0, 0, 255), 3)

print(faces)

resized = cv2.resize(img, (int(img.shape[1] / 3), int(img.shape[0] / 3)))

cv2.imshow("sample", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
