"""Module which describes the form fields in the bushing app."""

from flask_wtf import Form, RecaptchaField
from wtforms import StringField  # , StringField, SelectField, TextAreaField
from wtforms import validators, SubmitField  # ValidationError,
# from wtforms.validators import DataRequired


class ContactForm(Form):
    """Main contact form for OFSS."""

    name = StringField("Name", [validators.Required(
        "Please enter your name.")])
    email = StringField("Email", [validators.Required(
        "Please enter your email address."), validators.Email(
        "Please enter your email address.")])
    recaptcha = RecaptchaField()
    submit = SubmitField("Send")

# end
