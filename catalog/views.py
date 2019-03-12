from django.shortcuts import render
from catalog.models import user
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

def index(request):
    limit = 5
    user_page = user.objects
    paginator = Paginator(user_page, limit)

    page_num = request.GET.get('page', 1)
    loaded = paginator.page(page_num)
    context = {
        'user': loaded
    }
    return render(request, "index.html", context)


def accessAddUserPage(request):
    return render(request, "addUser.html")

def addUser(request):
    if request.method == 'POST':
        idNumber = request.POST.get("idNumber", None)
        name = request.POST.get("name", None)
        age = request.POST.get("age", None)
        mailbox = request.POST.get("mailbox", None)
        power = request.POST.get("power", None)
        password = request.POST.get("password", None)
        
        # Save to database.
        ret = user(idNumber = idNumber, name = name, age = age, mailbox = mailbox, power = power, password = password)
        ret.save()
    return HttpResponseRedirect('/index/')

def AccessupdateUserPage(request):
    if request.method == 'GET':
        idNumber = request.GET.get("number", None)
        select_user = user.objects.filter(idNumber = idNumber)
        context = {
            'user': select_user
        }
        return render(request, "updateUser.html", context)

def updateUser(request):
    if request.method == 'POST':
        idNumber = request.POST.get("idNumber", None)
        name = request.POST.get("name", None)
        age = request.POST.get("age", None)
        mailbox = request.POST.get("mailbox", None)
        power = request.POST.get("power", None)
        password = request.POST.get("password", None)
        ret = user.objects.filter(idNumber = idNumber).update(name = name, age = age, mailbox = mailbox, power = power, password = password)
    return HttpResponseRedirect('/index/')

def deleteUser(request):
    if request.method == 'GET':
        idNumber = request.GET.get("idNumber", None)
        res = user.objects.filter(idNumber = idNumber).delete()
        print(res)
        return HttpResponseRedirect('/index/')