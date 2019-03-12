from django.db import models
from mongoengine import *

connect('EduForum', host = '127.0.0.1', port = 27017)

class user(Document):
    idNumber = StringField()
    name = StringField()
    age = StringField()
    mailbox = StringField()
    power = StringField()
    password = StringField()

    meta = {'collection': 'user'}
