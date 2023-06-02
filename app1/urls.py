
from django.urls import path
from app2.views import *
app_name='app1'
urlpatterns=[

    path('jerry/',jerry,name='jerry')
]