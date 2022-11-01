# django-full-stack

## Part-1 (Basic)

### create project directory
```
mkdir project_dir
```
```
cd project_dir
```
### create virtual env
```
py -m venv venv
```
### activate virtual env
```
.\venv\Scripts\activate
```
### install Django
```
pip install Django
```
### create start project
```
django-admin startproject project_name .
```
### test
```
python .\manage.py runserver
```
### create start app
```
python .\manage.py startapp app_name
```
### add app_name to project project_name/settings.py
```
INSTALLED_APPS = [
    '...'
    'app_name'
]
```
### code hello-world in app_name/views.py
```
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')
```
### add url config in app_name/urls.py
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
### add url config in project_name/urls.py
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('first_app/', include('first_app.urls')),
    path('admin/', admin.site.urls),
]
```
## Part-2 (Template)

### create hello-world template in app_name/templates/app_name/index.html
```
<em>Hello World! {{ myVar }}</em>
```
### add template dir in project_name/settings.py
```
FIRST_APP_TEMPLATE_DIR = os.path.join(BASE_DIR, "first_app/templates")

TEMPLATES = [
    {
        '...',
        'DIRS': [FIRST_APP_TEMPLATE_DIR,],
        '...',
    },
]
```
### update hello-world in app_name/views.py
```
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'first_app/index.html'
```
### update url config in app_name/urls.py
```
from first_app.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]
```
## Part-3 (REST)

### install djangorestframework
```
pip install djangorestframework
```
### add app_name to project project_name/settings.py
```
INSTALLED_APPS = [
    '...'
    'rest_framework'
]
```
## Part-4 (Serialize)

### update first_app/models.py
```
from django.db import models

class Users(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
```
### makemigrations and migrate
```
python manage.py makemigrations
python manage.py migrate
```
### Add Record
```
py manage.py shell
```
```
from first_app.models import Users
```
```
Users.objects.all()
```
```
user = Users(firstname='Emil', lastname='Refsnes')
```
```
Users.objects.all().values()
```
### Add UserData API to first_app/views.py
```
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .models import Users
from django.core import serializers

import logging
logger = logging.getLogger(__name__)

class IndexView(TemplateView):
    template_name = 'first_app/index.html'

class UserData(APIView):
    def get(self, request, format=None):
        users = Users.objects.all()
        data = serializers.serialize("json", users)
        return Response(data)
```
### Update first_app/urls.py
```
from django.urls import path
from first_app.views import IndexView, UserData

urlpatterns = [
    path('', IndexView.as_view()),
    path('userdata', UserData.as_view(), name='UserData'),
]
```
## Part-5 (Front-End)

### Add jquery-3.6.1.min.js, script.js, style.css to first_app/static/first_app directory
```
console.log('js from first_app');

$(document).ready(function(){
    $.get("/first_app/userdata", function(data, status){
        console.log("Data: " + JSON.parse(JSON.stringify(data)) + "\nStatus: " + status);
    })
});
```
```
body {
    color: red;
}
```
