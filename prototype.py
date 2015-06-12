from backend import db
from datetime import datetime

class Device(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	posicaox = db.Column(db.Float)
	posicaoy = db.Column(db.Float)
	Measurements = db.relationship('Measurement')
	
class Measurement(db.Model):
        id_Measurement = db.Column(db.Integer, db.ForeignKey('device.id'))
        temp = db.Column(db.Float)
        lum = db.Column(db.Float)
        time = db.Column(db.DateTime, primary_key= True)
