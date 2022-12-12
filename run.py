"""
/run.py
~~~~~~~
Starts a Flask web application instance.
"""

from webapp import create_app

application = create_app()

if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=True)
