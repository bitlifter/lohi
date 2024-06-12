import pigpio
import time

# Connect to the pigpio daemon running on the secondary Pi
secondaryPi = pigpio.pi('secondaryPi_IP')  # replace secondaryPi_IP with the actual IP address of your secondary Pi

# List of pins to test
pins = [21, 13, 26, 12, 20, 16, 19, 8]

# Set the pin mode as an input for each pin
for pin in pins:
    secondaryPi.set_mode(pin, pigpio.INPUT)

def test_connectivity(pin):
    # Check the status of the pin
    if secondaryPi.read(pin):
        print(f"Pin {pin} on secondary Pi is HIGH")
    else:
        print(f"Pin {pin} on secondary Pi is LOW")

# Test connectivity
try:
    while True:
        for pin in pins:
            test_connectivity(pin)
        time.sleep(1)  # Delay for 1 second

finally:
    secondaryPi.stop()  # Disconnect from the pigpio daemon