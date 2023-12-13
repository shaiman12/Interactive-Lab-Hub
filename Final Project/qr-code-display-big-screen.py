import digitalio
import board
from PIL import Image
from adafruit_rgb_display import ili9341  # Import ILI9341

# Configuration for CS, DC, and RST pins:
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D27)  # Define reset pin

# Config for display baudrate (default max is 24mhz for ILI9341):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ILI9341 display:
disp = ili9341.ILI9341(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=240,  # ILI9341 width
    height=320   # ILI9341 height
)

# Load your image.
image_path = 'qr-code-unlock.png'  # Make sure this is the correct path to your image
image = Image.open(image_path)

# Rotate and resize the image to fit the display
rotation = 0
image = image.rotate(rotation, expand=True)

# Calculate the aspect ratio and resize proportionally
aspect_ratio = image.width / image.height
new_height = int(disp.height)
new_width = int(aspect_ratio * new_height)

if new_width > disp.width:
    new_width = disp.width
    new_height = int(new_width / aspect_ratio)

image = image.resize((new_width, new_height), Image.BICUBIC)

# Create a new blank image with the size of the display
blank_image = Image.new("RGB", (disp.width, disp.height))

# Paste the resized image onto the blank image, centered
x = (disp.width - new_width) // 2
y = (disp.height - new_height) // 2
blank_image.paste(image, (x, y))

# Display the image
disp.image(blank_image)
