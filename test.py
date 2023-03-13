from gpiozero import LED
import time

led = [4, 5, 6, 13, 19, 26]


def onOff(led, t):
    led.on()
    time.sleep(t)
    led.off()
    time.sleep(t)


while True:
    for i in led:
        onOff(LED(i), 2)

"""button1 = Button(23)
button2 = Button(24)
while True:
    if button1.is_pressed() == True:
        led[0].on()
    else:
        led[0].off()"""
