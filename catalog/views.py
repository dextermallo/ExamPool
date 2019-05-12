from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
#from django.contrib.auth.models import User
from django.template import loader, Context, RequestContext
import sys
from .forms import *
from .models import *
from django.db.models import Max
from django.contrib.auth import get_user_model
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
            #user = User.create_superuser(User, username='aaa', email='ok@g.com', password='aaa')
            user = User.create_user(username = username, password = password, email = 'test@mail.com', icon = "", voting = 0, favorite = "", contribution= "")
            user.save()
            #return render(request, '/accounts/login/', locals())
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
    try:
        result = User.objects.get(username = username) 
        print(result.date_joined, file=sys.stderr)
        ret = {
            'username': result.username,
            'email': result.email,
            'password': result.password,
            'icon': result.icon,
            'voting': result.voting,
            'favorite': result.favorite,
            'contribution': result.contribution,
            'registerDate': result.date_joined
        
        }
        
    except:
        result = False
    return render(request, 'accounts/info.html', ret)

def addToDept():
    dept = Department(dp_name = '資工', sb_name = ['MV','TEST'], dp_abb = 'CS')

def allDepartment(request):
    load_department = Department.objects.all()
    context = {
        'Department' : load_department
    }
    return render(request, 'dplist.html', context)

def allSubject(request, dpName):
    load_department = Department.objects.get(dp_abb = dpName)
    print(dpName)
    print(load_department.sb_name[0])
    context = {
        'Department' : load_department
    }
    return render(request, 'sblist.html', context)

def board(request, dpName, sbIndex):
    print(dpName)
    load_article = Article.objects.filter(dp_abb = dpName).filter(sb_index = sbIndex)
    context = {
        'Article' : load_article
    }
    return render(request, 'board.html', context)

def article(request, dpName, sbIndex, articleId):
    print(dpName)
    load_article = Article.objects.filter(dp_abb = dpName).filter(sb_index = sbIndex).get(qid = articleId)
    print(load_article.content)
    laod_comment = Comment.objects.filter(article_id = articleId)
    context = {
        'Article' : load_article,
        'Comment' : laod_comment
    }
    return render(request, 'article.html', context)

def postArticle(request, dpName, sbIndex):
    if request.method == 'POST':
        form = articleForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.qid = Article.objects.order_by('-qid')[0].qid + 1
            form.dp_abb = dpName
            form.sb_index = sbIndex
            form.save()
            return HttpResponseRedirect('/department')
        else:
            form = articleForm()
            return render(request, 'post.html', locals())
    else:
        form = articleForm()
    form = articleForm()
    print(form)
    context = {
        'dp_abb' : dpName,
        'sb_index' : sbIndex,
        'form' : form
    }
    return render(request, 'post.html', context)