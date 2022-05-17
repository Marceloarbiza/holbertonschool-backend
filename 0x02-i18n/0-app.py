#!/usr/bin/python3
""" Flask Babel i18n """

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ Index route """
    # return index.html in templates folder
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
