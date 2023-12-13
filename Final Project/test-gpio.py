from gpio import GPIOController
import time

def main():
    gpio_controller = GPIOController(pin=23)

    try:
        while True:
            # Turn the pin high
            gpio_controller.set_high()
            time.sleep(2)  # Wait for 2 seconds

            # Turn the pin low
            gpio_controller.set_low()
            time.sleep(2)  # Wait for 2 seconds

    except KeyboardInterrupt:
        print("Exiting loop.")

    finally:
        # Clean up at the end
        gpio_controller.cleanup()

if __name__ == "__main__":
    main()

