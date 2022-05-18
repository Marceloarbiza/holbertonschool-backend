#!/usr/bin/python3
""" Flask Babel i18n """

from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    """ Index route locale """
    return render_template('5-index.html')


class Config:
    """ Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Returns current locale """
    locale = request.args.get('locale', None)
    if locale and locale in app.config['LANGUAGES']:
        return locale
    locale = request.headers.get('locale', None)
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ Get user by id """
    args = request.args
    if 'login_as' in args:
        id = int(args['login_as'])
        if id in users:
            return users[id]
    return None


@app.before_request
def before_request():
    """ flask.g.user is the current user """
    g.user = get_user()


if __name__ == '__main__':
    app.run(debug=True)
