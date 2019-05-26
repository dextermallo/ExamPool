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

