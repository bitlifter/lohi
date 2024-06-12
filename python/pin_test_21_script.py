import RPi.GPIO as GPIO
import time

# Use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)

# set up the GPIO channels - one input (GPIO 21)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def test_connectivity():
    # Check the status of pin 21
    if GPIO.input(21):
        print("Pin 21 is HIGH")
    else:
        print("Pin 21 is LOW")

# Test connectivity
try:
    while True:
        test_connectivity()
        time.sleep(1)  # Delay for 1 second

finally:
    GPIO.cleanup()