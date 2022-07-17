import board
import time
from adafruit_servokit import ServoKit
import adafruit_vl53l4cd
from adafruit_as7341 import AS7341

i2c = board.I2C()  # uses board.SCL and board.SDA

# Distance sensor stop
## vl53l4cx sensor used but vl53l4cd library implemented (no python library for CX yet).
vl53l4cx = adafruit_vl53l4cd.VL53L4CD(i2c)
vl53l4cx.inter_measurement = 0
vl53l4cx.timing_budget = 100
vl53l4cx.stop_ranging()
print("\nDistance sensor OFF.")

# Color sensor stop
as7341 = AS7341(i2c)
as7341.led_current = 0
as7341.led = False
print("Color sensor OFF.")

# Motors stop
kit = ServoKit(channels=16)
for i in range(0,16):
    kit.continuous_servo[i].throttle = 0.1
print("Motors OFF.\n")

    


