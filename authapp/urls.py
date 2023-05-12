

from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('sign-up',views.signup,name='sign-up')
]