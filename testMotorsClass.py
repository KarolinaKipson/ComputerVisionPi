import RPi.GPIO as GPIO          
from time import sleep

GPIO.setmode(GPIO.BCM)

class Motor():
  def __init__(self, ena, in1, in2):
    self.ena = ena
	self.in1 = in1
	self.in2 = in2
	GPIO.setup(self.ena, GPIO.OUT)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        self.pwm = GPIO.PWM(self.ena, 100)
	self.pwm.start(0)
  def forward(self, speed = 50, sleepTime = 0):
    GPIO.output(self.in1, GPIO.LOW)
    GPIO.output(self.in2, GPIO.HIGH)
    self.pwm.ChangeDutyCycle(speed)
    sleep(sleepTime)
  def reverse(self, speed = 50, sleepTime = 0):
    GPIO.output(self.in1, GPIO.HIGH)
    GPIO.output(self.in2, GPIO.LOW)
    self.pwm.ChangeDutyCycle(speed)
    sleep(sleepTime)
  def stop(self, sleepTime = 0):
    GPIO.output(self.in1, GPIO.LOW)
    GPIO.output(self.in2, GPIO.LOW)
    self.pwm.ChangeDutyCycle(0)
    sleep(sleepTime)

motor1 = Motor(24, 25, 12)
motor2 = Motor(21, 16, 20)

while True:
    motor1.forward(100, 3)
    motor2.forward(100, 3)
    motor1.reverse(100, 3)
    motor2.reverse(100, 3)
    motor1.stop(2)
    motor2.stop(2)
