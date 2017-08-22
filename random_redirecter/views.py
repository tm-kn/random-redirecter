import random

from flask import Flask, redirect

app = Flask(__name__)

REDIRECT_URLS = [
    'http://dgg.gg/',
    'http://mozilla.org/',
]


@app.route("/")
def redirection_view():
    return redirect(random.choice(REDIRECT_URLS))
