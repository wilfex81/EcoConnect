from django.urls import path
from .views import user_login, home, register,projects, events

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('projects/', projects, name = 'projects'),
    path("events/", events, name = 'events'),
]
