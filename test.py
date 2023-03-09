from gpiozero import LED
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
    led.append(LED(i))

led[0].on()
