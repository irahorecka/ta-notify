"""
/webapp/config.py
~~~~~~~~~~~~~~~~~~~~~

Module to store Flask configurations for production.
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Flask app configuration class."""

    FLASK_APP = "development"
    # FLASK_APP = "production"
    # SERVER_NAME = "irahorecka.com"
    # SECRET_KEY = os.environ["SECRET_KEY"]
    # SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
