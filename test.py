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
    if button2.is_pressed:
        return 1
    green_led2.on()
    
def blink_sequence_reversed():
    for i in reversed(range(len(leds))):
        leds[i].on()
        sleep(0.2)
        leds[i].off()
    if button1.is_pressed:
        return 1
    green_led1.on()

def blink_3_times():
    for i in range(3):
        green_led1.on()
        green_led2.on()
        sleep(0.5)
        green_led1.off()
        green_led2.off()
        sleep(0.5)
        

def play_round_p1():
    round = blink_sequence()
    if round == 1:
        "P2 Hit too soon"
        return 1
    start_time = time()
    while time() - start_time < 0.2:
        if button2.is_pressed:
            print("P2 HIT")
            return 2

def play_round_p2():
    round = reversed_blink_sequence()
    if round == 1:
        "P1 Hit too soon"
        return 1
    start_time = time()
    while time() - start_time < 0.2:
        if button2.is_pressed:
            print("P1 HIT")
            return 2
def play():
    blink_3_times()
    while True:
        result = play_round_p1()
        green_led2.off()
        if result == 1:
            print("P1 WINS")
        elif result == 2:
            result = play_round_p2()
            green_led1.off()
            if result == 1:
                print("P2 WINS")
            

play()

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