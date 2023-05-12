import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Define GPIO pins
TRIG_PIN = 23
ECHO_PIN = 24
BUZZER_PIN = 18

# Set up GPIO pins
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def calculate_distance():
    # Send 10us pulse to trigger pin
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # Record time of pulse
    while GPIO.input(ECHO_PIN) == False:
        start_time = time.time()

    while GPIO.input(ECHO_PIN) == True:
        end_time = time.time()

    # Calculate distance
    duration = end_time - start_time
    distance = duration * 17150 # Speed of sound in cm/s
    distance = round(distance, 2)

    return distance

def trigger_buzzer(distance, threshold):
    if distance < threshold:
        GPIO.output(BUZZER_PIN, True)
    else:
        GPIO.output(BUZZER_PIN, False)

try:
    while True:
        distance = calculate_distance()
        print(f"Distance: {distance} cm")
        trigger_buzzer(distance, 100) # Trigger buzzer if distance is less than 10 cm
        time.sleep(0.5)

finally:
    GPIO.cleanup()