from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import loader, Context, RequestContext
import sys
from .forms import *
def index(request):
    return render(request, 'index.html',locals())

def login(request):
    
    if request.user.is_authenticated: 
        return HttpResponseRedirect('/index/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render(request, 'accounts/login.html') 

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username = username, password = password)
            user.save()
            return HttpResponseRedirect('/accounts/login/')
        else:
            form = registerForm()
            return render(request, 'accounts/register.html', locals())    
    else:
        form = registerForm()
        return render(request, 'accounts/register.html', locals())
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def userInfo(request, username):
    print(request.user.username, file=sys.stderr)
    try:
        result = User.objects.get(username = username)    
    except:
        result = False
    return render(request, 'accounts/info.html', locals())