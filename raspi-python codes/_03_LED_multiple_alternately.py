# Program to blink Multple LED alternately
import RPi.GPIO as GPIO
import time

# Constants
LED_PINS = [1, 12, 16, 20, 21]
BLINK_INTERVAL = 0.25 # seconds

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in LED_PINS:
        GPIO.setup(pin, GPIO.OUT)

def blink_leds():
    while True:
        # Turn all LEDs on
        for pin in LED_PINS:
            GPIO.output(pin, True)
            time.sleep(BLINK_INTERVAL)
            print("LEDs On")
            GPIO.output(pin, False)
            time.sleep(BLINK_INTERVAL)
            print("LEDs Off")
        

def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        setup()
        blink_leds()
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        cleanup()
        print("GPIO cleaned up")

