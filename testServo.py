from gpiozero import Servo
from time import sleep

servo = Servo(26)

while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)
    servo.mid()
    sleep(1)