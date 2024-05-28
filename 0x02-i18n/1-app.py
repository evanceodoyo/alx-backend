#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.url_map.strict_slashes = False


class Config:
    """
    Class that lists available languages.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    Index page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
