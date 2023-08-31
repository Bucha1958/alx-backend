#!/usr/bin/env python3
"""
My flask app file
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """
    function that render template
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
