import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/dogs')
    def dogs():
        import json
from typing import List
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import requests

def get_info_api(api_url):
    names = []
    response = requests.get(api_url)
    jsonBody = json.loads(response.content)
    for group in jsonBody:
        for key in group:
            names.append(group[key]['name'])
    return url_for('dogs')

    return app