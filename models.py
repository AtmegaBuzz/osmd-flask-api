from flask_sqlalchemy import SQLAlchemy
import enum
from passlib.apps import custom_app_context as pwd_context
from uuid import uuid4
from sqlalchemy.dialects.mysql import TIME,DATE

db = SQLAlchemy()

class UserTypeChoices(enum.Enum):
    driver = 'driver'
    rider = 'rider'

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    user_type = db.Column(
        db.Enum(UserTypeChoices), 
        default=UserTypeChoices.rider,
        nullable=False
    )
    api_token = db.Column(db.String(1000))

    bookings = db.relationship('Booking',backref='user')


    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_token(self):
        self.api_token = str(uuid4())

    def verify_token(self, api_token):
        pwd_context.verify(api_token, self.api_token)



# Create your models here.
class CabGroup(db.Model):
    __tablename__ = "cab_group"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    bookings = db.relationship('Booking',backref='cab_group')
    

# root destination of the organization offering the services
class Source(db.Model):
    __tablename__ = "source"
    
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(1000),nullable=False)


class Booking(db.Model):
    
    __tablename__ = "booking"

    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(1000),nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('cab_group.id'))
    
    status = db.Column(db.Integer)
    time = db.Column(TIME(),nullable=False)
    date = db.Column(DATE(),nullable=False) 

    cost = db.Column(db.Integer)
    distance = db.Column(db.Integer)
    