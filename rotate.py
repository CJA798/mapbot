import board
import time
from adafruit_servokit import ServoKit

i2c = board.I2C()

kit = ServoKit(channels=16)

def rotate_about_z():
    kit.continuous_servo[0].throttle = 0.4    # Left
    kit.continuous_servo[1].throttle = -0.2   # Right
    
def rotate_about_right():
    kit.continuous_servo[0].throttle = 0.4    # Left
    kit.continuous_servo[1].throttle = -0.1   # Right

rotate_about_right()