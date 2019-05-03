#BotTest
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Motor2A= 13
Motor2B= 19
Motor2E= 26
Motor1A= 23
Motor1B= 24
Motor1E= 25
pi=3.1415
diam=6.5
dbw=18.5
time_rot=0.26
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

def stop_motors():
        GPIO.output(Motor1E,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.LOW)
def move_forward(dist):
        radius=diam/2
        time_req=((dist)/(2*pi*radius))*time_rot
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)
        sleep(time_req)
        stop_motors()
def move_backward(dist):
        radius=diam/2
 time_req=((dist)/(2*pi*radius))*time_rot
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.HIGH)
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.HIGH)
        sleep(time_req)
        stop_motors()
def turn_clockwise(angle):
        arc=angle*dbw
        radius=diam/2
        time_req=((arc)/(2*pi*radius))*time_rot
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)
        sleep(time_req)
        stop_motors()
def turn_anticlockwise(angle):
        arc=angle*dbw
        radius=diam/2
        time_req=((arc)/(2*pi*radius))*time_rot
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)
        sleep(time_req)
        stop_motors()
if __name__=="__main__":
        sleep(3)
        angle1=pi/3
        angle2=((pi/18.0)*14.0)
        move_forward(50)
        turn_anticlockwise(angle1)
        move_forward(30)
        turn_anticlockwise(angle2)
        move_forward(70)
        stop_motors()

        GPIO.cleanup()
