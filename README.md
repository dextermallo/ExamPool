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





