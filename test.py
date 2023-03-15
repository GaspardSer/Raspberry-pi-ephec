from gpiozero import LED, Button
from time import sleep, time

#num = random.randint(1, 2)

green_led1 = LED(4)
yellow_led1 = LED(5)
yellow_led2 = LED(6)
yellow_led3 = LED(13)
yellow_led4 = LED(19)
green_led2 = LED(26)
button1 = Button(23)
button2 = Button(24)

leds = [yellow_led1, yellow_led2, yellow_led3, yellow_led4]

def blink_sequence():
    for i in range(len(leds)):
        leds[i].on()
        sleep(0.2)
        leds[i].off()
    green_led2.on()
    sleep(0.2)
    green_led2.off()
    
def blink_sequence_reversed():
    for i in reversed(range(len(leds))):
        leds[i].on()
        sleep(0.2)
        leds[i].off()
    green_led1.on()
    sleep(0.2)
    green_led1.off()

def blink_3_times():
    for i in range(3):
        green_led1.on()
        green_led2.on()
        sleep(0.5)
        green_led1.off()
        green_led2.off()
        sleep(0.5)
        

def play_round():
    blink_3_times()
    while True:
        blink_sequence()
        green_led2.on()
        sleep(0.2)
        #blink_sequence_reversed()
        if button1.is_pressed and green_led1.is_lit:
            print("Player 1 wins!")
            return 1
        if button2.is_pressed and green_led2.is_lit:
            print("Player 2 wins!")
            return 2
            """

while True:
    result = play_round()
    if result == 1:
        print("Player 1 scores!")
    elif result == 2:
        print("Player 2 scores!")
    else:
        print("No one scores!")

"""

from gpiozero import LED, Button
import time

led = [4, 5, 6, 13, 19, 26]
button1 = Button(23)
button2 = Button(24)

def onOff(led, t):
    led.on()
    time.sleep(t)
    led.off()


while True:
    if button1.is_pressed():
        for i in led:
            onOff(LED(i), 0.1)
    if button2.is_pressed():
        for j in reversed(led):
            onOff(LED(j), 0.1)


button1 = Button(23)
button2 = Button(24)
while True:
    if button1.is_pressed() == True:
        led[0].on()
    else:
        led[0].off()
"""