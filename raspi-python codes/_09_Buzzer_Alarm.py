# Program to create the Alarm Buzzer
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
BUZZER_PIN = 21
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def sound_alarm():
    pwm = GPIO.PWM(BUZZER_PIN, 1000)
    pwm.start(50)
    for _ in range(5):
        pwm.ChangeFrequency(1000)
        time.sleep(0.5)
        pwm.ChangeFrequency(500)
        time.sleep(0.5)
    pwm.stop()

if __name__ == "__main__":
    try:
        while True:
            sound_alarm()
            time.sleep(5)
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        GPIO.cleanup()
        print("GPIO cleaned up")
