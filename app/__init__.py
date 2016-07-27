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

from app import views, models

# end
