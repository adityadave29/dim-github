# import pyttsx3
# engine= pyttsx3.init()
# engine.setProperty('rate',70)
# voices=engine.getProperty('voices')
# for voice in voices:
#     print ("Using voice:"), repr(voice)
#     engine.setProperty('voice',voice.id)
#     engine.say("Hello Hello Hello")
# engine.runAndWait()

# import os
# 
# os.system('espeak "{}"'.format(text))

import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.say(text)
    engine.runAndWait()

# Example usage
text = "Hello, Raspberry Pi. Text to speech is working!"
speak(text)
