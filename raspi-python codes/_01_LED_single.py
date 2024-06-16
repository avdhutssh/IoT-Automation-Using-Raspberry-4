# Program to blink Single LED
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led=21
GPIO.setup(led,GPIO.OUT)
while True: 
    GPIO.output(led,True)
    time.sleep(1)
    print("LED On")
    GPIO.output(led,False)
    time.sleep(1)
    print("LED Off")
