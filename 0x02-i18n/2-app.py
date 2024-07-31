#!/usr/bin/env python3
"""
    create a get_locale func with babel.localeseletor
    use request.accept_languages to
    determine the best match with our supported languages
"""
from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
        config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
        get locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world():
    """
        hello world
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
