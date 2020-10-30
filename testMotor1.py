import RPi.GPIO as GPIO          
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
ena = 24
in1 = 25
in2 = 12



GPIO.setup(ena, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
pwm1 = GPIO.PWM(ena, 20)




while (True):
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(ena, GPIO.HIGH)
    pwm1.start(100)
  
    


 

