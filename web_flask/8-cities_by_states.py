#!/usr/bin/python3

from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Handles the get request for /cities_by_states.

    Returns:
        str: Return from the render_template method.
    """
    return render_template(
        "8-cities_by_states.html",
        states=storage.all(State).values()
    )


def close_session(res):
    """Close the current db session.

    Args:
        res (obj): Response object.
    """
    storage.close()


app.teardown_appcontext(close_session)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)