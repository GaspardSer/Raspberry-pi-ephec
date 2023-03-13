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
led = []
for i in [4,5,6,13,19,26]:
    led.append(i)

LED(4).blink()
sleep(1)
LED(5).blink()
sleep(1)
LED(6).blink()
sleep(1)
LED(13).blink()
sleep(1)
LED(19).blink()
sleep(1)
LED(26).blink()
sleep(1)


"""button1 = Button(23)
button2 = Button(24)
while True:
    if button1.is_pressed() == True:
        led[0].on()
    else:
        led[0].off()"""
