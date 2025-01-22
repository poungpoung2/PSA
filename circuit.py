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
