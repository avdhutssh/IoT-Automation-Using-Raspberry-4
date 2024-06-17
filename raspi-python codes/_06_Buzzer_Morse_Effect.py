# Program to control the Buzzer with Morse code
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
BUZZER_PIN = 21

GPIO.setup(BUZZER_PIN, GPIO.OUT)

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

DOT_DURATION = 0.1  # Duration of a dot
DASH_DURATION = DOT_DURATION * 3  # Duration of a dash
SYMBOL_SPACE = DOT_DURATION  # Space between dots and dashes in a letter
LETTER_SPACE = DOT_DURATION * 3  # Space between letters
WORD_SPACE = DOT_DURATION * 7  # Space between words

def send_morse_code(message):
    for letter in message:
        if letter == ' ':
            time.sleep(WORD_SPACE)
        else:
            morse = MORSE_CODE.get(letter.upper(), '')
            for symbol in morse:
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
        message = "HELLO WORLD"
        send_morse_code(message)
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        GPIO.cleanup()
        print("GPIO cleaned up")
