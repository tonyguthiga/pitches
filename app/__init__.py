from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__)

# Setting up configurartion
app.config.from_object(DevConfig)


# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views