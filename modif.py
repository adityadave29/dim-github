import cv2
import pytesseract
import pyttsx3

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    cv2.imshow("Test", img)

    if not ret:
        break

cam.release()
cv2.destroyAllWindows()

img = cv2.imread('img.jpg')
cv2.imshow('sample img', img)

# Wait for a fixed time (e.g., 5 seconds) before closing the window
cv2.waitKey(5000)
cv2.destroyAllWindows()

text = pytesseract.image_to_string(img)
print(text)

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.say(text)
    engine.runAndWait()

speak(text)