import RPi.GPIO as GPIO
import time

LED_PINS = [1, 12, 16, 20, 21]
DELAY = 0.1

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in LED_PINS:
        GPIO.setup(pin, GPIO.OUT)

def led_chaser():
    while True:
        for pin in LED_PINS:
            GPIO.output(pin, True)
            time.sleep(DELAY)
            GPIO.output(pin, False)
        for pin in reversed(LED_PINS):
            GPIO.output(pin, True)
            time.sleep(DELAY)
            GPIO.output(pin, False)

def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        setup()
        led_chaser()
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        cleanup()
        print("GPIO cleaned up")
