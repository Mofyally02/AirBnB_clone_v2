#!/usr/bin/python3
"""
Starts a Flask web application listening on 0.0.0.0 port 5000.
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Handles get request for /.

    Returns:
        string: String to be rendered.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Handles get request for /hbnb

    Returns:
        string: String ti be rendered.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Handles the get request for /c/<text>

    Args:
        text (string): C description.

    Returns:
        string: String ti be rendered.
    """
    text = text.replace("_", " ")
    return "C {}".format(escape(text))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is_cool"):
    """Handles the get request for /python/<text>.
    text is optional in the URL.

    Args:
        text (string): Python description.

    Returns:
        string: String ti be rendered.
    """
    text = text.replace("_", " ")
    return "Python {}".format(escape(text))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Handles the get request for /number/<n>.
    n must be an integer.

    Args:
        n (int): An integer.

    Returns:
        string: String ti be rendered.
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
