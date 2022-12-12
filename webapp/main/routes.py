"""
/webapp/main/routes.py
~~~~~~~~~~~~~~~~~~~~~~

Flask blueprint to handle routes for webapp.
"""

from pathlib import Path

import yaml
from flask import render_template, Blueprint, Response

main = Blueprint("main", __name__)

TEMPLATES_PATH = Path(__file__).absolute().parent.parent / "templates"


@main.route("/")
def index():
    """Landing page of personal website."""
    content = {
        "title": "Home",
    }
    return render_template("main/index.html", content=content)


@main.route("/humans.txt")
def humans_txt():
    """humans.txt page of personal website."""
    with open(TEMPLATES_PATH / "humans.txt", "r") as f:
        content = f.read()
    return Response(content, content_type="text/plain")
