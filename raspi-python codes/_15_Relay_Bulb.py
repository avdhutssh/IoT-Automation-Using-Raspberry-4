#Program to start relay to turn on bulb
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

try:
        time.sleep(2)
        GPIO.output(21,False)
        time.sleep(5)
        GPIO.output(21,True)

finally:
    GPIO.cleanup()
