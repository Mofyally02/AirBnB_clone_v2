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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
