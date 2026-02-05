#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import RPi.GPIO as GPIO

# ============================================
# CONFIGURATION - Change this to your GPIO pin
# ============================================
SOLENOID_PIN = 21


class SolenoidController(Node):
    def __init__(self):
        super().__init__('solenoid_controller')
        
        # Setup the GPIO pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SOLENOID_PIN, GPIO.OUT)
        GPIO.output(SOLENOID_PIN, GPIO.LOW)  # Start OFF


        print(f'✓ Ready! Listening on GPIO pin {SOLENOID_PIN}')
        
    def when_command_received(self, msg):
        command = msg.data.lower()
        
        if command == 'yes':
            GPIO.output(SOLENOID_PIN, GPIO.HIGH)  # Turn ON
            print('💡 Solenoid ON')
        elif command == 'no':
            GPIO.output(SOLENOID_PIN, GPIO.LOW)   # Turn OFF
            print('⚫ Solenoid OFF')
    
    def cleanup(self):
        GPIO.output(SOLENOID_PIN, GPIO.LOW)
        GPIO.cleanup()


def main():
    


if __name__ == '__main__':
    main()
