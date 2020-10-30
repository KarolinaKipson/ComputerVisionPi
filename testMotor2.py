import RPi.GPIO as GPIO          
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

in3 = 16
in4 = 20
enb = 21

GPIO.setup(enb, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
pwm2 = GPIO.PWM(enb, 20)

while True:
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(enb, GPIO.HIGH)
    pwm2.start(100)
