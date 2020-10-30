import RPi.GPIO as GPIO          
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
ena = 24
in1 = 25
in2 = 12

in3 = 16
in4 = 20
enb = 21

GPIO.setup(enb, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
pwm2 = GPIO.PWM(enb, 20)

GPIO.setup(ena, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
pwm1 = GPIO.PWM(ena, 20)

while True:
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(ena, GPIO.HIGH)
    pwm1.start(100)
   
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(enb, GPIO.HIGH)
    pwm2.start(100)
   
