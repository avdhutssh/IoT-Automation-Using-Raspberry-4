#Program to start relays sequentially on Three Channel RPi Relay Board Raspberry Pi
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

try:
    while True:
        for pin in [21, 20, 26]: 
            GPIO.output(pin, True)
            time.sleep(1)
            GPIO.output(pin, False)
finally:
    GPIO.cleanup()
