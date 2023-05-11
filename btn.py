from gpiozero import Button

import os

def call_script():
    print("Button pressed. Calling script...")
    os.system("python3 modif.py")

button = Button(17)

button.when_pressed = call_script

while True:
    pass


# from gpiozero import Button
# import os

# button_press_count = 0

# def call_script():
#     global button_press_count
#     button_press_count += 1
#     print("Button pressed. Calling script...")
#     if button_press_count == 1:
#         os.system("python3 modif.py")
#     elif button_press_count == 2:
#         print("Button pressed again. Stopping the program.")
#         exit()

# button = Button(17)
# button.when_pressed = call_script

# while True:
#     pass
