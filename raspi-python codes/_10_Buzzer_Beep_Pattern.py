# Program to create Beep Pattern Buzzer
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
BUZZER_PIN = 21
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def beep_pattern():
    pattern = [0.2, 0.2, 0.5, 0.2, 0.2, 1.0]
    for duration in pattern:
        GPIO.output(BUZZER_PIN, True)
        time.sleep(duration)
        GPIO.output(BUZZER_PIN, False)
        time.sleep(duration)

if __name__ == "__main__":
    try:
        while True:
            beep_pattern()
            time.sleep(3)
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        GPIO.cleanup()
        print("GPIO cleaned up")
