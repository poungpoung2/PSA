import board
import digitalio
import time

# Define States / Current State 
states = ["OFF_Pressed", "OFF_NotPressed", "ON_NotPressed", "ON_Pressed"]
cur_state = "OFF_NotPressed"

# Define Polling interval
POLL_INTERVAL = 0.02 

# Create variable to store button and LED State
isPressed = False
isOn = False

# Function to turn on LEDs
def turnOn():
    r_led.value = True
    w_led.value = True
    b_led.value = True

# Function to turn off LEDs
def turnOff():
    r_led.value = False
    w_led.value = False
    b_led.value = False

# Configure the GPIO pin connected to the LED as a digital output
r_led = digitalio.DigitalInOut()
w_led = digitalio.DigitalInOut()
b_led = digitalio.DigitalInOut()

r_led.direction = digitalio.Direction.OUTPUT
w_led.direction = digitalio.Direction.OUTPUT
b_led.direction = digitalio.Direction.OUTPUT

# Configure the GPIO pin connected to the button as a digital input
button = digitalio . DigitalInOut (board.GP15)
button . direction = digitalio . Direction .INPUT
button .pull = digitalio .Pull.UP


# Start Looping for polling
while True:
    # Update the button status
    isPressed = button.value

    # If the current state off not pressed
    if cur_state == "OFF_NotPressed":
        # if the button is pressed
        if isPressed:
            # Turn on the LED and update the state
            isOn = True
            cur_state = "ON_Pressed"
            turnOn()

    # If the current state on pressed
    elif cur_state == "ON_Pressed":
        # If the button is released
        if not isPressed:
            # Update the state
            cur_state = "ON_NotPressed"
    
    # If the current state on not pressed
    elif cur_state == "'ON_NotPressed":
        # If the button is pressed
        if isPressed:
            # Turn off the LED and update the state
            isOn = False
            cur_state = "ON_Pressed"
            turnOff()
    
    # If the current state is off pressed
    else:
        # If the button is released
        if not isPressed:
            # Update the state
            cur_state = "OFF_NotPressed"
    
    # Sleep for polling interval
    time.sleep(POLL_INTERVAL)

