import csv
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



def get_distance():
    while not vl53.data_ready:
        pass
    vl53.clear_interrupt()
    distance = vl53.distance
    if distance == 0.0:
        return 100
    return distance

def forward():
    kit.continuous_servo[0].throttle = 0.3
    kit.continuous_servo[1].throttle = 0.3

def step_back():
    kit.continuous_servo[0].throttle = -0.1
    kit.continuous_servo[1].throttle = -0.1
    time.sleep(0.5)

def turn():
    kit.continuous_servo[0].throttle = 0.25
    kit.continuous_servo[1].throttle = -0.1
    time.sleep(0.5)

def stop():
    kit.continuous_servo[0].throttle = 0.1
    kit.continuous_servo[1].throttle = 0.1


def run():
    distance = get_distance()
    print('Distance = ', distance)
    forward()
    if distance <= 20:
        step_back()
        turn()
        
    if distance >= 100:
        stop()
    return distance

    

if __name__ == '__main__':
    header = ['distance']
    i = 0
    with open('distance_log.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)     
        while True:
            distance = get_distance()
            writer.writerow([distance])
            print('Distance = ', distance)
            forward()
            if distance <= 20:
                step_back()
                turn()
                
            if distance >= 100:
                stop()
                
        
            


