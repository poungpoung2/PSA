import board
import digitalio
import time

# Define States
states = ["OFF", "ON"]
cur_state = "OFF"

# Define Polling Interval
POLL_INTERVAL = 0.02

# Track button state for edge detection
prev_button_state = False
prev_color = False

# Create variable to store button and LED states
isWhite = False

# Function to turn on LEDs
def turnOn():
    if isWhite:
        g_led_1.value = True
        g_led_2.value = True
        g_led_3.value = True

    r_led_1.value = True
    r_led_2.value = True
    r_led_3.value = True

    b_led_1.value = True
    b_led_2.value = True
    b_led_3.value = True


# Function to turn off LEDs
def turnOff():
    r_led_1.value = False
    r_led_2.value = False
    r_led_3.value = False

    g_led_1.value = False
    g_led_2.value = False
    g_led_3.value = False

    b_led_1.value = False
    b_led_2.value = False
    b_led_3.value = False

# Function to toggle between white and purple
def toggle_color():
    g_led_1.value = isWhite
    g_led_2.value = isWhite
    g_led_3.value = isWhite


# Configure the GPIO pins for LEDs as digital outputs
r_led_1 = digitalio.DigitalInOut(board.GP22)
r_led_1.direction = digitalio.Direction.OUTPUT
r_led_2 = digitalio.DigitalInOut(board.GP26)
r_led_2.direction = digitalio.Direction.OUTPUT
r_led_3 = digitalio.DigitalInOut(board.GP27)
r_led_3.direction = digitalio.Direction.OUTPUT

g_led_1 = digitalio.DigitalInOut(board.GP21)
g_led_1.direction = digitalio.Direction.OUTPUT
g_led_2 = digitalio.DigitalInOut(board.GP20)
g_led_2.direction = digitalio.Direction.OUTPUT
g_led_3 = digitalio.DigitalInOut(board.GP19)
g_led_3.direction = digitalio.Direction.OUTPUT

b_led_1 = digitalio.DigitalInOut(board.GP18)
b_led_1.direction = digitalio.Direction.OUTPUT
b_led_2 = digitalio.DigitalInOut(board.GP17)
b_led_2.direction = digitalio.Direction.OUTPUT
b_led_3 = digitalio.DigitalInOut(board.GP16)
b_led_3.direction = digitalio.Direction.OUTPUT

# Configure the GPIO pin connected to the button as a digital input with pull-up resistor
onoff_button = digitalio.DigitalInOut(board.GP13)  # Set actual pin
onoff_button.direction = digitalio.Direction.INPUT
onoff_button.pull = digitalio.Pull.UP

white_button = digitalio.DigitalInOut(board.GP11)  # Set actual pin
white_button.direction = digitalio.Direction.INPUT
white_button.pull = digitalio.Pull.UP

# Start looping for polling
while True:
    # Read button state
    isPressed = not onoff_button.value
    isWhite = not white_button.value

    # Detect button press 
    if isPressed and not prev_button_state:
        if cur_state == "OFF":
            cur_state = "ON"
            turnOn()
        elif cur_state == "ON":
            cur_state = "OFF"
            turnOff()

    # Detect color toggle press
    if prev_color != isWhite:
        toggle_color()

    # Update previous button state
    prev_button_state = isPressed
    prev_color = isWhite

    # Sleep for polling interval
    time.sleep(POLL_INTERVAL)
