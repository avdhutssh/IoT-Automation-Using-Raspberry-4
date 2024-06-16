import RPi.GPIO as GPIO
import time

# Constants
LED_PINS = [1, 12, 16, 20, 21]
BLINK_INTERVAL = 1  # seconds

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in LED_PINS:
        GPIO.setup(pin, GPIO.OUT)

def blink_leds():
    while True:
        # Turn all LEDs on
        for pin in LED_PINS:
            GPIO.output(pin, True)
        print("LEDs On")
        time.sleep(BLINK_INTERVAL)

        # Turn all LEDs off
        for pin in LED_PINS:
            GPIO.output(pin, False)
        print("LEDs Off")
        time.sleep(BLINK_INTERVAL)

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
