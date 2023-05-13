import RPi.GPIO as GPIO
import time

button_pin = 26  # GPIO pin number for the button
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

running = False

def button_callback(channel):
    global running
    running = not running

GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback, bouncetime=300)

trig = 18
echo = 24
buzzer = 16

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

def get_distance():
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    pulse_start = time.time()
    pulse_end = time.time()
    while GPIO.input(echo) == 0:
        pulse_start = time.time()
    while GPIO.input(echo) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return distance

try:
    while True:
        if running:
            distance = get_distance()
            print("Distance: %.2f cm" % distance)

            if distance < 50:
                GPIO.output(buzzer, True)
            else:
                GPIO.output(buzzer, False)

            time.sleep(0.5)
        else:
            GPIO.output(buzzer, False)
            time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
