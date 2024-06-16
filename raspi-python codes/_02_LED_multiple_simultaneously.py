# Program to blink Multple LED simulatneously
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
LED1 = 1
LED2 = 12
LED3 = 16
LED4 = 20
LED5 = 21
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)
GPIO.setup(LED5,GPIO.OUT)
while True:
    GPIO.output(LED1, True)
    GPIO.output(LED2, True)
    GPIO.output(LED3, True)
    GPIO.output(LED4, True)
    GPIO.output(LED5, True)
    time.sleep(1)
    print("LED On")
    GPIO.output(LED1, False)
    GPIO.output(LED2, False)
    GPIO.output(LED3, False)
    GPIO.output(LED4, False)
    GPIO.output(LED5, False)
    time.sleep(1)
    print("LED Off")