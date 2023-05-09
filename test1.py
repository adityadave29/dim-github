import RPi.GPIO as GPIO
import time
import os
from PIL import Image
from gtts import gTTS
import googletrans as gt
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        os.system('./webcam2.sh')
        message = 'picture is taken'
        language = 'en'
        print(message)
        myobj = gTTS(text=message, lang=language,
                     low=False)
        myobj.save("welcome.mp3")
        os.system("mpg321 welcome.mp3")

    time.sleep(0.2)
