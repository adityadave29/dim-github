import cv2
import pytesseract
import pyttsx3
import sys

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
while True:
    cam = cv2.VideoCapture(0)
    while True:
        ret, img = cam.read()
        cv2.imshow("Test", img)

        if not ret:
            break

        k = cv2.waitKey(1)

        if k % 256 == 32:
            # For Space key
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

# sys.exit()  # Add this line to exit the code
