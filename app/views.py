"""Views module for the flask app."""

from app import app


@app.route('/')
@app.route('/index')
def index():
    """Display the home (index) page."""
    return "Hello, World!"
