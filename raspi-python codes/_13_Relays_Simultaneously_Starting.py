#Program to start all relays simultaneously on Three Channel RPi Relay Board Raspberry Pi
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

try:
    while True:
        # If relay turns on with LOW signal
        GPIO.output(21, False)
        GPIO.output(20, False)
        GPIO.output(26, False)

        time.sleep(1)  # Adjust the duration as needed
        GPIO.output(21, True)
        GPIO.output(20, True)
        GPIO.output(26, True)

        time.sleep(1)  # Adjust the duration as needed
finally:
    GPIO.cleanup()
