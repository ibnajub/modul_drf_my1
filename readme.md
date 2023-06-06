python -m venv /path/to/new/virtual/environment
pip install django
django-admin startproject mysite
python manage.py startapp myapp

pip freeze > requirements.txt  
pip install -r requirements.txt
python manage.py createsuperuser

from myapp.models import *