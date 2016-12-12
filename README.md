#vix_servo_device_python

This Python package (vix\_servo\_device) creates a class named
VixServoDevice, which contains an instance of
serial\_device2.SerialDevice and adds methods to it to interface to
Vix Servo balances and scales that use the Vix Servo
Standard Interface Command Set (MT-SICS).

Authors:

    Peter Polidoro <polidorop@janelia.hhmi.org>

Contributors:

    James Pells <https://github.com/jpells>
    Roger Zatkoff <https://github.com/rpzatkoff>

License:

    BSD

##Vix Servo RS232 Setup

| BAUDRATE | BIT/PARITY | STOP BITS | HANDSHAKE | END OF LINE  | CHAR SET | CONTINUOUS MODE |
| :-:      | :-:        | :-:       | :-:       | :-:          | :-:      | :-:             |
| 9600     | 8/NO       | 1         | NONE      | \<CR\>\<LF\> | ANSI/WIN | OFF             |

##Example Usage


```python
from vix_servo_device import VixServoDevice
dev = VixServoDevice() # Might automatically find device if one available
# if it is not found automatically, specify port directly
dev = VixServoDevice(port='/dev/ttyUSB0') # Linux specific port
dev = VixServoDevice(port='/dev/tty.usbmodem262471') # Mac OS X specific port
dev = VixServoDevice(port='COM3') # Windows specific port
dev.get_serial_number()
1126493049
dev.get_balance_data()
['XS204', 'Excellence', '220.0090', 'g']
dev.get_weight_stable()
[-0.0082, 'g'] #if weight is stable
None  #if weight is dynamic
dev.get_weight()
[-0.6800, 'g', 'S'] #if weight is stable
[-0.6800, 'g', 'D'] #if weight is dynamic
dev.zero_stable()
True  #zeros if weight is stable
False  #does not zero if weight is not stable
dev.zero()
'S'   #zeros if weight is stable
'D'   #zeros if weight is dynamic
```

```python
devs = VixServoDevices()  # Might automatically find all available devices
# if they are not found automatically, specify ports to use
devs = VixServoDevices(use_ports=['/dev/ttyUSB0','/dev/ttyUSB1']) # Linux
devs = VixServoDevices(use_ports=['/dev/tty.usbmodem262471','/dev/tty.usbmodem262472']) # Mac OS X
devs = VixServoDevices(use_ports=['COM3','COM4']) # Windows
dev = devs[0]
```

##Installation

[Setup Python](https://github.com/janelia-pypi/python_setup)

###Linux and Mac OS X

```shell
mkdir -p ~/virtualenvs/vix_servo_device
virtualenv ~/virtualenvs/vix_servo_device
source ~/virtualenvs/vix_servo_device/bin/activate
pip install vix_servo_device
```

###Windows

```shell
virtualenv C:\virtualenvs\vix_servo_device
C:\virtualenvs\vix_servo_device\Scripts\activate
pip install vix_servo_device
```
