"""
1) make a new Flask application
2) It will configure application for the following
        a) Path of database
        b) Whether we are tracking every change made by SQLAlchemy (performance improves if it is
        set to False)

3) Create a new db object based on SQLAlchemy

4) Use the db object as parent class to inherit and make Employee models
"""

from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dataclasses import dataclass

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "super secret key"

db=SQLAlchemy(app) #instance of flask and instance of SQLAlchemy is connected

@dataclass
class Employee(db.Model):

    #attributes for the class and mentioned their
    #expected data type
    #Python will make a constructor & repr for these attributes

    eid : int
    ename : str
    eage : int

    #serialization : converting python fields to sql fields
    eid = db.Column(db.Integer, primary_key=True)
    ename = db.Column(db.String(20), nullable=False)
    eage = db.Column(db.Integer, nullable=False)



@dataclass
class User(db.Model):
    name : str
    age : int
    email : str
    password : str

 #serialization : converting python fields to sql fields
    email = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    password=db.Column(db.String(1000), nullable=False)




with app.app_context():
    db.create_all()



"""

attributes - variables & methods

constructor
repr
hash - generate unique ID for each object
equals - How to determine equality between 2 objects of this class
call : what to do if object of this call is used like a function*
operator functions: __add__, __mul__, etc

"""