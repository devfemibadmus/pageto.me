from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.home, name="home"),
    re_path(r'^account.*$', views.account, name="account"),
    re_path(r'^analytics.*$', views.analytics, name="analytics"),
    re_path(r'^templates.*$', views.templates, name="templates"),
    re_path(r'^.*$', views.lost, name="lost"),
]
