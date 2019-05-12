# installation
brew install mongodb 
pip3 install django  
pip3 install djongo  
pip3 install django-widget-tweaks  
pip3 install Pillow

# usage
cd env  
source bin/activate  

# cmd
python3 manage.py shell  

# run
python3 manage.py runserver  

# migrate (syncdb)  
python3 manage.py migrate  

# quit   
deactivate  

# startup(on Mac)
cd env  
source bin/activate  
alias e="python3 manage.py"  
alias c="clear"  
e migrate  
c  

# kill port(on Mac)
lsof -i:<port-number>  
kill -9 <pid>  

# drop database
mongo <dbname> --eval "db.dropDatabase()"

# delete migrations (in root path)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete


