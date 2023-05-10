import cv2
import pytesseract
import pyttsx3

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
count = 0
cam = cv2.VideoCapture(0)

while True:
    print("Hello")
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
            print("Image " + str(count) + " saved")
            file = '/home/pi/dim-github/img' + str(count) + '.jpg'
            cv2.imwrite(file, img)
            count += 1

    # Move these lines outside of the inner while loop
    cam.release()
    cv2.destroyAllWindows()

    img = cv2.imread('img' + str(count - 1) + '.jpg')
    if img is not None and img.size[0] > 0 and img.size[1] > 0:
        cv2.imshow('sample img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    text = pytesseract.image_to_string(img)
    print(text)

    def speak(text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Speed of speech
        engine.say(text)
        engine.runAndWait()
    speak(text)

    print("Asking for new image no: ", count)
