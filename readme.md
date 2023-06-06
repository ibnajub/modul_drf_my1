python -m venv /path/to/new/virtual/environment
pip install django
django-admin startproject mysite
python manage.py startapp myapp

pip freeze > requirements.txt  
pip install -r requirements.txt
python manage.py createsuperuser

from myapp.models import *

Уроки по Django REST Framework
https://www.youtube.com/watch?v=EVrMbS14FdE&list=PLA0M1Bcd0w8xZA3Kl1fYmOH_MfLpiYMRs&index=2&ab_channel=selfedu