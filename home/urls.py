from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup.html', views.signup, name='signup'),
    path('login.html', views.login, name='login'),
    path('calendar.html', views.calendar, name='calendar'),
    path('contact.html', views.contact, name='contact'),
   
]