import cv2
import pytesseract
import pyttsx3

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
count = 0
cam = cv2.VideoCapture(0)

import pyttsx3
engine= pyttsx3.init()

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

    # engine.setProperty('rate',70)
    # voices=engine.getProperty('voices')
    # cnt=0
    # for voice in voices:
    #     if(cnt==2):
    #         print ("Using voice:"), repr(voice)
    #         engine.setProperty('voice',voice.id)
    #         engine.say("jineet the gian")
    #         exit()
    #     cnt=cnt+1
    # engine.runAndWait()
    
    import os

    def text_to_speech(text):
        cmd = f'espeak "{text}"'
        os.system(cmd)

    text = "Hello, this is a test for text to speech conversion."
    text_to_speech(text)
    cv2.waitKey(5)
    print("Asking for new image no: ", count)


