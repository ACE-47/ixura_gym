

from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.handleLogin,name='login'),

]