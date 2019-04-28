from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import loader, Context, RequestContext

from catalog.models import Departments, Articles

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


# path('departments/', views.allDepartment),
# path('departments/<str:dpname>/', views.allSubject),
# path('departments/<str:dpname>/subjects/<str:sbname>', views.board)

def allDepartment(request):
    load_departments = Departments.objects
    context = {
        'Departments' : load_departments
    }
    return render(request, 'dplist.html', context)

def allSubject(request, dpname):
    load_department = Departments.objects.get(short_name = dpname)
    print(dpname)
    print(load_department.subjects[0])
    context = {
        'Department' : load_department
    }
    return render(request, 'sblist.html', context)

def board(request, dpname, sbindex):
    print(dpname)
    load_article = Articles.objects.filter(dp_short_name = dpname).filter(sb_index = sbindex)
    print(load_article[0].content)
    context = {
        'Articles' : load_article
    }
    return render(request, 'board.html', context)