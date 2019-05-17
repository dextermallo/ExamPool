# PRE-REQUIREMENTS
1. Python 3.7.3
2. Mongodb 4.0.3
3. virtualenv
# HOW TO RUN

1. load virtualenv
```sh
source bin/activate
```
2. install requirements.  
```sh
pip install -r requirements.txt  
```
3. start mongodb.  
```sh
source start_mongo.sh   
```
4. start inverment.   
```sh
source start_env.sh
```
5. import data.
```sh
source data_import.sh
```
6. run server.
```sh
python3 manage.py runserver
```