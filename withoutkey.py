import cv2
import pytesseract
from PIL import Image
from gtts import gTTS
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Set up the camera
camera = cv2.VideoCapture(0)

# Capture an image from the camera
ret, frame = camera.read()

# Convert the captured image to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Apply thresholding to the grayscale image
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Perform OCR using Tesseract
text = pytesseract.image_to_string(Image.fromarray(thresh))

# Convert text to speech
tts = gTTS(text)
tts.save("speech.mp3")

# Load and play the speech
pygame.mixer.music.load("speech.mp3")
pygame.mixer.music.play()

# Wait for the speech to finish playing
while pygame.mixer.music.get_busy():
    continue

# Release the camera
camera.release()