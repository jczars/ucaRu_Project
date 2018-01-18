## Projeto ucaRu
### tutoriais
https://wsvincent.com/django-allauth-tutorial/
https://djangoforbeginners.com/blog/
https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html

## virtualenvs
python3 -m venv ~/.virtualenvs/ucaRuProj
source ~/.virtualenvs/ucaRuProj/bin/activate
pip install django
django-admin.py startproject ucaRu_Project
cd ucaRu_Project/
ls
./manage.py migrate
./manage.py runserver
pip install django-allauth

## criando accounts
./manage.py startapp accounts
./manage.py migrate
./manage.py runserver

## registrando app
setting.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'accounts'
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'

## # myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]

## migrate
./manage.py migrate

### sites
127.0.0.1

### Social Applications
### google
https://console.developers.google.com/project

### create views.py
### myproject/views.py
from django.views.generic import TemplateView
class Home(TemplateView):
    template_name = 'home.html'
### myproject/settings.py
TEMPLATES = [
    ...
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    ...
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'BD_ucaRu',
        'USER': 'root',
        'PASSWORD': 'jc1122',
        'HOST': 'localhost',
        'PORT': '',
    }
}

### mySQL client
sudo apt-get install python-django
mysql -u root -p

mysql> create database BD_ucaRu;
mysql>exit

## templates
templates/login.html
<!-- templates/home.html -->
{% load socialaccount %}

<h1>Django Allauth Tutorial</h1>
{% if user.is_authenticated %}
<p>Welcome {{ user.username }} !!!</p>
{% else %}
<a href="{% provider_login_url 'google' %}">Sign Up</a>
{% endif %}

### myproject/urls.py
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('accounts.urls')),
]

### accounts/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.SignUpView.as_view(), name='login'),
]

## views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'login.html'

## super user
./manage.py createsuperuser
jczars
jcdjangoss


./manage.py runserver
http://127.0.0.1:8000/admin/
logg de admin

127.0.0.1:8000

## migrate
./manage.py makemiations accounts
./manage.py migrate accounts

## git 
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/jczars/ucaRu_Project.git
git push -u origin master

## app cardapio
./manage.py startapp cardapio
## urls.py
path('cardapio/', include('cardapio.urls')),

## cardapio/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
]

### cardapio/views
from django.views.generic import ListView, DetailView
from . models import Cardapio

class HomeListView(ListView):
    model = Cardapio
    template_name = 'home.html'

### template
cardapio/template

<!-- templates/home.html -->
{% extends 'base.html' %}

{% block content %}
  {% for Cardapio in object_list %}
    <div class="post-entry">
      <h2><a href="">{{ Cardapio.pratoPrincipal }}</a></h2>
      <p>{{ post.refeicao }}</p>
    </div>
  {% endfor %}
{% endblock content %}

<!-- templates/base.html -->
<html>
  <head>
    <title>Django blog</title>
  </head>
  <body>
    <header>
      <h1><a href="/">Django blog</a></h1>
    </header>
    <div class="container">
      {% block content %}
      {% endblock content %}
    </div>
  </body>
</html>

### cardapio/models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Cardapio(models.Model):
    pratoPrincipal = models.TextField(max_length=30)
    refeicao = models.TextField(max_length=30)
    salada = models.TextField(max_length=30)
    acompanhamento = models.TextField(max_length=30)
    sobremesa = models.TextField(max_length=30)
    observa = models.TextField(blank=True, null=True)
    dataCap = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pratoPrincipal

class Reserva(models.Model):
    resData = models.DateField(default=date.today)
    resHora = models.TimeField()
    idCap = models.ForeignKey(Cardapio, null=True, related_name='reserva', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.resData

## Registra App
'cardapio'

## Registra Admin
from django.contrib import admin
from . models import Cardapio
# Register your models here.
admin.site.register(Cardapio)

## migrate BD
./manage.py migrate cardapio

./managy runserver

## cadastrar no admin os cardapios

## static files
cardapio/static/css

# myproject/settings.py
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]






