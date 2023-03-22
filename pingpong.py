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
<!doctype html>
<html>
    <head>
        <style>

        html {
            background-color: rgb(16, 9, 44);
        }
        .button-64 {
            align-items: center;
            background-image: linear-gradient(144deg,#AF40FF, #5B42F3 50%,#00DDEB);
            border: 0;
            border-radius: 8px;
            box-shadow: rgba(151, 65, 252, 0.2) 0 15px 30px -5px;
            box-sizing: border-box;
            color: #FFFFFF;
            display: flex;
            font-family: Phantomsans, sans-serif;
            font-size: 20px;
            justify-content: center;
            line-height: 1em;
            max-width: 100%;
            min-width: 140px;
            padding: 3px;
            text-decoration: none;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
            white-space: nowrap;
            cursor: pointer;
            }

        .button-64:active, .button-64:hover {
            outline: 0;
        }

        .button-64 span {
            background-color: rgb(5, 6, 45);
            padding: 16px 24px;
            border-radius: 6px;
            width: 100%;
            height: 100%;
            transition: 300ms;
        }

        .button-64:hover span {
            background: none;
        }

        @media (min-width: 768px) {
        .button-64 {
                font-size: 100px;
                min-width: 400px;
            }
        }

        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 200px;
            }

        h1{
            text-align: center;
            font-size: 100px;
            color:  white;
        }
    </style>
        <title>Ping Pong</title>
    </head>
    <body>
        <h1>Ping Pong</h1>
        <form action="/play" method="post">
            <div class="center">
                <button class="button-64" role="button"><span class="text">Press to play</span></button>
                    <!--Button from https://getcssscan.com/css-buttons-examples-->
            </div>
            
        </form>
    </body>
</html>
"""
@app.route('/play', methods=['POST'])
def play_web():
    play(0.5)
    return "Function play() has been executed."

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
        return -1
    start_time = time()
    while time() - start_time < t:
        if button2.is_pressed:
            print("P2 HIT")
            return (time() - start_time)/(2*t)
    return -1


def play_round_p2(t):
    round = blink_sequence_reversed(t)
    if round == 1:
        print("P1 Hit too soon")
        return -1
    start_time = time()
    while time() - start_time < t:
        if button1.is_pressed:
            print("P1 HIT")
            return (time() - start_time)/(2*t)
    return -1

def loose_p1():
    for i in range(5):
        green_led1.on()
        sleep(0.3)
        green_led1.off()
        sleep(0.3)

def loose_p2():
    for i in range(5):
        green_led2.on()
        sleep(0.3)
        green_led2.off()
        sleep(0.3)


def play(speed):
    blink_3_times()
    result = 0.5
    while True:
        result = play_round_p1((0.5+result)/speed)
        green_led2.off()
        if result == -1:
            print("P1 WINS")
            loose_p2()
            break
        else:
            result = play_round_p2((0.5+result)/speed)
            green_led1.off()
            if result == -1:
                print("P2 WINS")
                loose_p1()
                break
        speed *= 1.1


app.run(host='0.0.0.0', port=8000, debug=True)
