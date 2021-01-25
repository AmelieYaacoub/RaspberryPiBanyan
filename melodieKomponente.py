import RPi.GPIO as GPIO

class Constants:
    def __init__(self):
        self.C1 = 12
        self.B = 16
        self.A = 18
        self.G = 22
        self.F = 32
        self.E = 36
        self.D = 38
        self.C = 40


constants = Constants()



GPIO.setmode(GPIO.BOARD)

GPIO.setup(constants.C1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(constants.B,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(constants.A,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(constants.G,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(constants.F,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(constants.E,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(constants.D,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(constants.C,GPIO.IN,pull_up_down=GPIO.PUD_UP)

val=0

try:
    while True:
        val=val+1
        if (GPIO.input(constants.C1)==0):
            print('C1 Pressed', val)
        elif (GPIO.input(constants.B)==0):
            print('B Pressed', val)
        elif (GPIO.input(constants.A)==0):
            print('A Pressed', val)
        elif (GPIO.input(constants.G)==0):
            print('G Pressed', val)
        elif (GPIO.input(constants.F)==0):
            print('F Pressed', val)
        elif (GPIO.input(constants.E)==0):
            print('E Pressed', val)
        elif (GPIO.input(constants.D)==0):
            print('D Pressed', val)
        elif (GPIO.input(constants.C)==0):
            print('C Pressed', val)
            
        
        else:
            print('Not pressed :(', val)
            
except KeyboardInterrupt:
    GPIO.cleanup()