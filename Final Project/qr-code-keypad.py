import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import ili9341
import qwiic_keypad
import time
import sys
import RPi.GPIO as GPIO
import requests
from io import BytesIO
from html.parser import HTMLParser
import base64
from rpi_ws281x import PixelStrip, Color  # Import for LED strip
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

locked = True

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

#GPIO setup
GPIO.setmode(GPIO.BCM)
PIN = 23  # Make sure this is the correct pin connected to your lock
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.HIGH)

# Screen setup
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D27)
BAUDRATE = 24000000
spi = board.SPI()
disp = ili9341.ILI9341(
    spi, cs=cs_pin, dc=dc_pin, rst=reset_pin, baudrate=BAUDRATE, width=240, height=320, rotation=180
)

# Load and prepare QR code image
#image_path = 'qr-code-unlock.png'  # Adjust path as needed
#qr_image = Image.open(image_path)
qr_image = None
class ImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.image_data = None

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            for attr in attrs:
                if attr[0] == "src" and attr[1].startswith("data:image/png;base64,"):
                    self.image_data = attr[1].split(",")[1]
try:
    response = requests.get("https://copwatch-api-test-9c567e874ba4.herokuapp.com/generate_qr")
    response.raise_for_status()

    parser = ImageParser()
    parser.feed(response.text)

    if parser.image_data:
        image_data = base64.b64decode(parser.image_data)
        qr_image = Image.open(BytesIO(image_data))
        #qr_image.show()
    else:
        print("No image data found in the response.")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
aspect_ratio = qr_image.width / qr_image.height

# Increase the height of the QR code, for example, 3/4th of the display height
qr_height = int(disp.height * 3 / 4)
qr_width = int(aspect_ratio * qr_height)

# Resize the QR image
qr_image = qr_image.resize((qr_width, qr_height), Image.BICUBIC)

# Ensure QR code width doesn't exceed the display width
if qr_width > disp.width:
    qr_width = disp.width
    qr_height = int(qr_width / aspect_ratio)
    qr_image = qr_image.resize((qr_width, qr_height), Image.BICUBIC)

# Keypad setup
print("\nSparkFun qwiic Keypad Example\n")
myKeypad = qwiic_keypad.QwiicKeypad()
if not myKeypad.connected:
    print("The Qwiic Keypad device isn't connected to the system. Please check your connection", file=sys.stderr)
    sys.exit(1)
myKeypad.begin()
print("Initialized. Firmware Version:", myKeypad.version)

# Function to update the screen with QR code and text
def update_screen(display, qr, text, message):
    width, height = display.width, display.height
    combined_image = Image.new("RGB", (width, height), "white")  # Background color white

    # Paste QR code
    x_qr = (width - qr_width) // 2
    combined_image.paste(qr, (x_qr, 0))

    # Create font object for drawing text
    text_font_path = "arial.ttf"  # Adjust as needed
    text_font_size = 60  # Font size for the text is 60
    text_font = ImageFont.truetype(text_font_path, text_font_size)

    # Create a separate font object for the message
    message_font_path = "arial.ttf"  # Adjust as needed
    message_font_size = 24  # Font size for the message is 24
    message_font = ImageFont.truetype(message_font_path, message_font_size)

    # Create ImageDraw object
    draw = ImageDraw.Draw(combined_image)

    # Manually set the x-coordinate for text
    text_x = 27  # As you've set

    # Adjust the y-coordinate to move text closer to the QR code
    spacing = -25  # Space between the QR code and the text, adjust as needed
    text_y = qr_height + spacing  # Position text closer to the QR code

    # Draw the text
    draw.text((text_x, text_y), text, font=text_font, fill="black")  # Font color black
    if message == "Connecting...":
        message_y = text_y + text_font_size + 10  # Adjust position of the message below the text
        text_x2 = 53
        draw.text((text_x2, message_y), message, font=message_font, fill="black")  # Font color black
    elif message == "Wrong code!":
        message_y = text_y + text_font_size + 10  # Adjust position of the message below the text
        text_x2 = 58
        draw.text((text_x2, message_y), message, font=message_font, fill="black")  # Font color black
    elif message == "Success!":
        message_y = text_y + text_font_size + 10  # Adjust position of the message below the text
        text_x2 = 70
        draw.text((text_x2, message_y), message, font=message_font, fill="black")  # Font color black
    else:
        # Draw the message (if any) below the text
        message_y = text_y + text_font_size + 10  # Adjust position of the message below the text
        text_x2 = 15
        draw.text((text_x2, message_y), message, font=message_font, fill="black")  # Font color black

    # Display the combined image
    display.image(combined_image)

def check_code(input_code):
    try:
        response = requests.get("https://copwatch-api-test-9c567e874ba4.herokuapp.com/get_code")
        response.raise_for_status()  # This will raise an error for HTTP error responses
        data = response.json()
        return int(input_code) == int(data["fourDigitCode"])
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Initialize text with underscores
text = "_ _ _ _"
message = ""
update_screen(disp, qr_image, text, message)

# Main loop
input_count = 0
while True:

    # colorWipe(Color(255, 0, 0))  # Turn red when locked
    colorWipeThreaded(Color(255, 0, 0, 0))
    myKeypad.update_fifo()
    button = myKeypad.get_button()

    if button == -1:
        print("No keypad detected")
        time.sleep(1)

    elif button != 0:
        charButton = chr(button)

        if charButton == '*':  # Backspace
            if input_count > 0:
                input_count -= 1
                text = text[:input_count*2] + '_' + text[input_count*2+1:]
                message = ""

        elif charButton == '#':
            if input_count != 4:
                message = "Please input 4 digits"
            else:
                inputted_code = text.replace(" ", "")  # Remove spaces
                
                # Display "Connecting..." message
                message = "Connecting..."
                update_screen(disp, qr_image, text, message)
                
                # Wait for 1 second
                time.sleep(1)
                
                # Check code and display result
                if check_code(inputted_code):
                    message = "Success!"
                    colorWipeThreaded(Color(255, 255, 255))
                    update_screen(disp, qr_image, text, message)
                    GPIO.output(PIN, GPIO.LOW)  # Unlock
                    time.sleep(5)  # Wait for 5 seconds
                    GPIO.output(PIN, GPIO.HIGH)  # Lock
                    colorWipeThreaded(Color(255, 0, 0))  # Turn red when locked
                    text = "_ _ _ _"
                    input_count = 0
                    message = ""
                    update_screen(disp, qr_image, text, message)
                    # Additional actions for successful code, like unlocking, can be added here
                else:
                    message = "Wrong code!"
                    text = "_ _ _ _"
                    input_count = 0

        elif input_count < 4 and charButton.isdigit():
            text = text[:input_count*2] + charButton + text[input_count*2+1:]
            input_count += 1
            message = ""

        update_screen(disp, qr_image, text, message)

    time.sleep(.1)
