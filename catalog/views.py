from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User

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
        user = User.objects.create_user(username=request.POST.get('username', None), password=request.POST.get('password', None))
        user.save()
        return HttpResponseRedirect('/accounts/login/')
    else:
        return render(request, 'accounts/register.html',locals())
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')