# django-full-stack

mkdir project_dir

cd project_dir

py -m venv venv

.\venv\Scripts\activate

pip install Django

django-admin startproject project_name .

python .\manage.py runserver

python .\manage.py startapp app_name

# project_dir/settings.py
INSTALLED_APPS = [
    '...'
    'app_name'
]

# app_dir/views.py
import imp
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')

# app_dir/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

#project_dir/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('first_app/', include('first_app.urls')),
    path('admin/', admin.site.urls),
]

# project_dir/templates/app_name/index.html
<em>Hello World! {{ myVar }}</em>

# project_dir/settings.py 
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        '...',
        'DIRS': [TEMPLATE_DIR,],
        '...',
    },
]

# project_dir/app_name/views.py
import imp
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'myVar': 'welcome to templates.'
    }
    return render(request, 'first_app/index.html', context=data)
