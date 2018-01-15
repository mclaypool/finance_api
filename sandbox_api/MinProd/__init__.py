from flask import Flask
from flask_oauthlib.provider import OAuth2Provider


# add sslify
app = Flask(__name__)
app.config.from_object('config')

from .server import routes
