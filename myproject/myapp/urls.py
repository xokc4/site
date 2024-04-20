from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # URL для представления "Главная"
    path('about/', views.about, name='about'),  # URL для представления "О себе"
]