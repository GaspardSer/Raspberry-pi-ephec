from gpiozero import LED, Button
from time import sleep
"""
led1 = LED(4)
led2 = LED(5)
led3 = LED(6)
led4 = LED(13)
led5 = LED(19)
led6 = LED(26)
"""
led = [LED(4), LED(5), LED(6), LED(13), LED(19), LED(26)]
#for i in [4,5,6,13,19,26]:
#    led.append(LED(i))

while True:
    for i in led:
        i.blink()
        sleep(1)

button1 = Button(23)
button2 = Button(24)
while True:
    if button1.is_pressed() == True:
        led[0].on()
    else:
        led[0].off()
