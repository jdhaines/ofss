"""Views module for the flask app."""

# import csv

# from io import StringIO

from app import app, blogging_engine, login_manager  # db, models,
from flask import render_template, redirect
from .forms import ContactForm, LoginForm
from flask_login import UserMixin, login_user, logout_user


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


@app.route("/success", methods=['GET'])
def success():
    """Display the about page."""
    return render_template("success.html",
                           title="Success - Ohio Family Survival Store",)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    """Display the contact page."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect("/success")
    return render_template("contact.html",
                           title="Contact - Ohio Family Survival Store",
                           form=form)


@app.route("/login", methods =["GET", "POST"])
def login():
    """Login Page."""
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # next_is_valid should check if the user has valid
        # permission to access the `next` url
        if not next_is_valid(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)


@app.route("/logout")
def logout():
    """Logout Page."""
    logout_user()
    return redirect("/")


# Classes
class User(UserMixin):
    """Docstring."""

    def __init__(self, user_id):
        """Docstring."""
        self.id = user_id

    def get_name(self):
        """Docstring."""
        return "Mary"  # typically the user's name


# Functions
@login_manager.user_loader
@blogging_engine.user_loader
def load_user(user_id):
    """Docstring."""
    return User(user_id)
