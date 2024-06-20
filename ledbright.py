from gpiozero import PWMLED
from time import sleep

led = PWMLED(2)

while True:
    for x in range(0, 101):
        led.value = x / 100
        print(x / 100)
        sleep(.01)
    for x in range(100, -1, -1):
        led.value = x / 100
        print(x / 100)
        sleep(.01)