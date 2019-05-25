from djongo import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin   
from datetime import datetime

class Subject(models.Model):
    dp_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    subjects = models.ListField(models.CharField(max_length=100))
    meta  = {'collection' : 'Subject'}

class Department(models.Model):
    dp_name = models.CharField(max_length=100)
    dp_abb = models.CharField(max_length=100)
    sb_name = models.ListField(models.CharField(max_length=100))
    meta  = {'collection' : 'Department'}

class Article(models.Model):
    qid = models.IntegerField()
    content = models.CharField(max_length=100)
    dp_abb = models.CharField(max_length=100)
    sb_index = models.IntegerField()
    title = models.CharField(max_length=100)
    tag_name = models.ListField(models.CharField(max_length=100))
    tag_count = models.ListField(models.IntegerField())
    post_date = models.DateTimeField()
    revise_date = models.DateField()
    good_count = models.IntegerField()
    bad_count = models.IntegerField()
    author = models.CharField(max_length=100)
    meta  = {'collection' : 'Article'}

class Comment(models.Model):
    qid = models.IntegerField()
    content = models.CharField(max_length=100)
    article_id = models.IntegerField()
    post_date = models.DateField()
    revise_date = models.DateField()
    good_count = models.IntegerField()
    bad_count = models.IntegerField()
    author = models.CharField(max_length=100)
    child_comment_id = models.IntegerField()
    parent_comment_id = models.IntegerField()
    meta  = {'collection' : 'Comment'}