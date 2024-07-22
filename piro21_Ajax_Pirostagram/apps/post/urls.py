from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
  path('', main, name='main'),
  path('create/', create, name='create'),
  path('<int:pk>/comment/', comment, name='comment'),
  path('<int:post_id>/comment/create_ajax/', comment_create, name='comment_create'),
  path('<int:post_id>/comment/<int:comment_id>/delete_ajax/', comment_delete, name='comment_delete'),
  path('<int:post_id>/like/', post_like, name="post_like"),
]