import pi_servo_hat
import time

def test_motor():
    # Moves servo position to 0 degrees (1ms), Channel 0
    test.move_servo_position(0, 0, 180)
    time.sleep(1)
    # Moves servo position to 180 degrees (2ms), Channel 0
    test.move_servo_position(0, 180, 180)
    time.sleep(1)



def move_motor(motor, freq, pos):
    test.set_pwm_frequency(freq)
    test.move_servo_position(motor, pos, 180)
    time.sleep(0.01)

if __name__ == '__main__':
    # Initialize Constructor
    test = pi_servo_hat.PiServoHat()
    # Restart Servo Hat (in case Hat is frozen/locked)
    test.restart()
    #test_motor()
    move_motor(0, 200, 120)
    move_motor(1, 100, 50)
    
    
    test.restart()





