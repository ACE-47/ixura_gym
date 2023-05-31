

from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('sign-up',views.signup,name='signup'),
    path('log-in',views.handleLogin,name='login'),
    path('log-out',views.handleLgout,name='logout'),
    path('contact',views.contact,name='contact'),
    path('enroll',views.enrollment,name='enroll'),

]