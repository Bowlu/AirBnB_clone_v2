#!/usr/bin/python3
"""Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displaying Hello HBNB!"""

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displaying HBNB!"""

    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """Displays text"""

    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/<text>', strict_slashes=False)
def python(text = "is cool"):
    """Display Python with 'is cool' as default"""

    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)