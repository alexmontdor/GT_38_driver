# GT-38 wireless communication Module class

This class is designed to communicate with a GT-38 and a Raspberry PI (zero or 3)

# How to link the GT-38 to your raspberry GPIO
GT-38 -> RASPBERRY GPIO
VCC -> 3.3V
GND -> GROUND
RX -> TX
TX -> RX
SET -> a pin to be chosen

# How to use the class

Import the class 
example
'import as'

Call the class like GT38 (SetPin)
example
'comModule = GT38(6)'

# Method
setSpeed ()
return :
True : speed Changed
False : speed no Changed

getParams()
will set class internal parameters corresponding to the module speed, power, mode, channel

setSpeed(speed)
speed : int
??? could be 1200, 2400, 4800, 9600

setMode(mode)
mode : int
??? could be 1, 2, 3, 4

setChannel(channel)
channel : int
??? between 1 and 120 

send(message)
message : string
The method will add the special character '\n'