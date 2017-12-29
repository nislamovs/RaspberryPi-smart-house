from datetime import datetime

from raspi_angular_flask.core import db
from raspi_angular_flask import app


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device = db.Column(db.String(80))
    data = db.Column(db.Text)
    event_date = db.Column(db.DateTime)

    def __init__(self, device, data, event_date=None):
        self.device = device
        self.data = data
        if event_date is None:
            event_date = datetime.utcnow()
        self.event_date = event_date

    def __repr__(self):
        return '<Events %r>' % self.device

# models for which we want to create API endpoints
app.config['API_MODELS'] = {'events': Events}

# models for which we want to create CRUD-style URL endpoints,
# and pass the routing onto our AngularJS application
app.config['CRUD_URL_MODELS'] = {'events': Events}
