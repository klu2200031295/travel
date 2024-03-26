from django.contrib import admin
from django.urls import path
from.views import *

urlpatterns = [
    path('hello2/', hello1),
    path('hello/', hello, name='hello'),
    path('',newhomepage,name='newhomepage'),
    path('Travel/',travelpackage,name='travelpackage'),
    path('h/', print_to_console, name='print_to_console'),
    path('p/', print1, name='print1'),
    path('ran1/',random123,name='random123'),
    path('g/',getdate1,name='getdate1'),
    path('getdate/',get_date,name='get_date'),
    path('tzfunctioncall/', tzfunctioncall, name='tzfunctioncall'),
    path('reg/',registerloginfunction,name='registerloginfunction'),
    path('pie/',pie_chart,name='pie_chart'),
    path('pie1/', Pie, name='Pie'),
    path('s/',slide,name='slide'),
    path('t/',temp,name='temp'),
    path('w/',weatherlogic,name='weatherlogic'),
    path('sign/',signup,name='signup'),
    path('sign1/',signup1,name='signup1'),
    path('l/',login,name='login'),
    path('l1/',login1,name='login1'),
    path('lg/',logout,name='logout'),
    path('contactmail/',contactmail,name='contactmail'),
    path('contactmail1/',contactmail1,name='contactmail1'),

]