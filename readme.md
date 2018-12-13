# GT-38 Wireless Communication Module Driver

This driver is designed to help using a GT-38 Wireless Communication Module with a Raspberry PI (zero or 3) and its GPIO.

# How to connect the GT-38 to your raspberry GPIO
GT-38 Pin -> RASPBERRY GPIO Pin
VCC -> 3.3V
GND -> GROUND
RX -> TX (pin 9)
TX -> RX (pin 10)
SET -> a pin to be chosen

# How to use the class

Import the class 
example
'from GT38 import GT38'

Call the class like GT38 (SetPin)
example
'comModule = GT38(6)'
# Parameters
speed
mode


# Methods
__getParams()__
will set class internal parameters corresponding to the module speed, power, mode, channel

__setSpeed(speed)__
speed : int
??? could be 1200, 2400, 4800, 9600

internal Parameter Speed is set

_returns_
True : Mode is Changed
False : Mode is not Changed

__setMode(mode)__
mode : int
??? could be 1, 2, 3, 4

internal Parameter Mode is set

_returns_
True : Mode is Changed
False : Mode is not Changed

__setChannel(channel)__
channel : int
??? between 1 and 120 

internal Parameter Channel is set

_returns_
True : Channel is Changed
False : Channel is not Changed

__send(message)__
message : string
The method will add the special character '\n'

_returns_
True : Message is sent
False : Message is not sent
