import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

south=[2,3,4]
west=[14,15,18]
north=[17,27,22]
east=[23,24,25]
red=[2,14,17,23]
yellow=[3,15,27,24]
green=[4,18,22,25]

all=south+west+north+east

def initialize():
    for led in all:
        GPIO.setup(led,GPIO.OUT)

def reset_all():
    for led in all:
        GPIO.output(led,GPIO.LOW)


def all_yellow():
    for led in yellow:
        GPIO.output(led,GPIO.HIGH)


def north_south_red():
    GPIO.output(north[0],GPIO.HIGH)
    GPIO.output(south[0],GPIO.HIGH)

def north_south_green():
    GPIO.output(north[2],GPIO.HIGH)
    GPIO.output(south[2],GPIO.HIGH)

def west_est_red():
    GPIO.output(west[0],GPIO.HIGH)
    GPIO.output(east[0],GPIO.HIGH)

def west_est_green():
    GPIO.output(west[2],GPIO.HIGH)
    GPIO.output(east[2],GPIO.HIGH)



initialize()
reset_all()


