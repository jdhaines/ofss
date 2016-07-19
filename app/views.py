"""Views module for the flask app."""

# import csv

# from io import StringIO

from app import app  # , db, models
from flask import render_template, redirect  # request Markup abort make_response
from .forms import ContactForm  # BushingInfo, BushingSN, SingleExtract


@app.route("/")
@app.route("/index", methods=['GET'])
def index():
    """Display the home (index) page."""
    return render_template("index.html",
                           title="Ohio Family Survival Store",)


@app.route("/about", methods=['GET'])
def about():
    """Display the about page."""
    return render_template("about.html",
                           title="About - Ohio Family Survival Store",)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    """Display the contact page."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect('/sucess')
    return render_template("contact.html",
                           title="Contact - Ohio Family Survival Store",
                           form=form)

    # # user is sending data to the page
    # if request.method == 'POST':

    #     # form input isn't correct
    #     if form.validate() is False:

    #         # re-show the contact page
    #         return render_template("contact.html",
    #                        title="Contact - Ohio Family Survival Store",
    #                        form=form)
    #     # form input is correct, do the database thing
    #     else:
    #         return render_template("success.html",
    #                         title="Sucess - Ohio Family Survival Store")

    # # We're simply displaying the page, not getting user input
    # elif request.method == 'GET':
    #     return render_template("contact.html",
    #                        title="Contact - Ohio Family Survival Store",
    #                        form=form)

# end
