import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins connected to the L298N
IN1 = 17  # Connect IN1 on L298N to GPIO17 on Raspberry Pi
IN2 = 27  # Connect IN2 on L298N to GPIO27 on Raspberry Pi

# Set up the GPIO pins as outputs
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Set IN1 to HIGH and IN2 to LOW to make the motor move forward
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)

# Let the motor run for 5 seconds
time.sleep(5)

# Stop the motor
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)

# Clean up the GPIO settings
GPIO.cleanup()
