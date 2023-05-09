import cv2
import pytesseract
from gtts import gTTS
import os

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
            print("Image " + str(count) + "saved")
            file = '/home/pi/dim-github/img' + str(count) + '.jpg'
            cv2.imwrite(file, img)
            count += 1

    cam.release()
    cv2.destroyAllWindows()

    img = cv2.imread('img' + str(count - 1) + '.jpg')
    cv2.imshow('sample img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    text = pytesseract.image_to_string(img)
    print(text)

    language = 'en'
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("text_to_speech.mp3")
    os.system("text_to_speech.mp3")

    print("Asking for new image no: ", count)