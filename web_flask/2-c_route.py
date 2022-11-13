#!/usr/bin/python3
"""
A python script that uses the flask web-framework
web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """
    Displays "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_is_fun(text):
    """
    Display “C ” followed by the value of the text variable
    replaces underscore _ symbols with a space
    """
    text = text.replace("_", " ")
    return (f"C {text}")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
