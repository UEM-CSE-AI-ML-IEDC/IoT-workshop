import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the pin connected to the rain sensor (Digital Output D0)
RAIN_SENSOR_PIN = 17

# Setup the pin as an input
GPIO.setup(RAIN_SENSOR_PIN, GPIO.IN)

def detect_rain():
    if GPIO.input(RAIN_SENSOR_PIN) == 0:
        print("It's raining!")
    else:
        print("No rain detected.")

try:
    while True:
        detect_rain()
        time.sleep(1)  # Check every second

except KeyboardInterrupt:
    print("Program terminated")

finally:
    GPIO.cleanup()  # Clean up the GPIO settings when done
