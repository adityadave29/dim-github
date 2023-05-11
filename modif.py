# import cv2
# import pytesseract
# import pyttsx3

# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
# cam = cv2.VideoCapture(0)
# while True:
#     ret, img = cam.read()
#     cv2.imshow("Test", img)

#     if not ret:
#         break

#     k = cv2.waitKey(1)

#     if k % 256 == 32:
#         # For Space key
#         print("Image saved")
#         file = '/home/pi/dim-github/img.jpg'
#         cv2.imwrite(file, img)
#         print("Close")
#         break

# cam.release()
# cv2.destroyAllWindows()

# img = cv2.imread('img.jpg')
# # cv2.imshow('sample img', img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# text = pytesseract.image_to_string(img)
# print(text)

# def speak(text):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)  # Speed of speech
#     engine.say(text)
#     engine.runAndWait()
# speak(text)

import cv2
import pytesseract
import pyttsx3
import RPi.GPIO as GPIO

# Set up GPIO
button_pin = 18  # GPIO pin number for the button
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    cv2.imshow("Test", img)

    if not ret:
        break

    button_state = GPIO.input(button_pin)

    if button_state == GPIO.LOW:
        # Button pressed
        print("Image saved")
        file = '/home/pi/dim-github/img.jpg'
        cv2.imwrite(file, img)
        print("Close")
        break

cam.release()
cv2.destroyAllWindows()

img = cv2.imread('img.jpg')
text = pytesseract.image_to_string(img)
print(text)

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.say(text)
    engine.runAndWait()

speak(text)
