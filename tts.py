import pyttsx3

def text_to_speech(text):
    text_speech = pyttsx3.init()
    text_speech.say(text)
    text_speech.runAndWait()

if __name__ == "__main__":
    text = "Hello, this is a test."
    text_to_speech(text)
