from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_items = db.Column(db.Integer, nullable=False)
    delivery_date = db.Column(db.Date, nullable=False)
    sender_name = db.Column(db.String(128), nullable=False)
    recipient_name = db.Column(db.String(128), nullable=False)
    recipient_address = db.Column(db.String(256), nullable=False)
    status = db.Column(db.String(20), default='Ongoing')
    logs = db.relationship('ActionLog', backref='order', lazy=True)

class ActionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action_type = db.Column(db.String(20), nullable=False)
    performed_by = db.Column(db.String(64), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=True)
