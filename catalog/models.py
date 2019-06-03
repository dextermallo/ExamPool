from djongo import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin   
from datetime import datetime

class Department(models.Model):
    dp_name = models.CharField(max_length=100)
    dp_abb = models.CharField(max_length=100)
    sb_name = models.ListField(models.CharField(max_length=100))
    meta  = {'collection' : 'Department'}

class Article(models.Model):
    content = models.CharField(max_length=100000)
    dp_abb = models.CharField(max_length=100)
    sb_index = models.IntegerField()
    title = models.CharField(max_length=100)
    tag_name = models.ListField(models.CharField(max_length=100))
    tag_count = models.ListField(models.IntegerField())
    post_date = models.DateField()
    revise_date = models.DateField()
    good_list = models.ListField(models.CharField(max_length=100))
    bad_list = models.ListField(models.CharField(max_length=100))
    author = models.CharField(max_length=100)
    top = models.BooleanField(default=False)
    exist = models.BooleanField(default=True)
    meta  = {'collection' : 'Article'}

class Comment(models.Model):
    article_id = models.IntegerField()
    child_comment_id = models.ListField(models.IntegerField(), default=[])
    good_list = models.ListField(models.CharField(max_length=100), default=[])
    bad_list = models.ListField(models.CharField(max_length=100), default=[])
    content = models.CharField(max_length=100000)
    post_date = models.DateField()
    revise_date = models.DateField()
    author = models.CharField(max_length=100)
    parent_comment_id = models.IntegerField()
    exist = models.BooleanField(default=True)
    meta  = {'collection' : 'Comment'}