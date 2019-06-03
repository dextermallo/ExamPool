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

from django.utils import timezone

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
    form = voteForm()
    load_article = Article.objects.filter(dp_abb = dpName).filter(sb_index = sbIndex).get(id = articleId)
    load_comment = Comment.objects.filter(article_id = articleId)

    if not load_article.exist:
        return render(request, 'noArticle.html')

    context = {
        'User' : request.user,
        'Article' : load_article,
        'Comment' : load_comment,
        'tag_name' : [],
        'tag_count' : [],
        'article_goodbad_count' : len(load_article.good_list) - len(load_article.bad_list),
        'comment_goodbad_count' : [len(x.good_list) - len(x.bad_list) for x in load_comment],
    }

    if request.method == 'POST':
        form = favoriteForm(request.POST)
        if form.is_valid():
            #if user's action is "add to favorite"
            #print(form.cleaned_data.get("article_id"))
            user_name = request.user.username
            article_id = int(form.cleaned_data.get("article_id"))
            print("add favorite")
            context["form"] = form

            return render(request, 'article.html', context)

        form = voteForm(request.POST)
        if form.is_valid():
            #if user's action is "vote"
            user_name = request.user.username
            user_vote = form.cleaned_data.get("goodbad")
            is_vote_article = form.cleaned_data.get("is_article") == "True"
            comment_id = int(form.cleaned_data.get("comment_id"))
            voted_user = set()
            voted_user = set()
            if is_vote_article:
                voted_user = set(load_article.good_list) or set(load_article.bad_list)
            else:
                voted_user = set(load_comment.get(id=comment_id).good_list) or set(load_comment.get(id=comment_id).bad_list)

            #check if user already voted
            is_voted = user_name in voted_user
            if not is_voted:
                if is_vote_article:
                    if user_vote == "good":
                        load_article.good_list.insert(0, user_name)
                    if user_vote == "bad":
                        load_article.bad_list.insert(0, user_name)
                    load_article.save()
                else:
                    load_comment_el = load_comment.get(id=comment_id)
                    if user_vote == "good":
                        load_comment_el.good_list.insert(0, user_name)
                    if user_vote == "bad":
                        load_comment_el.bad_list.insert(0, user_name)
                    load_comment_el.save()
            print(user_name)
            print(comment_id)
            print(user_vote)
            load_comment = Comment.objects.filter(article_id = articleId)
            context["form"] = form
            context["article_goodbad_count"] = len(load_article.good_list) - len(load_article.bad_list)
            context["comment_goodbad_count"] = [len(x.good_list) - len(x.bad_list) for x in load_comment]
            context["is_voted"] = is_voted

            return render(request, 'article.html', context)
            
    form = voteForm()
    return render(request, 'article.html', context)

def postArticle(request, dpName, sbIndex):
    if request.method == 'POST' and request.user.is_authenticated:
        form = articleForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            try:
                form.id = Article.objects.order_by('-id')[0].id + 1
            except IndexError:
                form.id = 0
            print(form.id)
            form.dp_abb = dpName
            form.sb_index = sbIndex
            form.tag_name = []
            form.tag_count = []
            form.post_date = timezone.now()
            form.revise_date = timezone.now()
            form.good_list = []
            form.bad_list = []
            form.author = request.user.username
            form.save()
            return HttpResponseRedirect('/department/' + dpName + '/' + sbIndex)
        else:
            form = articleForm()
            return render(request, 'post.html', locals())
    else:
        form = articleForm()
    form = articleForm()
    #print(form)
    context = {
        'dp_abb' : dpName,
        'sb_index' : sbIndex,
        'form' : form
    }
    return render(request, 'post.html', context)

def reviseArticle(request, dpName, sbIndex, articleId):
    article = Article.objects.get(id=articleId)
    if request.method == 'POST':
        form = articleForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.id = articleId
            form.dp_abb = dpName
            form.sb_index = sbIndex
            form.tag_name = article.tag_name
            form.tag_count = article.tag_count
            form.post_date = article.post_date
            form.revise_date = timezone.now()
            form.good_list = article.good_list
            form.bad_list = article.bad_list
            form.author = request.user.username
            form.save()
            return HttpResponseRedirect('/department/' + dpName + '/' + sbIndex)
        else:
            form = articleForm()
            return render(request, 'post.html', locals())
    else:
        form = articleForm()
    form = articleForm()
    context = {
        'dp_abb' : dpName,
        'sb_index' : sbIndex,
        'article' : article,
        'form' : form
    }
    return render(request, 'revise.html', context)

def deleteArticle(request, dpName, sbIndex, articleId):
    delete_article = Article.objects.get(id = articleId)
    delete_article.exist = False
    delete_article.save()
    for delete_comment in Comment.objects.filter(article_id = articleId):
        delete_comment.exist = False
        delete_comment.save()
    return HttpResponseRedirect('/department/' + dpName + '/' + sbIndex)

def deleteComment(request, dpName, sbIndex, articleId, commentId):
    delete_comment = Comment.objects.get(id=commentId)
    delete_comment.exist = False
    delete_comment.save()
    return HttpResponseRedirect('/department/' + dpName + '/' + sbIndex + '/' + articleId)

def replyArticle(request, dpName, sbIndex, articleId):
    load_article = Article.objects.get(id=articleId)
    form = commentForm()
    context = {
        'dp_abb' : dpName,
        'sb_index' : sbIndex,
        'article' : load_article,
    }

    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            try:
                form.id = Comment.objects.order_by('-id')[0].id + 1
            except IndexError:
                form.id = 1
            form.article_id = articleId            
            form.child_comment = []
            form.good_list = []
            form.bad_list = []
            form.post_date = timezone.now()
            form.revise_date = timezone.now()
            form.author = request.user.username
            form.parent_comment_id = 0
            form.save()
            context['form'] = form
            print("id="+form.article_id)
            return HttpResponseRedirect('/department/' + dpName + '/' + sbIndex + '/' + articleId)
    return render(request, 'reply.html', context)

def replyComment(request, dpName, sbIndex, articleId, commentId):
    load_article = Article.objects.get(id=articleId)
    replyto_comment = Comment.objects.get(id=commentId)
    context = {
        'dp_abb' : dpName,
        'sb_index' : sbIndex,
        'article' : load_article,
        'replyto_comment' : replyto_comment,
    }

    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            try:
                form.id = Comment.objects.order_by('-id')[0].id + 1
            except IndexError:
                form.id = 1
            form.article_id = articleId            
            form.child_comment = []
            form.good_list = []
            form.bad_list = []
            form.post_date = timezone.now()
            form.revise_date = timezone.now()
            form.author = request.user.username
            form.parent_comment_id = commentId
            form.save()
            context['form'] = form
            print("id="+form.article_id)
            return HttpResponseRedirect('/department/' + dpName + '/' + sbIndex + '/' + articleId)
    return render(request, 'reply.html', context)
