#!/usr/bin/python3
""" Flask Babel i18n """

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """ Index route """
    # return index.html in templates folder
    return render_template('0-index.html')


class Config:
    """ Config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_DOMAIN = 'messages'
    BABEL_DEFAULT_FOLDER = 'translations'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
