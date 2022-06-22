import time
from adafruit_servokit import ServoKit

def smooth_surface():
    kit = ServoKit(channels=16)
    kit.continuous_servo[0].throttle = 0.25
    kit.continuous_servo[1].throttle = 0.25
    time.sleep(1)
    kit.continuous_servo[0].throttle = 0.1
    kit.continuous_servo[1].throttle = 0.1
    time.sleep(1)
    kit.continuous_servo[0].throttle = -0.055
    kit.continuous_servo[1].throttle = -0.055
    time.sleep(1)
    kit.continuous_servo[0].throttle = 0.1
    kit.continuous_servo[1].throttle = 0.1
    time.sleep(1)


def rough_surface():
    kit = ServoKit(channels=16)
    kit.continuous_servo[0].throttle = 0.4
    kit.continuous_servo[1].throttle = 0.4
    time.sleep(1)
    kit.continuous_servo[0].throttle = 0.1
    kit.continuous_servo[1].throttle = 0.1
    time.sleep(1)
    kit.continuous_servo[0].throttle = -0.2
    kit.continuous_servo[1].throttle = -0.2
    time.sleep(1)
    kit.continuous_servo[0].throttle = 0.1
    kit.continuous_servo[1].throttle = 0.1
    time.sleep(1)
    
def forward():
    kit = ServoKit(channels=16)
    kit.continuous_servo[0].throttle = 0.5
    kit.continuous_servo[1].throttle = -0.4
    time.sleep(1)
    kit.continuous_servo[0].throttle = -0.4
    kit.continuous_servo[1].throttle = 0.5
    time.sleep(1)
    
def high_low():
    kit = ServoKit(channels=16)
    for i in range(-100, 100, 5):
        kit.continuous_servo[0].throttle = i/100
        kit.continuous_servo[1].throttle = -i/100
        time.sleep(0.1)
    for i in range(100, -100, -5):
        kit.continuous_servo[0].throttle = i/100
        kit.continuous_servo[1].throttle = -i/100
        time.sleep(0.01)
    kit.continuous_servo[0].throttle = 0.1
    kit.continuous_servo[1].throttle = 0.1
    
        
    


if __name__ == '__main__':
    high_low()
