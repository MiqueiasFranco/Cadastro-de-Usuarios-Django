
from django.contrib import admin
from django.urls import path
from appcadastrousuarios import views
urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
]
