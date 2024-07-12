from django.urls import path
from .views import *

app_name = 'movies'

urlpatterns = [
   path('', movie_list),
   path('/create', movie_create),
   path('/<int:pk>', movie_detail),
   path('/<int:pk>/update', movie_update),
   path('/<int:pk>/delete', movie_delete),
]