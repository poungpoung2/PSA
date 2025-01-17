import board
import digitalio
import time

# Define States
states = ["OFF_Pressed", "OFF_NotPressed", "ON_NotPressed", "ON_Pressed"]
cur_state = "OFF_NotPressed"

# Define Polling Interval
POLL_INTERVAL = 0.02

# Create variable to store button and LED states
isPressed = False
isWhite = False

# Function to turn on LEDs
def turnOn():
    if isWhite:
        g_led.value = True  
    r_led.value = True
    b_led.value = True

# Function to turn off LEDs
def turnOff():
    r_led.value = False
    g_led.value = False
    b_led.value = False

# Configure the GPIO pins for LEDs as digital outputs
r_led = digitalio.DigitalInOut()  
g_led = digitalio.DigitalInOut()
b_led = digitalio.DigitalInOut()

r_led.direction = digitalio.Direction.OUTPUT
g_led.direction = digitalio.Direction.OUTPUT
b_led.direction = digitalio.Direction.OUTPUT

# Configure the GPIO pin connected to the button as a digital input with pull-up resistor
onoff_button = digitalio.DigitalInOut()  # Set actual pin
onoff_button.direction = digitalio.Direction.INPUT
onoff_button.pull = digitalio.Pull.UP

white_button = digitalio.DigitalInOut()  # Set actual pin
white_button.direction = digitalio.Direction.INPUT
white_button.pull = digitalio.Pull.UP

# Start looping for polling
while True:
    # Update the button status
    isPressed = not onoff_button.value  
    isWhite = not white_button.value  

    # If the current state is OFF_NotPressed
    if cur_state == "OFF_NotPressed":
        # If the button is pressed
        if isPressed:  
            cur_state = "ON_Pressed"
            turnOn()

    # If the current state is ON_Pressed
    elif cur_state == "ON_Pressed":
        # If the button is released
        if not isPressed:  
            cur_state = "ON_NotPressed"

    # If the current state is ON_NotPressed
    elif cur_state == "ON_NotPressed":
        # If the button is pressed again
        if isPressed:  
            cur_state = "OFF_Pressed"
            turnOff()

    # If the current state is OFF_Pressed
    elif cur_state == "OFF_Pressed":
        # If the button is released
        if not isPressed:  
            cur_state = "OFF_NotPressed"

    # Sleep for polling interval
    time.sleep(POLL_INTERVAL)
