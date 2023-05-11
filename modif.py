import cv2
import pytesseract
import pyttsx3
import time

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
cam = cv2.VideoCapture(0)

start_time = time.time()
duration = 10  # Duration of the webcam feed in seconds

while time.time() - start_time < duration:
    ret, img = cam.read()
    cv2.imshow("Test", img)

    if not ret:
        break

cam.release()
cv2.destroyAllWindows()

img = cv2.imread('img.jpg')
cv2.imshow('sample img', img)

time.sleep(5)  # Display the sample image for 5 seconds
cv2.destroyAllWindows()

text = pytesseract.image_to_string(img)
print(text)

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.say(text)
    engine.runAndWait()

speak(text)