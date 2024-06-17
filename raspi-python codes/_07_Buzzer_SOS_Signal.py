# Program to control the Buzzer with SOS signal
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

BUZZER_PIN = 21

GPIO.setup(BUZZER_PIN, GPIO.OUT)

DOT_DURATION = 0.1
DASH_DURATION = DOT_DURATION * 3
SYMBOL_SPACE = DOT_DURATION
LETTER_SPACE = DOT_DURATION * 3
WORD_SPACE = DOT_DURATION * 7

def send_sos():
    sos = "... --- ..."
    for symbol in sos:
        if symbol == '.':
            GPIO.output(BUZZER_PIN, True)
            time.sleep(DOT_DURATION)
        elif symbol == '-':
            GPIO.output(BUZZER_PIN, True)
            time.sleep(DASH_DURATION)
        GPIO.output(BUZZER_PIN, False)
        time.sleep(SYMBOL_SPACE)
    time.sleep(LETTER_SPACE)

if __name__ == "__main__":
    try:
        while True:
            send_sos()
            time.sleep(5)
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        GPIO.cleanup()
        print("GPIO cleaned up")
