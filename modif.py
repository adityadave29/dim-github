import cv2
import pytesseract
import pyttsx3
from gpiozero import Button

def capture_image():
    cam = cv2.VideoCapture(0)
    while True:
        ret, img = cam.read()
        cv2.imshow("Test", img)

        if not ret:
            break

        else:
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

    speak(text)

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.say(text)
    engine.runAndWait()

# Set up the GPIO button and callback function
button = Button(18)  # Replace 17 with the GPIO pin number you are using
button.when_pressed = capture_image

# Keep the script running
while True:
    pass
