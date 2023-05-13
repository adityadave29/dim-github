import RPi.GPIO as GPIO
import time

button_pin = 26  # GPIO pin number for the button
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

button_state = GPIO.input(button_pin)	
if button_state == GPIO.LOW:
# set GPIO numbering mode to BCM
	GPIO.setmode(GPIO.BCM)

	# set up pins for sensor and buzzer
	trig = 18
	echo = 24
	buzzer = 16

	# set up GPIO direction for sensor and buzzer
	GPIO.setup(trig, GPIO.OUT)
	GPIO.setup(echo, GPIO.IN)
	GPIO.setup(buzzer, GPIO.OUT)

	def get_distance():
		# trigger sensor to send ultrasonic signal
		GPIO.output(trig, True)
		time.sleep(0.00001)
		GPIO.output(trig, False)

		# measure time for ultrasonic signal to bounce back
		pulse_start = time.time()
		pulse_end = time.time()
		while GPIO.input(echo) == 0:
			pulse_start = time.time()
		while GPIO.input(echo) == 1:
			pulse_end = time.time()

		# calculate distance in centimeters
		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17150
		return distance

	try:
		while True:
			distance = get_distance()
			print("Distance: %.2f cm" % distance)

			# turn on buzzer if object is within 50 cm
			if distance < 100:
				GPIO.output(buzzer, True)
			else:
				GPIO.output(buzzer, False)

			time.sleep(0.5)

	except KeyboardInterrupt:
		GPIO.cleanup()