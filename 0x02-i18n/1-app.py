#!/usr/bin/env python3
"""
    Instatiate Babel object
    store in a module len variable named babel
    in order to configure available languages in our app
    you will create a config clas that has a LANGUAGES class
    attribute equal to ['en', 'fr']
    use config to set Babel's default locale to 'en'
    and timezone to 'UTC'
    use that class as config for Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
        Config class for Babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """
        Return index.html
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
