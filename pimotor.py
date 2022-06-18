import time
import math
import qwiic_pca9685
import pi_servo_hat

# Device Name:
_DEFAULT_NAME = "Pi Servo HAT"

# Fixed Address:
_AVAILABLE_I2C_ADDRESS = [0x40]

# Default Servo Frequency:
_DEFAULT_SERVO_FREQUENCY = 50   # Hz

# Special Use Addresses:
gcAddr = 0x00       # General Call address for software reset
acAddr = 0x70       # All Call address- used for modifications to
                    # multiple PCA9685 chips reguardless of thier
                    # I2C address set by hardware pins (A0 to A5).
subAddr_1 = 0x71    # 1110 001X or 0xE2 (7-bit)
subAddr_2 = 0x72    # 1110 010X or 0xE4 (7-bit)
subAddr_3 = 0x74    # 1110 100X or 0xE8 (7-bit)

test = pi_servo_hat.PiServoHat()
test.restart()

# Moves servo position to 0 degrees (1ms), Channel 0
test.move_servo_position(0, 0)

# Pause 1 sec
time.sleep(1)

# Moves servo position to 90 degrees (2ms), Channel 0
test.move_servo_position(0, 90)

# Pause 1 sec
time.sleep(1)

test.restart()
