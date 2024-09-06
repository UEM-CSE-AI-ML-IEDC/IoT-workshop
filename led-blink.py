# pip install RPi.GPIO

import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin number where the LED is connected (GPIO17)
LED_PIN = 17

# Set the LED pin as an output pin
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        # Turn the LED on
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")
        time.sleep(2)  # Wait for 2 seconds

        # Turn the LED off
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")
        time.sleep(2)  # Wait for 2 seconds

except KeyboardInterrupt:
    # Clean up the GPIO settings before exiting
    GPIO.cleanup()
    print("Program stopped")
