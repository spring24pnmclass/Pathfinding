from gpiozero import Motor
from time import sleep

# Define the GPIO pins connected to the motor driver
# Adjust these pins according to your actual wiring
left_motor = Motor(forward=17, backward=18)
right_motor = Motor(forward=22, backward=23)

# Function to move the robot forward
def move_forward():
    left_motor.forward()
    right_motor.forward()

# Function to move the robot backward
def move_backward():
    left_motor.backward()
    right_motor.backward()

# Function to turn the robot left
def turn_left():
    left_motor.backward()
    right_motor.forward()

# Function to turn the robot right
def turn_right():
    left_motor.forward()
    right_motor.backward()

# Function to stop the robot
def stop():
    left_motor.stop()
    right_motor.stop()

# Test the movements
move_forward()
sleep(2)
stop()
sleep(1)

move_backward()
sleep(2)
stop()
sleep(1)

turn_left()
sleep(1)
stop()
sleep(1)

turn_right()
sleep(1)
stop()
