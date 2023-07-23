#!/usr/bin/python3

from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Handles the get request for /states.

    Returns:
        str: Return from the render_template method.
    """
    return render_template(
        "9-states.html",
        states=storage.all(State).values()
    )


@app.route("/states/<id>", strict_slashes=False)
def states_with_id(id):
    """Handles the get request for /states/<id>.

    Returns:
        str: Return from the render_template method.
    """
    found = None

    for state in storage.all(State).values():
        if state.id == id:
            found = state

    return render_template(
        "9-states.html",
        state=found,
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