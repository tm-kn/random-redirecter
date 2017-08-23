import random

from flask import Flask, redirect

app = Flask(__name__)

REDIRECT_URLS = [
    'https://www.loop11.com/usertest/39566/',
    'https://www.loop11.com/usertest/39564/',
    'https://www.loop11.com/usertest/39563/',
    'https://www.loop11.com/usertest/39559/',
    'https://www.loop11.com/usertest/39500/',
]


@app.route("/")
def redirection_view():
    return redirect(random.choice(REDIRECT_URLS))
