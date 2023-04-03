from django.urls import path
from .views import *

urlpatterns = [
    path('register/',Register,name='register'),
    path('signin/',Signin,name='signin'),
]