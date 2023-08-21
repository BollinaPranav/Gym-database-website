
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('saverecords', views.saverecords, name='saverecords'),
    path('home', views.home, name='home'),
    path('index', views.saverecords, name='index'),
    path('connsql', views.connsql, name='connsql'),
    path('addtrainer', views.addtrainer, name='addtrainer'),
    path('trainerview', views.trainerview, name='trainerview'),
    path('showclient/<clientid>',views.showclient, name='showclient'),
    path('searchclients', views.searchclients, name='searchclients'),

]
