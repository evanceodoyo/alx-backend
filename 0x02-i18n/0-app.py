#!usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template
from flask.wrappers import Response


app = Flask(__name__)


@app.route('/')
def index() -> Response:
    """
    Index page
    """
    return render_template('0-index.html')
