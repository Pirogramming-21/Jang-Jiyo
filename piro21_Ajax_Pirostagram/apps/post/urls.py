from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
  path('', main, name='main'),
  path('create/', create, name='create'),
  path('<int:pk>/comment/', comment, name='comment'),
  path('<int:pk>/comment/create', comment_create, name='comment_create'),
  path('<int:post_pk>/comment/<int:comment_pk>/delete/', comment_delete, name='comment_delete'),
  path('like/', like, name='like'),
]