import RPi.GPIO as GPIO
import time

class GPIOController:
    def __init__(self, pin=23):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        # Initially set the pin to LOW
        GPIO.output(self.pin, GPIO.LOW)

    def set_high(self):
        GPIO.output(self.pin, GPIO.HIGH)
        print(f"GPIO pin {self.pin} set to HIGH")

    def set_low(self):
        GPIO.output(self.pin, GPIO.LOW)
        print(f"GPIO pin {self.pin} set to LOW")

    def cleanup(self):
        GPIO.cleanup()
        print("GPIO cleaned up.")