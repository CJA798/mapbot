import pandas as pd

import time
import datetime
import board
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX


# Gyro-Accelerometer Setup
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = LSM6DSOX(i2c)


# Dataframe Setup
columns = ["x_acceleration", "y_acceleration", "z_acceleration",
           "x_rotation", "z_rotation", "z_rotation"]

df = pd.DataFrame(columns=columns)
filename = "gyroscope_{}".format(datetime.datetime.now())

while True:
    data_gyro = sensor.gyro
    data_accel = sensor.acceleration
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (sensor.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (sensor.gyro))
    print("")
    df.loc[len(df.index)] = [data_gyro[0], data_gyro[1], data_gyro[2],
               data_accel[0], data_accel[1], data_accel[2]]
    print(df.head())
    df.to_csv(filename)
    time.sleep(2)
