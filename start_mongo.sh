#!bin/bash

# To restart mongodb.
pid=$(lsof -i:27017 -t) 
kill -TERM $pid || kill -KILL $pid
mongod