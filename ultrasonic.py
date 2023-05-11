import RPi.GPIO as GPIO
import time

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
GPIO.setup(37, GPIO.OUT)

# Initialize the buzzer
buzzer = GPIO.PWM(37, 100)
buzzer.start(0)

def measure_distance():
    # Trigger the ultrasonic sensor
    GPIO.output(23, True)
    time.sleep(0.00001)
    GPIO.output(23, False)

    # Wait for the echo response
    while GPIO.input(24) == 0:
        start_time = time.time()
    while GPIO.input(24) == 1:
        end_time = time.time()

    # Calculate distance
    duration = end_time - start_time
    distance = (duration * 34300) / 2

    return distance

try:
    while True:
        distance = measure_distance()
        print(f"Distance: {distance} cm")

        # Play a tone on the buzzer if the distance is less than 30 cm
        if distance < 30:
            buzzer.ChangeFrequency(440)
            buzzer.ChangeDutyCycle(50)
        else:
            buzzer.ChangeDutyCycle(0)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program stopped by user")
    buzzer.stop()
    GPIO.cleanup()
