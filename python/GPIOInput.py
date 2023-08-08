import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
inPin=40
GPIO.setup(inPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
from time import sleep
try:
	while True:
		readVal=GPIO.input(inPin)
		print(readVal)
		sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()

