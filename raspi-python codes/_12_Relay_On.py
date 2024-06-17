#Program to start relays alternately on Three Channel RPi Relay Board Raspberry Pi
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

try:
        GPIO.output(21,True)
        time.sleep(1)
        GPIO.output(21,False)
        GPIO.output(20,True)
        time.sleep(1)
        GPIO.output(20,False)
        GPIO.output(26,True)
        time.sleep(1)
        GPIO.output(26,False)

finally:
    GPIO.cleanup()