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
from gpiozero import LED, Button
from time import sleep, time
import random

#num = random.randint(1, 2)


# Initialize LED and button objects for each LED/button on the board
green_led1 = LED(4)
yellow_led1 = LED(5)
yellow_led2 = LED(6)
yellow_led3 = LED(13)
yellow_led4 = LED(19)
green_led2 = LED(26)
button1 = Button(23)
button2 = Button(24)

# Set up a list of LEDs to be used for the ping pong game
leds = [green_led1, yellow_led1, yellow_led2, yellow_led3, yellow_led4, green_led2]

# Define a function to blink the LEDs in sequence
def blink_sequence():
    for i in range(len(leds)):
        leds[i].on()
        sleep(0.2)
        leds[i].off()
    
def blink_sequence_reversed():
    for j in reversed(range(len(leds))):
        leds[j].on()
        sleep(0.2)
        leds[j].off()

def blink_3_times():
    for i in range(3):
        green_led1.on()
        green_led2.on()
        sleep(0.5)
        green_led1.off()
        green_led2.off()
        

# Define a function to play a round of ping pong
def play_round():
    blink_3_times()
    blink_sequence()
    green_led1.on()
    green_led2.on()
    start_time = time()
    while True:
        if button1.is_pressed and green_led1.is_lit:
            print("Player 1 wins!")
            return 1
        elif button2.is_pressed and green_led2.is_lit:
            print("Player 2 wins!")
            return 2
        elif time() - start_time > 1:
            print("Time's up!")
            return 0

# Play the game of ping pong
while True:
    result = play_round()
    if result == 1:
        print("Player 1 scores!")
    elif result == 2:
        print("Player 2 scores!")
    else:
        print("No one scores!")

"""
In this code, the blink_sequence() function is used to blink the LEDs in sequence, which creates the visual effect of the line of LEDs
moving from one end to the other. The play_round() function is used to play a round of ping pong, where the green LEDs light up and 
the players must press their buttons in time to win the round. Finally, the main loop of the program plays the game of ping pong indefinitely,
printing out the scores for each round. Note that this is just an example implementation and you may need to modify the code to fit your 
specific setup.
"""