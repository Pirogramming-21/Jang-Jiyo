from django.urls import path
from .views import *

app_name = 'movies'

urlpatterns = [
   path('', movie_list),
   path('/create', movie_create),
   path('/<int:pk>', movie_detail),
]