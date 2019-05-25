from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.template import loader, Context, RequestContext
import sys
from .forms import *
from .models import *
from users.models import *
from django.db.models import Max
from django.contrib.auth import get_user_model
from collections import Counter

def index(request):
    return render(request, 'index.html',locals())

def login(request):
    
    if request.user.is_authenticated: 
        return HttpResponseRedirect('/index/')
    
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = User.authenticate(username=username, password=password)
        print(user.username, file=sys.stderr)
        print(user.password, file=sys.stderr)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/index/')
        else: # TODO: Add account verify.
            return render(request, 'accounts/login.html') 
    else: # via GET method to return page.
        return render(request, 'accounts/login.html') 

def register(request):
    if request.user.is_authenticated: 
        return HttpResponseRedirect('/index/')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        password = request.POST.get('password', '')
        
        user = User.create_user(username = username, email = email, password = password, first_name = first_name, last_name = last_name)

        #return render(request, '/accounts/login/', locals())
        ret = {
            'username': email,
            'password': password
        }
        return HttpResponseRedirect('/accounts/login/')
    else:
        return render(request, 'accounts/login.html', ret)
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def user_profile(request, username):
    try:
        result = User.objects.get(username = username) 
        articles = Article.objects.all().filter(author = username)
        print(articles, file=sys.stderr)
        reply_count = {}
        for article in articles:
            comments = Comment.objects.all().filter(article_id = article.qid)         
            reply_count[article.qid] = len(Counter(comments)) if comments is not None else 0
        
        ret = {
            'username': result.username,
            'email': result.email,            
            'first_name': result.first_name,
            'last_name': result.last_name,            
            'contribution': articles,
            'reply': reply_count,
        }    
    except:
        result = False
        ret = {
            'result': False
        }
    return render(request, 'accounts/info.html', ret)

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
        'Comment' : laod_comment,
        'tag_name': [],
        'tag_count': []
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
            form.tag_name = []
            form.tag_count = []
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

