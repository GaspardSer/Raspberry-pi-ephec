from gpiozero import LED, Button
import time

led = [4, 5, 6, 13, 19, 26]


def onOff(led, t):
    led.on()
    time.sleep(t)
    led.off()


#while True:
if Button(23).is_pressed() == True:
    for i in led:
        onOff(LED(i), 0.1)
if Button(24).is_pressed() == True:
    for j in reversed(led):
        onOff(LED(j), 0.1)


"""button1 = Button(23)
button2 = Button(24)
while True:
    if button1.is_pressed() == True:
        led[0].on()
    else:
        led[0].off()"""
