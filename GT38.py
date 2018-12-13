# GT-38 Class
# need power
import serial
import time
import RPi.GPIO as GPIO

class GT38:
    speed = 0
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
        self.parseAnswer(self.receive())
        self.parseAnswer(self.receive())
        self.parseAnswer(self.receive())
        self.parseAnswer(self.receive())
        GPIO.output(self.setPin, GPIO.HIGH)
        return True

    def reset (self):
        self.wirelessCommunication.baudrate = 9600
        GPIO.output(self.setPin, GPIO.LOW)
        time.sleep (.1)

        request="AT+DEFAULT\r\n"
#       print (request)
        self.sendToDevice(request)
        self.parseAnswer(self.receive())
        GPIO.output(self.setPin, GPIO.HIGH)
        
    def setSpeed(self, newSpeed):
        self.wirelessCommunication.baudrate = 9600
        GPIO.output(self.setPin, GPIO.LOW)
        time.sleep (.1)
        if (isinstance(newSpeed, int)):
            request="AT+B"+str(newSpeed)+"\r\n"
#            print (request)
            self.sendToDevice(request)
            if (self.parseAnswer(self.receive())):
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
            if (self.parseAnswer(self.receive())):
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
            if (self.parseAnswer(self.receive())):
                GPIO.output(self.setPin, GPIO.HIGH)
                return True
            else:
                GPIO.output(self.setPin, GPIO.HIGH)
                return False
        else:
            GPIO.output(self.setPin, GPIO.HIGH)
            return False

    def receive(self):
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

    def parseAnswer(self, GT38response):
#        print ('Answer', GT38response)
        if (GT38response[0:5] == ' OK+B'):
            self.speed = int(GT38response[5:])
            return True
        if (GT38response[0:5] == ' OK+C'):
            self.channel = int(GT38response[5:])
            return True
        if (GT38response[0:6] == ' OK+FU'):
            self.mode = int(GT38response[6:])
            return True
        if (GT38response[0:7] == ' OK+RP:'):
            self.power = GT38response[7:-2]
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

    def send (self, message):
        self.wirelessCommunication.baudrate = self.speed
        return self.sendToDevice(message)
