import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the ultrasonic sensor
TRIG = 23  # GPIO pin 23 (Trig)
ECHO = 24  # GPIO pin 24 (Echo)

# Set up the GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    # Ensure the trigger pin is set to low
    GPIO.output(TRIG, False)
    time.sleep(2)

    # Trigger the ultrasonic pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # 10 microseconds pulse
    GPIO.output(TRIG, False)

    # Measure the time for the echo to return
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calculate the time difference
    pulse_duration = pulse_end - pulse_start

    # Calculate the distance (speed of sound = 34300 cm/s)
    distance = pulse_duration * 17150  # Convert time to distance in cm
    distance = round(distance, 2)  # Round to 2 decimal places

    return distance

try:
    while True:
        dist = measure_distance()
        print(f"Distance: {dist} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
