# Program to create Countdown Timer Buzzer
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
BUZZER_PIN = 21
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"Time remaining: {i} seconds")
        time.sleep(1)
    print("Time's up! Buzzer on.")
    GPIO.output(BUZZER_PIN, True)
    time.sleep(5)
    GPIO.output(BUZZER_PIN, False)

if __name__ == "__main__":
    try:
        countdown_seconds = 5
        countdown_timer(countdown_seconds)
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        GPIO.cleanup()
        print("GPIO cleaned up")
