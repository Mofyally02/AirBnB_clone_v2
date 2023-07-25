#!/usr/bin/python3
"""
Starts a Flask web application listening on 0.0.0.0 port 5000.
"""

from flask import Flask, render_template, url_for

from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """Handles the get request for /states and /states/<id>.

    Args:
        id (str, optional): Id of the state to display. Defaults to None.

    Returns:
        str: Return from the render_template method.
    """

    state, states = None, None

    if id:
        state = storage.all(State).get('State.{}'.format(id), None)
    else:
        states = storage.all(State).values()

    return render_template(
        "9-states.html",
        states=states,
        state=state,
    )


@app.teardown_appcontext
def close_session(exception):
    """Close the current db at the end of a request.

    Args:
        exception (Exception): Exception object.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
