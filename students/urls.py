from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.homepage, name='home'),
    path('sidebar', views.sidebar, name='sidebar'),
    path('form', views.form, name='form'),
    path('bsit', views.bsit, name='bsit'),
    path('bsce', views.bsce, name='bsce'),
]