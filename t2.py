from gpiozero import LED
from time import sleep

red = LED(2)
green = LED(3)
blue = LED(4)

red.on()
green.on()
blue.on()

sleep(5)

red.off()
green.off()
blue.off()

sleep(5)

while True:
    red.on()
    green.on()
    blue.on()
    sleep(1)
    red.off()
    green.off()
    blue.off()
    sleep(1)