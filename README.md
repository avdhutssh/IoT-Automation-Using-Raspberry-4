<!--
    #/**
    # * @author Avdhut Shirgaonkar
    # * Email: avdhut.ssh@gmail.com
    # * LinkedIn: https://www.linkedin.com/in/avdhut-shirgaonkar-811243136/
    # */
    #/***************************************************/
-->

---

# 💻# IoT Automation Using Raspberry Pi-4 (Python)

## 📑 Table of Contents

- [Introduction](#introduction)
- [Must-Have Components/Devices](#components/devices)
- [Getting Started](#getting-started)
- [Running Tests](#running-tests)
- [Contents](#contents)
- [Contacts](#contacts)

## 📖 Introduction

This repository contains various Python scripts for IoT automation projects using the Raspberry Pi 4. The projects demonstrate how to control LEDs, LDRs, sensors, buttons, and relays.

## 🍓 IoT and Raspberry pi

### What is IoT?

The Internet of Things (IoT) refers to a network of physical devices connected to the internet, collecting and sharing data. These devices, equipped with sensors and software, interact with their environment and communicate with each other, enabling intelligent decision-making and automation.

### Why Raspberry Pi for IoT?

The Raspberry Pi is a small, affordable computer ideal for IoT projects. With its GPIO pins, the Raspberry Pi can interface with a variety of sensors and actuators, making it perfect for automation tasks. Its affordability, versatility, and extensive community support make it an excellent choice for both beginners and experienced developers.

![alt text](./misc/Raspberry%20Pi%204%20Pinout%20Diagram%20and%20terminals.png "Pinout diagram")

### Benefits of IoT Automation

**Efficiency**: Automate repetitive tasks, saving time and reducing errors.

**Monitoring**: Continuously monitor environments and systems for optimal performance.

**Control**: Remotely control devices and systems from anywhere in the world.

**Data Collection**: Gather data for analysis, enabling informed decision-making and predictive maintenance.

## 🛠️ Components/Devices

Raspberry Pi computer (Pi 3 / Pi 4 / Pi 5, any version)

Minimum 32 GB MicroSD card

Raspberry Pi power adapter

Sensors/Interfaces Used

LEDs, resistors (common values: 100 ohm, 1k, 10k, 4.7k, 330 ohm)

Transistorized relay interfacing module

LDR (Light Dependent Resistor)

Capacitor

Buzzer

## ▶️ Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/avdhutssh/Iot-Automation-Using-Raspberry-4.git
   cd Iot-Automation-Using-Raspberry-4/raspi-python codes
   ```

2. Navigate to the project directory:

   ```bash
   cd Iot-Automation-Using-Raspberry-4
   ```

3. Setup:

    Ensure you have Python and the RPi.GPIO library installed on your Raspberry Pi.

   ```bash
    sudo apt-get update
    sudo apt-get install python3-dev
    sudo apt-get install python3-pip
    sudo apt-get install python3-rpi.gpio
   ```

## 🚀 Running Scripts:


```bash
python3 _01_LED_single.py
```

## 📚 Contents

### LED Control
_01_LED_single.py: Control a single LED.

_02_LED_multiple_simultaneously.py: Control multiple LEDs simultaneously.

_02_LED_multiple_simultaneously_Optimize.py: Optimized control of multiple LEDs.

_03_LED_multiple_alternately.py: Control multiple LEDs alternately.

_04_LED_Chaser_Knight_Rider_Effect.py: Create a Knight Rider effect with LEDs.

### Buzzer Control

_05_Buzzer.py: Basic buzzer control.

_06_Buzzer_Morse_Effect.py: Generate Morse code effects.

_07_Buzzer_SOS_Signal.py: Create an SOS signal.

_08_Buzzer_Melody.py: Play a melody using the buzzer.

_09_Buzzer_Alarm.py: Create an alarm sound.

_10_Buzzer_Beep_Pattern.py: Beep in a specific pattern.

_11_Buzzer_CountdownTimer.py: Countdown timer with buzzer.
Relay Control

_12_Relay_On.py: Turn on a single relay.

_13_Relays_Simultaneously_Starting.py: Start all relays simultaneously.

_14_Relays_Starting_Sequence.py: Start relays in sequence.

_15_Relay_Bulb.py: Turn on a bulb using a relay.

_16_Relay_Toggle_Bulb.py: Toggle a bulb on and off with a relay.

### Sensor and Button Control

_17_Button_Input.py: Read input from a button.

_18_LDR.py: Read data (resistance) from an LDR (Light Dependent Resistor).

## 📧 Contacts

- [![Email](https://img.shields.io/badge/Email-avdhut.ssh@gmail.com-green)](mailto:avdhut.ssh@gmail.com)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/avdhut-shirgaonkar-811243136/)

Feel free to reach out if you have any questions, or suggestions

Happy Learning!!!
