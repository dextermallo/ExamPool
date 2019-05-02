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

class Subject(Document):
    dp_name = StringField()
    short_name = StringField()
    subjects = ListField(StringField())
    meta  = {'collection' : 'Subject'}

class Department(Document):
    dp_name = StringField()
    dp_abb = StringField()
    sb_name = ListField(StringField())
    meta  = {'collection' : 'Department'}

class Article(Document):
    qid = IntField()
    content = StringField()
    dp_abb = StringField()
    sb_index = IntField()
    title = StringField()
    tag_name = ListField(StringField())
    tag_count = ListField(IntField())
    post_date = DateTimeField()
    revise_date = DateField()
    good_count = IntField()
    bad_count = IntField()
    author = IntField()
    meta  = {'collection' : 'Article'}

class Comment(Document):
    qid = IntField()
    content = StringField()
    article_id = IntField()
    post_date = DateField()
    revise_date = DateField()
    good_count = IntField()
    bad_count = IntField()
    author = IntField()
    child_comment_id = IntField()
    parent_comment_id = IntField()
    meta  = {'collection' : 'Comment'}