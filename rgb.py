from gpiozero import PWMLED
from time import sleep

red = PWMLED(2)
green = PWMLED(3)
blue = PWMLED(4)

red.value = 0
green.value = 0
for x in range(0, 101):
    blue.value = x / 100
    sleep(.02)

def setValue(j):
    if j <= 100:
        red.value = j / 100
    elif j <= 200:
        blue.value = 1 - ((j - 100) / 100)
    elif j <= 300:
        green.value = (j - 200) / 100
    elif j <= 400:
        red.value = 1 - ((j - 300) / 100)
    elif j <= 500:
        blue.value = (j - 400) / 100
    elif j <= 600:
        green.value = 1 - ((j - 500) / 100)
    sleep(.02)

i = 1

while True:
    #red up
    #blue down
    #green up
    #red down
    #blue up
    #green down
    setValue(i)
    i += 1
    if i > 600:
        i = 1