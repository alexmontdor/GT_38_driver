# GT-38 Driver
# need power
import serial
import time
import RPi.GPIO as GPIO

class GT38:
    def __init__ (self, pin):
        self.setPin = pin
        # Setting the Communication to 
        self.wirelessCommunication = serial.Serial(
            port='/dev/ttyS0',
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
        GPIO.setup(self.setPin, GPIO.OUT) # Set pin set as output

    def getParams (self):
        self.wirelessCommunication.baudrate = 9600
        GPIO.output(self.setPin, GPIO.LOW)
        time.sleep (.1)
#        print ('Getting GT-38 Params')
        request = "AT+RX\r\n"
        self.sendToDevice(request)
        self.parseAnswer(self.receiveFromDevice())
        self.parseAnswer(self.receiveFromDevice())
        self.parseAnswer(self.receiveFromDevice())
        self.parseAnswer(self.receiveFromDevice())
        GPIO.output(self.setPin, GPIO.HIGH)
        return True

    def reset (self):
        self.wirelessCommunication.baudrate = 9600
        GPIO.output(self.setPin, GPIO.LOW)
        time.sleep (.1)

        request="AT+DEFAULT\r\n"
#       print (request)
        self.sendToDevice(request)
        self.parseAnswer(self.receiveFromDevice())
        GPIO.output(self.setPin, GPIO.HIGH)
        
    def setSpeed(self, newSpeed):
        self.wirelessCommunication.baudrate = 9600
        GPIO.output(self.setPin, GPIO.LOW)
        time.sleep (.1)
        if (isinstance(newSpeed, int)):
            request="AT+B"+str(newSpeed)+"\r\n"
#            print (request)
            self.sendToDevice(request)
            if (self.parseAnswer(self.receiveFromDevice())):
                GPIO.output(self.setPin, GPIO.HIGH)
                return True
            else:
                GPIO.output(self.setPin, GPIO.HIGH)
                return False
        else:
            GPIO.output(self.setPin, GPIO.HIGH)
            return False
     
    def setMode(self, newMode):
        self.wirelessCommunication.baudrate = 9600
        GPIO.output(self.setPin, GPIO.LOW)
        time.sleep (.1)
        if (isinstance(newMode, int)):
            request="AT+FU"+str(newMode)+"\r\n"
#            print (request)
            self.sendToDevice(request)
            if (self.parseAnswer(self.receiveFromDevice())):
                GPIO.output(self.setPin, GPIO.HIGH)
                return True
            else:
                GPIO.output(self.setPin, GPIO.HIGH)
                return False

        else:
            GPIO.output(self.setPin, GPIO.HIGH)
            return False

    def setChannel(self, newChannel):
        self.wirelessCommunication.baudrate = 9600
        GPIO.output(self.setPin, GPIO.LOW)
        time.sleep (.1)
        if (isinstance(newChannel, int)):
            request="AT+C"+str(newChannel)+"\r\n"
#            print (request)
            self.sendToDevice(request)
            if (self.parseAnswer(self.receiveFromDevice())):
                GPIO.output(self.setPin, GPIO.HIGH)
                return True
            else:
                GPIO.output(self.setPin, GPIO.HIGH)
                return False
        else:
            GPIO.output(self.setPin, GPIO.HIGH)
            return False

    def receiveFromDevice(self):
        # get the answer from GT38
        #time.sleep(.1)
        # Waiting for a line to receive
        answer=""
        counter=0
        #time.sleep(1)
        while True:
            answer=self.wirelessCommunication.read_until('\n')
            
            if ((answer =="" or answer =='\r\n' or answer =='\n') and counter<10):
                if (counter>6):
                    print ("attempt "+ str(counter))
                counter +=1
            else:
                break
        return answer

    def parseAnswer(self, GT38Response):
#        print ('Answer', GT38response)
        if (GT38Response[0:4] == ' OK+'):
            answer = GT38Response[4:].split(',')
            for index in range (len(answer)):
                if (answer[index][0:1]=='B'):
                    self.speed = int(answer[index][1:])
                if (answer[index][0:1] == 'C'):
                    self.channel = int(answer[index][1:])
                if (answer[index][0:2] == 'FU'):
                    self.mode = int(answer[index][2:])
                if (answer[index][0:3] == 'RP:'):
                    self.power = answer[index][3:-2]
                if (answer[index][0:7] == 'DEFAULT'):
                    self.getParams()
            return True
        return False

    def sendToDevice (self, message):
        if (isinstance(message, str)):
            if (message[-1:]!='\n'):
                message= message+"\n"
            self.wirelessCommunication.write (message)
            return True
        else:
            return False

    def displayParameters(self):
        print ('Speed '+ str(self.speed))
        print ('Mode '+ str(self.mode))
        print ('Channel '+ str(self.channel))
        print ('Power '+ self.power)

    def send (self, message):
        self.wirelessCommunication.baudrate = self.speed
        return self.sendToDevice(message)

    def receive(self):
        self.wirelessCommunication.baudrate = self.speed
        return self.receiveFromDevice()
        
