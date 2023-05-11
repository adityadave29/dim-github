from gpiozero import Button
import os

def call_script():
    print("Button pressed. Calling script...")
    os.system("python3 modif.py")

button = Button(17)
button.when_pressed = call_script

while True:
    if button.is_pressed:
        print("Button pressed again. Stopping the program.")
        break
