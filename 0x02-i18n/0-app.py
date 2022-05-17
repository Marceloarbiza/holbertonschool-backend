#!/usr/bin/python3
""" Flask Babel i18n """

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ Index route """
    hello = 'Hello World'
    return render_template('0-index.html', hello=hello)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
