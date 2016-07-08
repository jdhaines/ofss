"""Views module for the flask app."""

# import csv

# from io import StringIO

from app import app  # , db, models

from flask import render_template  # Markup, abort, make_response, , request

# from .forms import BushingInfo, BushingSN, SingleExtract


@app.route("/")
@app.route("/index", methods=['GET'])
def index():
    """Display the home (index) page."""
    return render_template("index.html",
                           title="Ohio Family Survival Store",)

# end
