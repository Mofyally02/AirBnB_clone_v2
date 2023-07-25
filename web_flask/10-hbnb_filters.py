#!/usr/bin/python3
"""
Starts a Flask web application listening on 0.0.0.0 port 5000.
"""

from flask import Flask, render_template

from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Handles the get request for /hbnb_filters

    Returns:
        str: Return from the render_template function.
    """
    return render_template(
        "10-hbnb_filters.html",
        states=storage.all(State).values(),
        amenities=storage.all(Amenity).values(),
    )


@app.teardown_appcontext
def close_session(exception):
    """Close the current db session after a request.

    Args:
        exception (Exception): Exception object.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
