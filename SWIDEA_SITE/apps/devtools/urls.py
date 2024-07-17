from django.urls import path
from .views import *

app_name = 'devtools'

urlpatterns = [
  path('/list', list, name='list'),
  path('/register', register, name='register'),
  path('/detail/<int:pk>', detail, name='detail'),
  path('/delete/<int:pk>', delete, name='delete'),
  path('/update/<int:pk>', update, name='update'),
]