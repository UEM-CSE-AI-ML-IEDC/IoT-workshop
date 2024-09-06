import RPi.GPIO as GPIO
import time

# GPIO Pin where the PIR sensor's output is connected
PIR_SENSOR_PIN = 18  # GPIO18 (Pin 12)

def setup():
    GPIO.setmode(GPIO.BCM)  # Set the GPIO mode to BCM
    GPIO.setup(PIR_SENSOR_PIN, GPIO.IN)  # Set the PIR_SENSOR_PIN as input

def loop():
    print("Waiting for motion detection...")
    time.sleep(2)  # Allow sensor to stabilize
    try:
        while True:
            if GPIO.input(PIR_SENSOR_PIN) == 1:
                print("Motion Detected!")
            else:
                print("No Motion")
            time.sleep(1)  # Check every second
    except KeyboardInterrupt:
        GPIO.cleanup()  # Clean up GPIO on exit

if __name__ == "__main__":
    setup()
    loop()
