#!/usr/bin/python3
'''A simple web application using Flask'''
from flask import Flask


app = Flask(__name__)
'''The Flask application instance'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''Home page'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
