from djongo import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin   
from datetime import datetime

class User(AbstractUser):
    # abstract
    # username, password, email.

    icon = models.CharField(max_length=100)
    voting = models.IntegerField()
    favorite = models.CharField(max_length=500)
    contribution = models.CharField(max_length=100)
    registerDate = models.DateTimeField()
    
    class Meta(AbstractUser.Meta):
        pass
    
    def create_user(username, email, password, icon, voting, favorite, contribution):
        if not password:
            raise ValueError('missing password')
        cur_time = datetime.now()
        user = User(username = username, email = email, icon = icon, voting = voting, favorite = favorite, contribution = contribution, registerDate = cur_time)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password, "icon", 0, "", "")
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user
        
class Block(models.Model):
    Department = models.CharField(max_length=100)
    Subject = models.ListField(models.CharField(max_length=100))
    Src = models.CharField(max_length=100)
    meta = {'collection': 'Block'}

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
    author = models.IntegerField()
    meta  = {'collection' : 'Article'}

class Comment(models.Model):
    qid = models.IntegerField()
    content = models.CharField(max_length=100)
    article_id = models.IntegerField()
    post_date = models.DateField()
    revise_date = models.DateField()
    good_count = models.IntegerField()
    bad_count = models.IntegerField()
    author = models.IntegerField()
    child_comment_id = models.IntegerField()
    parent_comment_id = models.IntegerField()
    meta  = {'collection' : 'Comment'}