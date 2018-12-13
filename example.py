# example how to GT-38 class
from GT38 import GT38

ComModule = GT38(6)
def displayParams():
    global ComModule
    print ('speed', ComModule.speed)
    print ('power', ComModule.power)
    print ('channel',ComModule.channel)
    print ('mode',ComModule.mode)

if (ComModule.getParams()):
    print ("params downloaded")
    displayParams()
else:
    print ("error while getting params")

#ComModule.setSpeed(4800)
print ('------ MODE 1')
ComModule.setMode(1)
ComModule.getParams()
displayParams()

print ('------ MODE 3')
ComModule.setMode(3)
ComModule.getParams()
displayParams()

print ('------ SPEED 4800')
ComModule.setSpeed(4800)
ComModule.getParams()
displayParams()

print ('------ CHANNEL 23')
ComModule.setChannel(23)
ComModule.getParams()
displayParams()

print ('------ RESET')
ComModule.reset()
ComModule.getParams()
displayParams()

print ('------ SENDING')
if (ComModule.send("sending on the channel")):
    print ('Sent')
else:
    print ('Not sent')