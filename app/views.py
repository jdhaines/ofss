"""Views module for the flask app."""

# import csv

# from io import StringIO

from app import app, blogging_engine, login_manager  # db, models,
from flask import render_template, redirect, request, flash, url_for
from .forms import ContactForm, LoginForm
from flask_login import UserMixin, login_user, logout_user, login_required
from flask_login import confirm_login


# Classes
class User(UserMixin):
    """Docstring."""

    def __init__(self, id, name, active=True):
        """Docstring."""
        self.id = id
        self.name = name
        self.active = active

    def is_active(self):
        """Docstring."""
        return self.active

    def get_name(self):
        """Docstring."""
        return self.name  # typically the user's name

# User Values
USERS = {
    1: User(1, u"Josh"),
    2: User(2, u"Mary")
}

USER_NAMES = dict((u.name, u) for u in USERS.values())


# Functions
@login_manager.user_loader
@blogging_engine.user_loader
def load_user(user_id):
    """Docstring."""
    return USERS.get(id)


# Routes
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


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login User."""
    form = LoginForm()
    if request.method == "POST" and "username" in request.form:
        username = request.form["username"]
        if username in USER_NAMES:
            print("Valid Username")
            remember = request.form.get("remember", "no") == "yes"
            if login_user(USER_NAMES[username], remember=remember):
                flash("Logged in!")
                print("After flash Logged In!")
                return redirect(request.args.get("next") or url_for("index"))
            else:
                flash("Sorry, but you could not log in.")
        else:
            flash(u"Invalid username.")
    return render_template("login.html", form=form)


@app.route("/reauth", methods=["GET", "POST"])
@login_required
def reauth():
    """Reauthorize User."""
    if request.method == "POST":
        confirm_login()
        flash(u"Reauthenticated.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("reauth.html")


@app.route("/logout")
@login_required
def logout():
    """Logout User."""
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))

# end
