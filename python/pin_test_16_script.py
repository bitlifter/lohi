import RPi.GPIO as GPIO
import time

# Use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)

# set up the GPIO channels - one input (GPIO 16)
GPIO.setup(16, GPIO.IN)

def test_connectivity():
    # Check the status of pin 16
    if GPIO.input(16):
        print("Pin 16 is HIGH")
    else:
        print("Pin 16 is LOW")

# Test connectivity
try:
    while True:
        test_connectivity()
        time.sleep(1)  # Delay for 1 second

finally:
    GPIO.cleanup()