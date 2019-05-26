from djongo import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin   
from datetime import datetime
from django.contrib.auth import get_user_model
import sys

class User(AbstractUser):
     
    username = models.CharField(max_length=30, blank=False, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)

    class Meta(AbstractUser.Meta):
        pass
    
    def _create_user(username, email, password, first_name, last_name, is_staff, is_superuser):
        if not password:
            raise ValueError('missing password')
        user = User(username=username, email=email, password=password,
                    first_name=first_name, last_name=last_name)
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.is_active = True
        user.save()
        return user

    def authenticate(username, password):
        try:
            user = User.objects.get(username=username)
        except:
            return None
        if user.check_password(password):
            return user
        return None

    def create_user(username, email, password, first_name, last_name):
        user = User._create_user(username, email, password, first_name, last_name, False, False)
        return user

    def create_superuser(username, email, password, first_name, last_name):
        user = User._create_user(username, email, password, first_name, last_name, True, True)
        return user

    def check_password(self, password):
        return self.password == password

    def set_password(self, raw_password):
        return super().set_password(raw_password)

    def update_profile(username, email, first_name, last_name, password):
        User.objects.filter(username=username).update(email=email,first_name=first_name,last_name=last_name,password=password)
        

class Icon(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    icon = models.ImageField(upload_to='media/user_icon/', max_length=None) 

    def create_icon(user, icon):
        icon = Icon(user, icon)
        icon.save()
    
    def update_icon(user, icon):
        Icon.obejcts.filter(pk=user).update(icon=icon)

class Contribution(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    contribution = models.ListField(models.CharField(max_length=2000))
    
    def register_user(user):
        contribution = Contribution(user, [])
        contribution.save()

class Favorite(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    favorite = models.ListField(models.CharField(max_length=2000))
    def register_user(user):
        favorite = Favorite(user, [])
        favorite.save()

class Voting(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )   
    voting = models.IntegerField() 

    def register_user(user):
        voting = Voting(user, 0)
        voting.save()

