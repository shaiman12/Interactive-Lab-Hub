# import digitalio
# import board
# from adafruit_rgb_display import ili9341
# import time

# # Configuration for CS, DC, and RST pins:
# cs_pin = digitalio.DigitalInOut(board.CE0)
# dc_pin = digitalio.DigitalInOut(board.D25)
# reset_pin = digitalio.DigitalInOut(board.D27)

# # Setup SPI bus using hardware SPI:
# spi = board.SPI()

# # Create the ILI9341 display:
# disp = ili9341.ILI9341(
#     spi,
#     rotation=90,  # Adjust rotation if needed
#     cs=cs_pin,
#     dc=dc_pin,
#     rst=reset_pin,
#     width=240,  # Adjust width if needed
#     height=320   # Adjust height if needed
# )

# # Fill the screen with a solid color.
# disp.fill(0xF81F)  # Magenta, for example

# time.sleep(10)  # Show the color for 10 seconds

import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import ili9341

# Configuration for CS, DC, and RST pins:
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D27)

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ILI9341 display:
disp = ili9341.ILI9341(
    spi,
    rotation=90,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    width=240,
    height=320
)

# Create blank image for drawing.
image = Image.new("RGB", (320, 240))
draw = ImageDraw.Draw(image)

# Load a font.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

# disp.image(image)

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)

    # IP address
    cmd = "hostname -I | cut -d' ' -f1"
    IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
    draw.text((0, 0), 'IP: ' + IP, font=font, fill="#FFFFFF")

    # Network name
    try:
        cmd = "iwgetid -r"
        Network = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
    except subprocess.CalledProcessError:
        Network = "Error fetching network name"
    draw.text((0, 20), 'Net: ' + Network, font=font, fill="#FFFFFF")

    # MAC address
    MAC = subprocess.check_output("cat /sys/class/net/wlan0/address", shell=True).decode("utf-8").strip()
    draw.text((0, 40), 'MAC: ' + MAC, font=font, fill="#FFFFFF")

    # CPU usage
    CPU = subprocess.check_output("top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'", shell=True).decode("utf-8")
    draw.text((0, 60), 'CPU Load: ' + CPU, font=font, fill="#FFFFFF")

    # Display image.
    disp.image(image)
    time.sleep(2)  # Refresh every 2 seconds
