from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from my_app.auth.authentication import *
"""
    Commented out statements are for database configuration
    this now happens in models.py I know it is better
    to do it here but could not get it to work.
"""

app = Flask(__name__)
app.config['SECRET_KEY'] = "super_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///item_catalog.db"
app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': '326861684438397',
        'secret': '086e6980ab1a1705d46a3b8eccedd767'
    },
    'twitter': {
        'id': 'RSY25MYFWqQlbomtNmxxy71a9',
        'secret': '1bhcL4TzsTPOOugaR411EU7frE2SGrzep5WyTfoWXHdyYLrGi3'
    },
    'google':{
        'id': '78419860005-fjssrgcr626qpmk4feic9snbss1og6np.apps.googleusercontent.com',
        'secret': 'vXmoJiVcB3mJ7mrMCH23leT-'
    }
}

import my_app.catalog.views
# from my_app.catalog.views import catalog
# from my_app.catalog.views import api
# app.register_blueprint(catalog)
# app.register_blueprint(api)
