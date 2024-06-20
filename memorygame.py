from gpiozero import LED
from gpiozero import Button
from time import sleep
import random

blueled = LED(4)
whiteled = LED(2)
redled = LED(20)
bluebutton = Button(3)
redbutton = Button(21)
whitebutton = Button(16)

def playGame():
    redled.off()
    whiteled.off()
    blueled.off()

    redwin = False
    bluewin = False
    time = random.uniform(3, 6)
    sleep(time)

    whiteled.on()

    while True:
        if bluebutton.is_pressed:
            bluewin = True
            print("blue wins!")
            break
        if redbutton.is_pressed:
            redwin = True
            print("red wins!")
            break

    if redwin:
        for x in range(10):
            redled.on()
            sleep(.25)
            if whitebutton.is_pressed:
                break
            redled.off()
            sleep(.25)
            if whitebutton.is_pressed:
                break
    if bluewin:
        for x in range(10):
            blueled.on()
            sleep(.25)
            if whitebutton.is_pressed:
                break
            blueled.off()
            sleep(.25)
            if whitebutton.is_pressed:
                break


while True:
    redled.on()
    whiteled.off()
    blueled.on()
    sleep(1)
    whiteled.on()
    print("Press the middle button to start!")
    whitebutton.wait_for_press()
    playGame()