#!bin/bash

# To start django.
source bin/activate
alias pm='python3 manage.py'
alias pmr='python3 manage.py runserver'
pm makemigrations
pm migrate