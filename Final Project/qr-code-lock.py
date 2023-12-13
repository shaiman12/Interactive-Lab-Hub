from flask import Flask, render_template, request, redirect, url_for, make_response
import RPi.GPIO as GPIO
import time
from rpi_ws281x import PixelStrip, Color
import threading

# LED strip configuration
LED_COUNT = 30  # Number of LED pixels
LED_PIN = 21  # GPIO pin connected to the pixels
LED_FREQ_HZ = 800000  # LED signal frequency in hertz
LED_DMA = 10  # DMA channel to use for generating signal
LED_BRIGHTNESS = 255  # Set brightness (0 to 255)
LED_INVERT = False  # True to invert the signal

# Create PixelStrip object
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

def colorWipeThreaded(color):
    def run():
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(50/1000.0)
    threading.Thread(target=run).start()

def pulseBlueThreaded():
    def run():
        for j in range(10):
            # Fade in
            for i in range(0, 256, 5):
                colorWipe(Color(0, 0, i), 500)
            # Fade out
            for i in range(255, 0, -5):
                colorWipe(Color(0, 0, i), 500)
    threading.Thread(target=run).start()

# Door lock setup
GPIO.setmode(GPIO.BCM)
PIN = 23
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.HIGH)

# Set up Flask server
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):
    changePin = int(changepin)
    if changePin == 1:
        print("UNLOCK")
        GPIO.output(PIN, GPIO.LOW)
        # pulseBlue(strip)  # Pulse blue when unlocked
    elif changePin == 2:
        print("LOCK")
        GPIO.output(PIN, GPIO.HIGH)
        # colorWipe(strip, Color(255, 0, 0), 10)  # Turn red when locked
    response = make_response(redirect(url_for('index')))
    return response

@app.route('/trigger-relay')
def trigger_relay():
    print("UNLOCK")
    colorWipeThreaded(Color(255, 255, 255))
    GPIO.output(PIN, GPIO.LOW)
    # pulseBlue(strip)  # Pulse blue
    time.sleep(5)
    print("LOCK")
    colorWipeThreaded(Color(255, 0, 0))  # Turn red when locked
    GPIO.output(PIN, GPIO.HIGH)
    # colorWipe(strip, Color(255, 0, 0), 10)  # Turn red
    return "Relay triggered for 5 seconds"

try:
    colorWipeThreaded(Color(255, 0, 0, 0))
    app.run(debug=True, host='0.0.0.0', port=8000)

except KeyboardInterrupt:
    colorWipeThreaded(Color(255, 0, 0, 0))
    GPIO.cleanup()
    print("Server and LED strip turned off.")