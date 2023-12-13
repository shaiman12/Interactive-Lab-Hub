from rpi_ws281x import PixelStrip, Color
import time

# LED strip configuration:
LED_COUNT = 30         # Number of LED pixels (change this to the number of pixels in your strip)
LED_PIN = 21           # GPIO pin connected to the pixels (13 is used here).
LED_FREQ_HZ = 800000   # LED signal frequency in hertz (usually 800kHz)
LED_DMA = 10           # DMA channel to use for generating signal
LED_BRIGHTNESS = 255   # Set brightness (0 to 255)
LED_INVERT = False     # True to invert the signal

# Create PixelStrip object
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

# Define a function to turn on all LEDs to white
def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

try:
    while True:
        print("Turning on the strip")
        colorWipe(strip, Color(255, 0, 0))  # White color
        time.sleep(1)
        print("Turning off the strip")
        colorWipe(strip, Color(0, 0, 0))        # Off
        time.sleep(1)

except KeyboardInterrupt:
    # Turn off all pixels on Ctrl+C
    colorWipe(strip, Color(0, 0, 0), 10)
    print("LED strip turned off.")
