import os
import RPi.GPIO as GPIO
import lcddriver

from flask import render_template, make_response, abort, json, send_from_directory, request
from w1thermsensor import W1ThermSensor
from raspi_angular_flask.core import api_manager
from raspi_angular_flask.models import *
from raspi_angular_flask import models

for model_name in app.config['API_MODELS']:
    model_class = app.config['API_MODELS'][model_name]
    api_manager.create_api(model_class, methods=['GET', 'POST'])

session = api_manager.session
sensor = W1ThermSensor()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

# routing for basic pages (pass routing onto the Angular app)
@app.route('/')
@app.route('/func')
@app.route('/blog')
def basic_pages(**kwargs):
    return make_response(open('raspi_angular_flask/templates/index.html').read())

@app.route('/ledon')
def ledon(**kwargs):
     print "LED on"
     GPIO.output(17, GPIO.HIGH)
     return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/ledoff')
def ledoff(**kwargs):
     print "LED off"
     GPIO.output(17, GPIO.LOW)
     return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/relayon')
def relayon(**kwargs):
    print "relay on"
    GPIO.output(18, GPIO.LOW)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/relayoff')
def relayoff(**kwargs):
    print "relay off"
    GPIO.output(18, GPIO.HIGH)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/consolego')
def consolego(**kwargs):
    print "Console app launched"
    data = os.popen('date').read()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/gettemp')
def gettemp(**kwargs):
    print "Thermometer DS18B20 test launched"
    data = sensor.get_temperature()
    db.session.add(models.Events(device='Thermometer', data=data))
    db.session.commit()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/sendmsg', methods=['POST'])
def sendmsg(**kwargs):
    print "LCD text message output"
    if not request.json:
        abort(400)
    print request.json
    print request.json.keys()

    data = ""
    for key in request.json:
        data+=request.json[key] + " : "

    db.session.add(models.Events(device='LCD', data=data))
    db.session.commit()

    lcd = lcddriver.lcd()
    lcd.lcd_clear()
    lcd.lcd_display_string( request.json['lcd1'], 1)
    lcd.lcd_display_string( request.json['lcd2'], 2)
    lcd.lcd_display_string( request.json['lcd3'], 3)
    lcd.lcd_display_string( request.json['lcd4'], 4)

    return json.dumps(request.json)

crud_url_models = app.config['CRUD_URL_MODELS']

@app.route('/getevents')
def getevents(**kwargs):
    events = Events.query.all()
    data = []
    for event in events:
        print "----------------------------------------------------"
        print event.id
        print event.device
        print event.data
        print event.event_date

        record = {
            'id': event.id,
            'device': event.device,
            'data': event.data,
            'event_date': event.event_date}
        data.append(record)

    print "----------------------------------------------------"

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
