from gpiozero import DistanceSensor, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

uds = DistanceSensor(trigger=27, echo=22)
buzzer = TonalBuzzer(21, octaves=3)

while True:
	print(sensor.distance)
	buzzer.play(Tone(midi=69))
	sleep(1)