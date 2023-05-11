from gpiozero import Button
import os

# Initialize count to 0
file = open("count.txt", "w")
file.write(str(0))
file.close()

def call_script():
    count = open("count.txt", "r")
    cnt = int(count.read())
    count.close()
    
    if cnt % 2 == 0:
        print("Button pressed. Calling script...")
        os.system("python3 modify.py")
    else:
        print("Stopping....")
        # Create an empty file as a signal to stop the modify.py script
        stop_file = open("stop.txt", "w")
        stop_file.close()
    
    cnt += 1
    count = open("count.txt", "w")
    count.write(str(cnt))
    count.close()

button = Button(17)
button.when_pressed = call_script

while True:
    # Check if the stop.txt file exists, indicating a request to stop the modify.py script
    if os.path.exists("stop.txt"):
        os.remove("stop.txt")  # Remove the stop.txt file
        print("Received stop signal. Exiting modify.py script.")
        break  # Break out of the while True loop

    # Rest of the main file's code



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
