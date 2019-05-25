from django.shortcuts import render
from .models import *
import sys

# Create your views here.
def update_user_profile(request):
    print("===", file=sys.stderr)
    for i in request:
        print(i, file=sys.stderr)
    print("===", file=sys.stderr)
    if request.user.is_authenticated:
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        print(last_name, file=sys.stderr)
        print("@@@", file=sys.stderr)
        print(email, file=sys.stderr)
        password = request.POST.get('password', '')
        password_check = request.POST.get('password_check', '')
        request.user.update_profile(email=email, first_name=first_name,last_name=last_name,password=password)
    else:
        return render(request, '/index/')