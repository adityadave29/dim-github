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

    k = cv2.waitKey(1)

    if k % 256 == 27:
        # For Esc key
        print("Close")
        break
    elif k % 256 == 32:
        # For Space key
        print("Image saved")
        file = '/home/pi/dim-github/img.jpg'
        cv2.imwrite(file, img)

cam.release()
cv2.destroyAllWindows()

img = cv2.imread('img.jpg')
cv2.imshow('sample img', img)
# cv2.waitKey(0)
cv2.destroyAllWindows()

text = pytesseract.image_to_string(img)
print(text)

# text_speech = pyttsx3.init()
# text_speech.say(text)
# text_speech.runAndWait()
# cv2.waitKey(5)
    
# import os
# os.system('espeak "{}"'.format(text))

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.say(text)
    engine.runAndWait()
speak(text)
