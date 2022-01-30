#!/usr/bin/python3
""" Flask route model """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """ / route  """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index():
    """ /hbnb route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """ /c route """
    return 'C {:s}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text):
    """ /c route """
    return 'Python {:s}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
