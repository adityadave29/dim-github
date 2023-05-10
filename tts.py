import pyttsx3
import cv2

def run_text_speech(text, count):
    text_speech = pyttsx3.init()
    text_speech.say(text)
    text_speech.runAndWait()
    cv2.waitKey(5)
    print("Asking for new image no: ", count)

# Example usage
text = "Hello, Raspberry Pi!"
count = 1
run_text_speech(text, count)
