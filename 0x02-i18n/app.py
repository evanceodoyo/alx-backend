#!/usr/bin/env python3
"""
Flask app
"""
import pytz
from flask import Flask, g, render_template, request
from flask_babel import Babel, format_datetime
from typing import Union, Dict

app = Flask(__name__)
app.url_map.strict_slashes = False
users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }


class Config:
    """
    Class that lists available languages.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match with supported languages.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Get the appropriate time zone.
    """
    timezone = request.args.get('timezone')
    if not timezone and g.user:
        timezone = g.user.get("timezone")
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user() -> Union[Dict, None]:
    """
    Gets user by mocking a database user table.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))

    return None


@app.before_request
def before_request() -> None:
    """
    Find user (if any) and set it as global on flask.g.user
    """
    g.user = get_user()
    g.current_time = format_datetime()


@app.route('/')
def index() -> str:
    """
    Index page
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
