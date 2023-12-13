# # Make sure to have everything set up
# # https://github.com/sparkfun/Qwiic_Keypad_Py 
# # `pip install sparkfun-qwiic-keypad`

# # From https://github.com/sparkfun/Qwiic_Keypad_Py/blob/main/examples/qwiic_keypad_ex2.py


import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import ili9341
import qwiic_keypad
import time
import sys

#inputs = ["", "", "", ""]

# Screen setup
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D27)
BAUDRATE = 24000000
spi = board.SPI()
disp = ili9341.ILI9341(
    spi, cs=cs_pin, dc=dc_pin, rst=reset_pin, baudrate=BAUDRATE, width=240, height=320
)

# Keypad setup
print("\nSparkFun qwiic Keypad Example\n")
myKeypad = qwiic_keypad.QwiicKeypad()
if myKeypad.connected == False:
    print("The Qwiic Keypad device isn't connected to the system. Please check your connection", file=sys.stderr)
    sys.exit(1)
myKeypad.begin()
print("Initialized. Firmware Version: %s" % myKeypad.version)

# Function to update the screen
def update_screen(display, text):
    width, height = display.width, display.height
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    font_path = "arial.ttf"  
    font_size = 60  # Adjust this size as needed
    font = ImageFont.truetype(font_path, font_size)

    draw.text((0, 0), text, font=font, fill="#FFFFFF")

    display.image(image)

# Initialize text with underscores
text = "_ _ _ _"
update_screen(disp, text)

# Main loop
input_count = 0
while True:
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
                update_screen(disp, text)

        elif charButton == '#' and input_count == 4:  # Enter
            # Perform an action since all 4 digits are entered
            print("Entered number: ", text.replace(" ", ""))  # Example action

            # Reset the input
            text = "_ _ _ _"
            input_count = 0
            update_screen(disp, text)

        elif input_count < 4:
            if charButton.isdigit():
                text = text[:input_count*2] + charButton + text[input_count*2+1:]
                input_count += 1
                update_screen(disp, text)

    time.sleep(.1)