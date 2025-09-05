from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='user')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    sku = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer, default=0, nullable=False)
    min_quantity = db.Column(db.Integer, default=0, nullable=False)
    price = db.Column(db.Float, default=0.0, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Movement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    type = db.Column(db.String(3), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    note = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    product = db.relationship('Product', backref=db.backref('movements', lazy=True))
    user = db.relationship('User', backref=db.backref('movements', lazy=True))
