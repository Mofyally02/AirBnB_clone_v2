#!/usr/bin/python3

from flask import Flask, render_template

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb_filters():
    """
    Handles the get request for /hbnb.

    Returns:
        str: Return from the render_template function.
    """
    return render_template(
        "100-hbnb.html",
        states=storage.all(State).values(),
        amenities=storage.all(Amenity).values(),
        places=storage.all(Place).values(),
    )


def close_session(res):
    """Close the current db session.

    Args:
        res (obj): Response object.
    """
    storage.close()


app.teardown_appcontext(close_session)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)