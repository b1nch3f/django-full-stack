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
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'myVar': 'welcome to templates.'
    }
    return render(request, 'first_app/index.html', context=data)
```
## Part-3 (REST)

### install djangorestframework
```
pip install djangorestframework
```
