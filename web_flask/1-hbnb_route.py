#!/usr/bin/python3
"""Script that runs a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Function invoked with / route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function invoked with /hbnb route"""
    return 'HBNB'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
