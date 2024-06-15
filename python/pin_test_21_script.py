import RPi.GPIO as GPIO
import time

# Use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)

# set up the GPIO channels - one input (GPIO 6)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def test_connectivity():
    # Check the status of pin 6
    if GPIO.input(6):
        print("Pin 6 is HIGH")
    else:
        print("Pin 6 is LOW")

# Test connectivity
try:
    while True:
        test_connectivity()
        time.sleep(1)  # Delay for 1 second

finally:
    GPIO.cleanup()