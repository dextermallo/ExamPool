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
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
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
    context = dict()
    #load_article = Article.objects.filter(exist = True).filter(dp_abb = dpName).filter(sb_index = sbIndex).order_by("-id")
    load_article = Article.objects.filter(exist = True).filter(dp_abb = dpName).filter(sb_index = sbIndex).order_by("-id")
    form = searchForm(request.POST)
    
    if request.method == "POST":   
        print(request, file=sys.stderr)    
        if form.is_valid():
            
            tag = form.cleaned_data.get("tag")
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            author = form.cleaned_data.get("author")
            sort = form.cleaned_data.get("sort")
            whole_search = "?"
            if tag:
                whole_search += "tag=" + tag + "&"
            if title:
                whole_search += "title=" + title + "&"
            if content:
                whole_search += "content=" + content + "&"
            if author:
                whole_search += "author=" + author + "&"
            if sort:
                whole_search += "sort=" + sort + "&"
            return HttpResponseRedirect(whole_search)

    print(request.get_full_path(), file=sys.stderr)
    if request.GET.get("tag"):
        tag = request.GET.get("tag")
        load_article = load_article.filter(tag_name__contains = tag).order_by("-id")
        context["tag"] = tag
    if request.GET.get("title"):
        title = request.GET.get("title")
        load_article = load_article.filter(title__contains = title).order_by("-id")
        context["title"] = title
    if request.GET.get("content"):
        content = request.GET.get("content")
        load_article = load_article.filter(content__contains = content).order_by("-id")
        context["content"] = content
    if request.GET.get("author"):
        author = request.GET.get("author")
        load_article = load_article.filter(author__contains = author).order_by("-id")
        context["author"] = author
    if request.GET.get("sort"):
        sort = request.GET.get("sort")       
        load_article = load_article.order_by(sort)
        context["sort"] = sort
    if request.GET.get("page"):
        page = request.GET.get("page")
    else:
        page = 1

    limit = 5
    paginator = Paginator(load_article, limit)

    if int(page) < 1:
        page = 1
    if request.method == "POST":
        form = pageForm(request.POST)
        if form.is_valid():
            page = form.cleaned_data.get("page")
            try:
                load_article = paginator.page(page)
            except PageNotAnInteger:
                page = 1
            except EmptyPage:
                if page == 0:
                    page = 1
                else:
                    page = paginator.num_pages
            full_path = request.get_full_path()
            path = request.path
            whole_search = full_path.replace(path, "")
            page_pos = whole_search.find("page=")
            if page_pos > 0:
                whole_search = whole_search[:page_pos]
            if whole_search == "":
                whole_search = "?"
            return HttpResponseRedirect(whole_search + 'page=' + str(page))

    try:
        load_article = paginator.page(page)
    except PageNotAnInteger:
        load_article = paginator.page(1)
        page = 1
    except EmptyPage:
        load_article = paginator.page(paginator.num_pages)
        page = paginator.num_pages
    context['Article'] = load_article
    context['now_page'] = int(page)
    context['max_page'] = int(paginator.num_pages)

    return render(request, 'board.html', context)

def article(request, dpName, sbIndex, articleId):
    form = voteForm()
    try:
        load_article = Article.objects.filter(dp_abb = dpName).filter(sb_index = sbIndex).get(id = articleId)
    except Article.DoesNotExist:
        return render(request, 'noArticle.html')
    if not load_article or not load_article.exist:
        return render(request, 'noArticle.html')
    load_comment = Comment.objects.filter(article_id = articleId)
    dp_full_name = Department.objects.get(dp_abb = dpName).dp_name
    sb_full_name = Department.objects.get(dp_abb = dpName).sb_name[int(sbIndex) - 1]
    already_favorite = int(articleId) in User.objects.get(username=request.user.username).favorite.favorite
    user_contribution = 0
    author_contribution = 0
    for article in Article.objects.filter(author=load_article.author):
        author_contribution += len(article.good_list) - len(article.bad_list)
    for comment in Comment.objects.filter(author=load_article.author):
        author_contribution += len(comment.good_list) - len(comment.bad_list)
    for comment in load_comment:
        if comment.author == request.user.username:
            user_contribution += len(comment.good_list) - len(comment.bad_list)
    if load_article.author == request.user.username:
        user_contribution += len(load_article.good_list) - len(load_article.bad_list)
    commenters = load_comment.values_list('author', flat=True)
    comment_icon = []
    for name in commenters:
        try:
            comment_icon.append(str(User.objects.get(username=name).icon.icon))
        except User.icon.RelatedObjectDoesNotExist:
            comment_icon.append(None)
    print(comment_icon)
    context = {
        'User' : request.user,
        'Article' : load_article,
        'Comment' : load_comment,
        'tag_name' : [],
        'tag_count' : [],
        'article_goodbad_count' : len(load_article.good_list) - len(load_article.bad_list),
        'comment_goodbad_count' : [len(x.good_list) - len(x.bad_list) for x in load_comment],
        'user_contribution' : user_contribution,
        'department_name' : dp_full_name,
        'subject_name' : sb_full_name,
        'author' : User.objects.get(username = load_article.author),
        'comment_icon' : comment_icon,
        'already_favorite' : already_favorite,
    }

    try:
        max_tag = load_article.tag_name[load_article.tag_count.index(max(load_article.tag_count))]
        max_tag_count = load_article.tag_count[load_article.tag_count.index(max(load_article.tag_count))]
        tag_name_copy = load_article.tag_name.copy()
        tag_count_copy = load_article.tag_count.copy()
        tag_name_copy.remove(max_tag)
        tag_count_copy.remove(max_tag_count)
        else_tag = tag_name_copy
        else_tag_count = tag_count_copy
        context['max_tag'] = max_tag
        context['max_tag_count'] = max_tag_count
        context['else_tag'] = else_tag
        context['else_tag_count'] = else_tag_count
    except:
        pass
    context['author_contribution'] = author_contribution
    if request.method == 'POST':
        form = favoriteForm(request.POST)
        if form.is_valid():
            #if user's action is "add to favorite"
            #print(form.cleaned_data.get("article_id"))
            user_id = request.user.id
            article_id = int(form.cleaned_data.get("article_id"))
            user_favorite = Favorite.objects.get(user_id=user_id)
            if already_favorite:
                user_favorite.favorite.remove(article_id)
            else:
                user_favorite.favorite.append(article_id)
            user_favorite.save()
            already_favorite = int(articleId) in User.objects.get(username=request.user.username).favorite.favorite
            context["already_favorite"] = already_favorite
            context["form"] = form

            return render(request, 'article.html', context)

        form = tagForm(request.POST)
        if form.is_valid():
            try:
                index = load_article.tag_name.index(form.cleaned_data.get("tag_name"))
            except ValueError:
                load_article.tag_name.append(form.cleaned_data.get("tag_name"))
                load_article.save()
                index = load_article.tag_name.index(form.cleaned_data.get("tag_name"))
                load_article.tag_count.append(0)
                load_article.save()
            load_article.tag_count[index] += 1
            load_article.save()
            try:
                max_tag = load_article.tag_name[load_article.tag_count.index(max(load_article.tag_count))]
                max_tag_count = load_article.tag_count[load_article.tag_count.index(max(load_article.tag_count))]
                tag_name_copy = load_article.tag_name.copy()
                tag_count_copy = load_article.tag_count.copy()
                tag_name_copy.remove(max_tag)
                tag_count_copy.remove(max_tag_count)
                else_tag = tag_name_copy
                else_tag_count = tag_count_copy
                context['max_tag'] = max_tag
                context['max_tag_count'] = max_tag_count
                context['else_tag'] = else_tag
                context['else_tag_count'] = else_tag_count
            except:
                pass
            context['max_tag'] = max_tag
            context['max_tag_count'] = max_tag_count
            context['else_tag'] = else_tag
            context['else_tag_count'] = else_tag_count
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
                        be_voted = User.objects.get(username=load_article.author)
                        #be_voted.contribution[]++
                        
                    if user_vote == "bad":
                        load_article.bad_list.insert(0, user_name)
                        be_voted = User.objects.get(username=load_article.author)
                        #be_voted.contribution[]--
                    load_article.save()
                else:
                    load_comment_el = load_comment.get(id=comment_id)
                    if user_vote == "good":
                        load_comment_el.good_list.insert(0, user_name)
                        be_voted = User.objects.get(username=load_comment_el.author)
                        #be_voted.contribution[]++
                    if user_vote == "bad":
                        load_comment_el.bad_list.insert(0, user_name)
                        be_voted = User.objects.get(username=load_comment_el.author)
                        #be_voted.contribution[]--
                    load_comment_el.save()
            print(user_name)
            print(comment_id)
            print(user_vote)
            load_comment = Comment.objects.filter(article_id = articleId)
            context["form"] = form
            context["article_goodbad_count"] = len(load_article.good_list) - len(load_article.bad_list)
            context["comment_goodbad_count"] = [len(x.good_list) - len(x.bad_list) for x in load_comment]
            context["is_voted"] = is_voted

            user_contribution = 0
            for comment in load_comment:
                if comment.author == request.user.username:
                    user_contribution += len(comment.good_list) - len(comment.bad_list)
            if load_article.author == request.user.username:
                user_contribution += len(load_article.good_list) - len(load_article.bad_list)
            context["user_contribution"] = user_contribution

            return render(request, 'article.html', context)
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
    dp_full_name = Department.objects.get(dp_abb=dpName).dp_name
    sb_full_name = Department.objects.get(dp_abb = dpName).sb_name[int(sbIndex) - 1]
    #print(form)
    context = {
        'dp_abb' : dpName,
        'sb_index' : sbIndex,
        'department_name' : dp_full_name,
        'subject_name' : sb_full_name,
        'form' : form
    }
    return render(request, 'post.html', context)

def reviseArticle(request, dpName, sbIndex, articleId):
    article = Article.objects.get(id=articleId)
    if request.method == 'POST':
        print(1111)
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
    dp_full_name = Department.objects.get(dp_abb=dpName).dp_name
    sb_full_name = Department.objects.get(dp_abb = dpName).sb_name[int(sbIndex) - 1]
    context = {
        'dp_abb' : dpName,
        'sb_index' : sbIndex,
        'article' : article,
        'department_name' : dp_full_name,
        'subject_name' : sb_full_name,
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
    dp_full_name = Department.objects.get(dp_abb=dpName).dp_name
    sb_full_name = Department.objects.get(dp_abb = dpName).sb_name[int(sbIndex) - 1]

    context = {
        'dp_abb' : dpName,
        'sb_index' : sbIndex,
        'article' : load_article,
        'department_name' : dp_full_name,
        'subject_name' : sb_full_name,
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
    dp_full_name = Department.objects.get(dp_abb=dpName).dp_name
    sb_full_name = Department.objects.get(dp_abb = dpName).sb_name[int(sbIndex) - 1]
    context = {
        'dp_abb' : dpName,
        'sb_index' : sbIndex,
        'article' : load_article,
        'replyto_comment' : replyto_comment,
        'department_name' : dp_full_name,
        'subject_name' : sb_full_name,
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
