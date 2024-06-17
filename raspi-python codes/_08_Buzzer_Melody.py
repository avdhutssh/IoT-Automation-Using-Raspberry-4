# Program to control the Melody Buzzer
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
BUZZER_PIN = 21
GPIO.setup(BUZZER_PIN, GPIO.OUT)
melody = [
    (262, 0.5),
    (294, 0.5),
    (330, 0.5),
    (349, 0.5),
    (392, 0.5),
    (440, 0.5),
    (494, 0.5),
    (523, 1.0)
]

def play_melody():
    pwm = GPIO.PWM(BUZZER_PIN, 440)
    pwm.start(50)
    for note, duration in melody:
        pwm.ChangeFrequency(note)
        time.sleep(duration)
    pwm.stop()

if __name__ == "__main__":
    try:
        while True:
            play_melody()
            time.sleep(2)
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        GPIO.cleanup()
        print("GPIO cleaned up")

