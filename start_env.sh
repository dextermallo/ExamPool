#!bin/bash

# To start django.
source bin/activate
alias pm='python3 manage.py'
pm makemigrations
pm migrate