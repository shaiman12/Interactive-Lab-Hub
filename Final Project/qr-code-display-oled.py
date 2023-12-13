import board
import busio
import adafruit_ssd1306
from PIL import Image

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class. Make sure to use the correct width and height.
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Load your image.
image_path = 'qr-code.png'  # Ensure this is the correct path to your image
image = Image.open(image_path).convert('1')  # Convert image to 1-bit color

# Calculate the aspect ratio and resize proportionally
aspect_ratio = image.width / image.height
new_height = int(oled.height)
new_width = int(aspect_ratio * new_height)

if new_width > oled.width:
    new_width = oled.width
    new_height = int(new_width / aspect_ratio)

image = image.resize((new_width, new_height), Image.BICUBIC)

# Create a new blank image with the size of the display
blank_image = Image.new('1', (oled.width, oled.height))

# Paste the resized image onto the blank image
x = (oled.width - new_width) // 2
y = (oled.height - new_height) // 2
blank_image.paste(image, (x, y))

# Display image.
oled.image(blank_image)
oled.show()
