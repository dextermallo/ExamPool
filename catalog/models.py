from djongo import models

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

class Subject(Document):
    dp_name = StringField()
    short_name = StringField()
    subjects = ListField(StringField())
    meta  = {'collection' : 'Subject'}

class Departments(Document):
    dp_name = StringField()
    short_name = StringField()
    subjects = ListField(StringField())
    meta  = {'collection' : 'Departments'}

class Articles(Document):
    qid = IntField()
    content = StringField()
    dp_short_name = StringField()
    sb_index = IntField()
    title = StringField()
    meta  = {'collection' : 'Article'}