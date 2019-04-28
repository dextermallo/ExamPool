from django.db import models
from mongoengine import *

connect('CRUD', host = '127.0.0.1', port = 27017)

class user(Document):
    idNumber = StringField()
    name = StringField()
    age = StringField()
    mailbox = StringField()
    power = StringField()
    password = StringField()

    meta = {'collection': 'user'}

class Block(Document):
    Department = StringField()
    Subject = ListField(StringField())
    Src = StringField()
    meta = {'collection': 'Block'}

class Article(Document):
    QID = IntField()
    Comment = StringField()
    meta  = {'collection' : 'Article'}