from gpiozero import PWMLED
from time import sleep, time
import random

led = PWMLED(16)

try:
    # Run forever
    while True:
        # Set the LED to a constant brightness of 30% for a random duration between 1 and 3 minutes
        led.value = 0.3
        sleep(random.uniform(5, 15))  # Convert minutes to seconds

        # Simulate erratic headlight behavior for a random duration between 10 and 15 seconds
        end_time = time() + random.uniform(10, 15)
        while time() < end_time:
            # Generate a random brightness level between 0.3 (dim) and 0.5 (bright)
            brightness = random.uniform(0.3, 0.5)
            led.value = brightness

            # Generate a random sleep duration between 0.07 and 0.28 seconds to simulate a loose wire effect
            duration = random.uniform(0.07, 0.28)
            sleep(duration)

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    print("Turning off the LED")
    led.value = 0
