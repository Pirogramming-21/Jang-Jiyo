from django.urls import path
from .views import *

app_name = 'ideas'

urlpatterns = [
  path('', main, name='main'),
  path('/toggle_star/<int:pk>', toggle_star, name='toggle_star'),
  path('/register', register, name='register'),
  path('/detail/<int:pk>', detail, name='detail'),
  path('/delete/<int:pk>', delete, name='delete'),
  path('/update/<int:pk>', update, name='update'),
]