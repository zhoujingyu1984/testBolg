#！/usr/bin/env python
#-*- coding utf8 -*-

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
import os
from . import app
db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    role = db.Column(db.Integer,db.ForeignKey('role.id'))

    @property
    def password(self):
        raise AttributeError('PassWord is not a readable attribute')
    @password.setter
    def password(self,password):
        self.password = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer,primary_key=True)
    rolename = db.Column(db.String(20))
    ownerrights = db.Column(db.Integer)#3位，增加100，删除010，修改001
    otherrights = db.Column(db.Integer)#3位，增加100，删除010，修改001
    users = db.relationship('user',backref='role')

class context(db.Model):
    __tablename__ = 'context'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20))
    time = db.Column(db.DateTime)
    context = db.Column(db.String(140))
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    contextid = db.Column(db.Integer,db.ForeignKey('context.id'))
    reply = db.Column(db.Boolean)
    goodcount = db.Column(db.Integer)
    ext = db.Column(db.LargeBinary)


class DBmanger():
    def __init__(self,app):
        self.app = app
    def initDB(self):
        if not os.path.exists(self.app.config['DBPATH']):
            db.create_all()
            print('db create OK!')
        else:
            print('db is no need create!')
    def addUser(self,name,passWord,roleType):
        tmpUser = User(username=name,password_hash=User.password(passWord),roleType=)
        tmpUser.password = passWord;
        tmpUser.password_hash

dbManager = DBmanger()