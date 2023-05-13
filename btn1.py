from gpiozero import Button
import os


def call_script():
    print("Button pressed. Calling script...")
    os.system("python3 btn2.py")
    
def call_script2():
    print("Button pressed. Calling script2...")
    os.system("python3 ultrasonic.py")

button = Button(17)
# button2 = Button(26)
button.when_pressed = call_script
# button2.when_pressed = call_script2

while True:
    pass