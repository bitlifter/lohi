import RPi.GPIO as GPIO
import time

# Use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)

# List of pins to test
pins = [21, 13, 26, 12, 20, 16, 19, 8]

# Set up the GPIO channels - one input for each pin
for pin in pins:
    GPIO.setup(pin, GPIO.IN)

def test_connectivity(pin):
    # Check the status of the pin
    if GPIO.input(pin):
        print(f"Pin {pin} is HIGH")
    else:
        print(f"Pin {pin} is LOW")

# Test connectivity
try:
    while True:
        for pin in pins:
            test_connectivity(pin)
        time.sleep(1)  # Delay for 1 second

finally:
    GPIO.cleanup()