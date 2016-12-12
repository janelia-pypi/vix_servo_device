'''
This Python package (vix_servo_device) creates a class named
VixServoDevice, which contains an instance of
serial_device2.SerialDevice and adds methods to it to interface to
Vix Servo balances and scales that use the Vix Servo
Standard Interface Command Set (MT-SICS).
'''
from .vix_servo_device import VixServoDevice, VixServoDevices, VixServoError, find_vix_servo_device_ports, find_vix_servo_device_port, __version__
