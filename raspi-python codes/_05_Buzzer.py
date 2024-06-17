# Program to control the Buzzer
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

BUZZER_PIN = 21

GPIO.setup(BUZZER_PIN, GPIO.OUT)

def buzz():
    while True:
        GPIO.output(BUZZER_PIN, True)  
        time.sleep(1)                  
        GPIO.output(BUZZER_PIN, False) 
        time.sleep(2)                  

if __name__ == "__main__":
    try:
        buzz()
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        GPIO.cleanup()                
        print("GPIO cleaned up")

