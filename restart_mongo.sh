#!bin/bash

pid=$(lsof -i:27017 -t) 
kill -TERM $pid || kill -KILL $pid
mongod

#mongo ExamPool --eval "db.dropDatabase()"
