

from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login, name='login'),
    path("creat_doc", views.creat_doc, name='creat_doc'),
    path("home", views.home, name='home'),
    path("teste", views.teste, name='teste'),
]


