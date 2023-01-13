#!/usr/bin/python3

""" Starting a Flask web application that
listens on 0.0.0.0 port 5000"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


"""another route added"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    text = text.replace("_", " ")
    return f "C {text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=5000) 