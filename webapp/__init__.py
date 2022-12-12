"""
/irahorecka/__init__.py
~~~~~~~~~~~~~~~~~~~~~~~

Concerns all things webapp.
"""

from flask import Flask

from webapp.config import Config

application = Flask(__name__)


def create_app(config_class=Config):
    """Creates Flask application instance."""
    application.config.from_object(config_class)

    from webapp.main.routes import main

    # from webapp.housing.routes import housing
    # from webapp.errors.handlers import errors

    application.register_blueprint(main)
    # application.register_blueprint(housing)
    # application.register_blueprint(errors)

    return application
