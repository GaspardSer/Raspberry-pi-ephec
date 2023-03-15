from flask import Flask
from gpiozero import LED, Button
from time import sleep, time

app = Flask(__name__)

green_led1 = LED(4)
yellow_led1 = LED(5)
yellow_led2 = LED(6)
yellow_led3 = LED(13)
yellow_led4 = LED(19)
green_led2 = LED(26)
button1 = Button(23)
button2 = Button(24)

leds = [yellow_led1, yellow_led2, yellow_led3, yellow_led4]

@app.route('/')
def index():
    # note: les 3 guillemets permetent de définir une chaine de charactère multi-ligne
    return """
<!DOCTYPE html>
<html>
<head>
<style>
.button {
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 50px;
  transition-duration: 0.4s;
  cursor: pointer;
  color: black;
  border: 2px solid #4CAF50;
}
.button:hover {
  background-color: #4CAF50;
  color: white;
}
</style>
</head>
<body>
<h1>Play Ping Pong/h1>
<a href="/ping pong" class="button">Play</a>
</body>
</html>
"""


@app.route('/pingpong')
def play_website():
    play(0.5)
    return redirect('/')
def blink_sequence(t):
    for i in range(len(leds)):
        leds[i].on()
        sleep(t)
        leds[i].off()
    if button2.is_pressed:
        return 1
    green_led2.on()
    
def blink_sequence_reversed(t):
    for i in reversed(range(len(leds))):
        leds[i].on()
        sleep(t)
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
        

def play_round_p1(t):
    round = blink_sequence(t)
    if round == 1:
        print("P2 Hit too soon")
        return 1
    start_time = time()
    while time() - start_time < t:
        if button2.is_pressed:
            print("P2 HIT")
            return 2
    return 1


def play_round_p2(t):
    round = blink_sequence_reversed(t)
    if round == 1:
        print("P1 Hit too soon")
        return 1
    start_time = time()
    while time() - start_time < t:
        if button1.is_pressed:
            print("P1 HIT")
            return 2
    return 1


def play(t):
    blink_3_times()
    while True:
        result = play_round_p1(t)
        green_led2.off()
        if result == 1:
            print("P1 WINS")
            break
        elif result == 2:
            result = play_round_p2(t)
            green_led1.off()
            if result == 1:
                print("P2 WINS")
                break


app.run(host='0.0.0.0', port=8000, debug=True)