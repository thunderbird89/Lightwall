#import record types for use in RGB array
from recordtype import recordtype

#create RGB array
color = recordtype('color', 'R G B', default=255)
rgb = color()

print ('Enter color values')
print ('red:', end=' ')
rgb.R = input()
print ('green:', end=' ')
rgb.G = input()
print ('blue:', end=' ')
rgb.B = input()
print (rgb)


##import wiring interface, set up clock and data lines
#import wiringpi
#wiringpi.wiringPiSetupGPIO
#wiringpi.pinMode(1,1)       #Pin 1 - Clock
#wiringpi.pinMode(2,1)       #Pin 2 - Data 1
#wiringpi.pinMode(3,1)       #Pin 3 - Data 2
#wiringpi.pinMode(4,1)       #Pin 4 - Data 3
#wiringpi.pinMode(5,1)       #Pin 5 - Data 4

##Clock function: send one pulse every 250us (register latches on 500us clock low)
#def clock():
#    while trigger == 1:
#            wiringpi.digitalWrite(1,1)
#            wiringpi.delayMicroseconds(250)
#            wiringpi.digitalWrite(1,0)
#            wiringpi.delayMicroseconds(250)

##Import threading and set up clock and comm threads
#import threading
#threading.Thread(None, None, clock)
