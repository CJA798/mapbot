import pandas as pd
import time
import datetime
import board
import adafruit_vl53l4cd
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX
from adafruit_as7341 import AS7341

i2c = board.I2C()  # uses board.SCL and board.SDA

# Distance sensor setup
## vl53l4cx sensor used but vl53l4cd library implemented (no python library for CX yet).
vl53l4cx = adafruit_vl53l4cd.VL53L4CD(i2c)
## OPTIONAL: can set non-default values
vl53l4cx.inter_measurement = 0
vl53l4cx.timing_budget = 100

# Gyro-Accelerometer Setup
lsm6dso32 = LSM6DSOX(i2c)

# Color sensor setup
as7341 = AS7341(i2c)
#as7341.led_current = 25
as7341.led = False

def bar_graph(read_value):
    scaled = int(read_value / 1000)
    return "[%5d] " % read_value + (scaled * "*")

# Print data
vl53l4cx.start_ranging()
while not vl53l4cx.data_ready:
    pass
vl53l4cx.clear_interrupt()
print("Distance: {} cm".format(vl53l4cx.distance))

print("\n------------------------------------------------")


print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (lsm6dso32.acceleration))
print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (lsm6dso32.gyro))

print("\n------------------------------------------------")

print("F1 - 415nm/Violet  %s" % bar_graph(as7341.channel_415nm))
print("F2 - 445nm//Indigo %s" % bar_graph(as7341.channel_445nm))
print("F3 - 480nm//Blue   %s" % bar_graph(as7341.channel_480nm))
print("F4 - 515nm//Cyan   %s" % bar_graph(as7341.channel_515nm))
print("F5 - 555nm/Green   %s" % bar_graph(as7341.channel_555nm))
print("F6 - 590nm/Yellow  %s" % bar_graph(as7341.channel_590nm))
print("F7 - 630nm/Orange  %s" % bar_graph(as7341.channel_630nm))
print("F8 - 680nm/Red     %s" % bar_graph(as7341.channel_680nm))
print("Clear              %s" % bar_graph(as7341.channel_clear))
print("Near-IR (NIR)      %s" % bar_graph(as7341.channel_nir))
print("\n------------------------------------------------")





