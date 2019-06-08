from django.shortcuts import render
from .models import *
import sys
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from catalog.models import *
from django.contrib import auth
from django.template import loader, Context, RequestContext
from collections import Counter

def login(request):
    
    if request.user.is_authenticated: 
        return HttpResponseRedirect('/index/')
    
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = User.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            print("***********", file=sys.stderr)
            auth.login(request, user)
            print("***********", file=sys.stderr)
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
        Icon.create_icon(user.id, './user_img.png')
        Contribution.create_contribution(user.id)
        Favorite.create_favorite(user.id)
        Voting.create_voting(user.id)        
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
		print(request.user.username, file=sys.stderr)
		result = User.objects.get(username = username) 
		#articles = Article.objects.all().filter(author = username)
		print('========================', file=sys.stderr)
		icon = Icon.objects.get(user_id = request.user.id)
		print(str(icon.icon.url), file=sys.stderr)
		print('========================', file=sys.stderr)
		reply_count = {}
		print("***************", file=sys.stderr)
		# for article in articles:
		# 	comments = Comment.objects.all().filter(article_id = article.id)
		# 	reply_count[article.id] = len(Counter(comments)) if comments is not None else 0
		print("***************", file=sys.stderr)
		ret = {
			'username': result.username,
			'email': result.email,            
			'first_name': result.first_name,
			'last_name': result.last_name,            
			#'contribution': articles,
			#'reply': reply_count,
			'icon': icon.icon.url,
            'comments': None,
		}    
	except:
		ret = {
			'result': False,
		}
		print('Except', file=sys.stderr)
	return render(request, 'accounts/info.html', ret)

def update_user_profile(request):

    if request.user.is_authenticated:
        username = request.user.username
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        User.update_profile(username, email, first_name, last_name, password)

        return HttpResponseRedirect('/index/')
    else:
        return render(request, '/index/')

def update_user_icon(request):
	if (request.user.is_authenticated) & (request.method == 'POST'):		
		form = UserImageForm(request.POST, request.FILES)
		if form.is_valid():
			if Icon.objects.filter(pk=request.user) is not None:
				Icon.create_icon(request.user.id, form.cleaned_data['image'])
			else:
				Icon.objects.filter(pk=request.user.id).update(icon=form.cleaned_data['image'])
			return HttpResponseRedirect('/accounts/info/' + request.user.username)

	else:	
		form = UserImageForm()
		return render(request, 'index.html', locals())
