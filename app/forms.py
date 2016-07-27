"""Module which describes the form fields in the bushing app."""

from flask_wtf import Form, RecaptchaField
from wtforms import StringField, TextAreaField, validators, SubmitField, \
    PasswordField
# from wtforms.validators import DataRequired


class ContactForm(Form):
    """Main contact form for OFSS."""

    name = StringField("Name", [validators.Required(
        "Please enter your name.")])
    email = StringField("Email", [validators.Required(
        "Please enter your email address."), validators.Email(
        "Please enter your email address.")])
    message = TextAreaField("Message", [validators.Required(
        "Please enter a message.")])
    recaptcha = RecaptchaField()
    submit = SubmitField("Send")


class LoginForm(Form):
    """Login form."""

    username = StringField("Username", [validators.Required(
        "Please enter your username.")])
    password = PasswordField("Password", [validators.Required(
        "Please enter your password.")])
    submit = SubmitField("Login")
# end
