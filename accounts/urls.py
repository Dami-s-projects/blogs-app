"""Module contains URLs patterns that will be used for the 
app that manages the accounts"""

from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns=[
    path('',include('django.contrib.auth.urls')),
    #Registration page path
    path('register/',views.register,name='register'),



]

