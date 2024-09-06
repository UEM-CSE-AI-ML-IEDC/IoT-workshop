import RPi.GPIO as GPIO
import time

# GPIO Pin where the gas sensor's digital output is connected
GAS_SENSOR_PIN = 17  # GPIO17 (Pin 11)

def setup():
    GPIO.setmode(GPIO.BCM)  # Set the GPIO mode to BCM
    GPIO.setup(GAS_SENSOR_PIN, GPIO.IN)  # Set the GAS_SENSOR_PIN as input

def loop():
    try:
        while True:
            if GPIO.input(GAS_SENSOR_PIN) == 0:
                print("No Gas Detected")
            else:
                print("Gas Detected! Take Action!")
            time.sleep(1)  # Read every second
    except KeyboardInterrupt:
        GPIO.cleanup()  # Clean up GPIO on exit

if __name__ == "__main__":
    setup()
    loop()
