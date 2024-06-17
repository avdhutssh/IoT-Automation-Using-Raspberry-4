#Program to start relay to toggle on/off bulb
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

try:
    while True:
        GPIO.output(21, True)  # Turn on the bulb
        time.sleep(0.5)          # Wait for 5 seconds
        GPIO.output(21, False) # Turn off the bulb
        time.sleep(0.5)          # Wait for 5 seconds
finally:
    GPIO.cleanup()
