from app import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class User(db.Model):
    Id = db.Column(db.Integer, primary_key=True, unique=True)
    firstname = db.Column(db.String(25))
    lastname = db.Column(db.String(25))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(10))
    school = db.Column(db.String(50))
    password = db.Column(db.String(80))

    def __init__(self, firstname, lastname, age, grade, school, password):
        #self.Id = Id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.grade = grade
        self.school = school
        self.password = password
    def __repr__(self):
        return '<User %r>' % self.Id
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.Id)