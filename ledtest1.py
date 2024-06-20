from gpiozero import LED
from gpiozero import Button
from time import sleep
red = LED(2)
yellow = LED(3)
green = LED(4)
button = Button(21)

while True:
    red.off()
    yellow.off()
    green.on()
    sleep(1)
    button.wait_for_press()
    green.off()
    yellow.on()
    sleep(3)
    yellow.off()
    red.on()
    button.wait_for_press()