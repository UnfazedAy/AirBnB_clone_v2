#!/usr/bin/bash
"""
A python script that uses the flask web-framework 
web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_page():
    """
    display “Hello HBNB!”
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
