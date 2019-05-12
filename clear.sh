#!bin/bash

# delete migrations (in root path)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

mongo ExamPool --eval "db.dropDatabase()"

#source bin/activate
alias pm="python3 manage.py"
#pm makemigrations
#pm migrate

