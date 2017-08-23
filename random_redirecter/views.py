import random

from flask import Flask, redirect

app = Flask(__name__)

REDIRECT_URLS = [
    'https://www.loop11.com/usertest/39581/',
    'https://www.loop11.com/usertest/39582/',
    'https://www.loop11.com/usertest/39583/',
    'https://www.loop11.com/usertest/39584/',
    'https://www.loop11.com/usertest/39585/',
]


@app.route("/")
def redirection_view():
    return redirect(random.choice(REDIRECT_URLS))
