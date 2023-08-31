#!/usr/bin/env python3
"""
My flask app file
"""


from flask import Flask, render_template
from flask_babel import Babel
from config import Config


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def index():
    """
        function that render template
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
