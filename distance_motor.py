import board
import adafruit_vl53l4cd
import time
from adafruit_servokit import ServoKit

i2c = board.I2C()

vl53 = adafruit_vl53l4cd.VL53L4CD(i2c)

# OPTIONAL: can set non-default values
vl53.inter_measurement = 0
vl53.timing_budget = 200

print("VL53L4CD Simple Test.")
print("--------------------")
model_id, module_type = vl53.model_info
print("Model ID: 0x{:0X}".format(model_id))
print("Module Type: 0x{:0X}".format(module_type))
print("Timing Budget: {}".format(vl53.timing_budget))
print("Inter-Measurement: {}".format(vl53.inter_measurement))
print("--------------------")

kit = ServoKit(channels=16)
vl53.start_ranging()

while True:
    while not vl53.data_ready:
        pass
    vl53.clear_interrupt()
    distance = vl53.distance
    print('Distance: ', distance)
    if distance < 10:
        kit.continuous_servo[0].throttle = 0.3
    elif distance >= 10 and distance < 20:
        kit.continuous_servo[0].throttle = 0.5
    elif distance >= 20 and distance < 30:
        kit.continuous_servo[0].throttle = 0.7
    elif distance >= 30 and distance < 40:
        kit.continuous_servo[0].throttle = 1
    else:
        kit.continuous_servo[0].throttle = 0.1


