#!/usr/bin/python3
""" Flask Babel i18n """

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Returns current locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Index route """
    return render_template('1-index.html')


class Config:
    """ Config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
