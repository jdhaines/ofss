"""Inititalize the flask app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_blogging import SQLAStorage, BloggingEngine
from flask_login import LoginManager

app = Flask(__name__, static_url_path="")
app.config.from_object('config')

# Blogging
db = SQLAlchemy(app)
storage = SQLAStorage(db=db)
db.create_all()

blogging_engine = BloggingEngine()
blogging_engine.init_app(app, storage)

# Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "reauth"

from app import views, models

# end
