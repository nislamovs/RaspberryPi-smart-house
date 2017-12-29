import os
import json
from flask import Flask, request, Response
from flask import render_template, send_from_directory, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('raspi_angular_flask.settings')

app.url_map.strict_slashes = False

import raspi_angular_flask.core
import raspi_angular_flask.models
import raspi_angular_flask.controllers






