from gpiozero import LED
import time

led = [4, 5, 6, 13, 19, 26]

def onOff(led, t):
    led.on()
    time.sleep(t)
    led.off()
    time.sleep(t)


while True:
    onOff(LED(4), 2)
    onOff(LED(5), 2)
    onOff(LED(6), 2)
    onOff(LED(13), 2)
    onOff(LED(19), 2)
    onOff(LED(26), 2)

"""button1 = Button(23)
button2 = Button(24)
while True:
    if button1.is_pressed() == True:
        led[0].on()
    else:
        led[0].off()"""
