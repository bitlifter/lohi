import pigpio
import time

# Connect to the pigpio daemon running on the secondary Pi
secondaryPi = pigpio.pi('secondaryPi_IP')  # replace secondaryPi_IP with the actual IP address of your secondary Pi

# Set the pin mode as an input
secondaryPi.set_mode(16, pigpio.INPUT)

def test_connectivity():
    # Check the status of pin 16
    if secondaryPi.read(16):
        print("Pin 16 on secondary Pi is HIGH")
    else:
        print("Pin 16 on secondary Pi is LOW")

# Test connectivity
try:
    while True:
        test_connectivity()
        time.sleep(1)  # Delay for 1 second

finally:
    secondaryPi.stop()  # Disconnect from the pigpio daemon