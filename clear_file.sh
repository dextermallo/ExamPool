#!bin/bash

# delete migrations (in root path)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# run restart_mongo.sh first.
mongo ExamPool --eval "db.dropDatabase()"

