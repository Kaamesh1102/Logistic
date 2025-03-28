from .database import db
from flask_security import UserMixin,RoleMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String,unique = True,nullable = False)
    username = db.Column(db.String,unique = True,nullable = False)
    password = db.Column(db.String,nullable = False)
    fs_uniquifier = db.Column(db.String,unique = True,nullable = False)
    active = db.Column(db.Boolean,nullable = False)
    roles = db.relationship('Role',backref = 'bearer', secondary = 'user_roles')

class Role(db.Model,RoleMixin):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String,unique = True,nullable = False)
    description = db.Column(db.String)

class UserRoles(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))
