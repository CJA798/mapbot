import numpy as np
import pandas as pd
import time
import datetime
import board
import adafruit_vl53l4cd
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX
from adafruit_as7341 import AS7341
from adafruit_servokit import ServoKit

i2c = board.I2C()  # uses board.SCL and board.SDA

# Motors setup
kit = ServoKit(channels=16)
left_motor = kit.continuous_servo[0]
right_motor = kit.continuous_servo[1]

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
as7341.led_current = 25
as7341.led = True
as7341_channels = as7341.all_channels

# Dataframe Setup
columns = ["distance",
           "x_acceleration", "y_acceleration", "z_acceleration",
           "x_rotation", "y_rotation", "z_rotation",
           "channel_415nm", "channel_445nm", "channel_480nm", "channel_515nm",
           "channel_555nm", "channel_590nm", "channel_630nm", "channel_680nm",
           "clear", "near_ir"]

df = pd.DataFrame(columns=columns)
filename = "logs/raw_data_{}".format(datetime.datetime.now())


data = np.empty(len(columns), dtype='float')
def get_data():
    vl53l4cx.start_ranging()
    while not vl53l4cx.data_ready:
        pass
    vl53l4cx.clear_interrupt()
    distance_data = vl53l4cx.distance
    vl53l4cx.stop_ranging()
    data[0] = distance_data
    
    data_gyro = lsm6dso32.gyro
    data_accel = lsm6dso32.acceleration
    for i in range(0,2):
        data[i+1] = data_gyro[i]
        data[i+4] = data_accel[i]
    
    for i in range(0,7):
        data[i+7] = as7341_channels[i]
    data[15] = as7341.channel_clear
    data[16] = as7341.channel_nir
    
    return data

def log_data():
    df.loc[len(df.index)] = get_data()
    #print(df.head())
    #df.to_csv(filename)
    
def stop():
    vl53l4cx.stop_ranging()
    as7341.led_current = 0
    as7341.led = False
    for i in range(0,16):
        kit.continuous_servo[i].throttle = 0.1

def rotate():
    left_motor.throttle = -0.3
    right_motor.throttle = 0.4
    

if __name__ == '__main__':
    rotate()
    for _ in range(50):
        log_data()
    stop()
    df.to_csv(filename)
    

