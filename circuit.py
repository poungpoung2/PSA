import board
import digitalio
import time

# Define States - these are all possible states of the system
states = ["OFF_Pressed", "OFF_NotPressed", "ON_NotPressed", "ON_Pressed"]
cur_state = "OFF_NotPressed"  # Initial state

# Define Polling Interval - how often to check button states
POLL_INTERVAL = 0.02

# Create variable to store button and LED states
isPressed = False  # On/Off button state
isWhite = False  # Color state
prev_white = False  # Previous color button state for edge detection


# Function to turn on LEDs - used when transitioning to ON state
def turnOn():
    if prev_white:  # If in white mode
        g_led_1.value = True
        g_led_2.value = True
        g_led_3.value = True

    r_led_1.value = True
    r_led_2.value = True
    r_led_3.value = True

    b_led_1.value = True
    b_led_2.value = True
    b_led_3.value = True


# Function to turn off LEDs - used when transitioning to OFF state
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


# Function to toggle between white and purple colors
def toggle_color():
    global isWhite
    isWhite = not isWhite  # Toggle the color state
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

# Configure the GPIO pins for buttons as digital inputs with pull-up resistors
onoff_button = digitalio.DigitalInOut(board.GP13)
onoff_button.direction = digitalio.Direction.INPUT
onoff_button.pull = digitalio.Pull.UP

white_button = digitalio.DigitalInOut(board.GP11)
white_button.direction = digitalio.Direction.INPUT
white_button.pull = digitalio.Pull.UP

# Start main polling loop
while True:
    # Update button states
    isPressed = not onoff_button.value
    white_pressed = not white_button.value

    # State machine logic
    if cur_state == "OFF_NotPressed":
        # If on/off button is pressed, turn on LEDs and change state
        if isPressed:
            cur_state = "ON_Pressed"
            turnOn()

    elif cur_state == "ON_Pressed":
        # If on/off button is released, change state
        if not isPressed:
            cur_state = "ON_NotPressed"

        # Check for color button rising edge
        if white_pressed and not prev_white:
            toggle_color()

    elif cur_state == "ON_NotPressed":
        # If on/off button is pressed, turn off LEDs and change state
        if isPressed:
            cur_state = "OFF_Pressed"
            turnOff()

        # Check for color button rising edge
        if white_pressed and not prev_white:
            toggle_color()

    elif cur_state == "OFF_Pressed":
        # If on/off button is released, change state
        if not isPressed:
            cur_state = "OFF_NotPressed"

    # Update previous color button state for next iteration
    prev_white = white_pressed
    # Wait before next poll
    time.sleep(POLL_INTERVAL)
