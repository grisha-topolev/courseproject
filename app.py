# app.py
from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/joke')
def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "There are only 10 kinds of people in this world: those who understand binary and those who don’t.",
        "I told my computer I needed a break, and it said: 'No problem, I'll go to sleep.'"
    ]
    return random.choice(jokes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)