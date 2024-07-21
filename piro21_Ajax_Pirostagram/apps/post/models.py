from django.db import models
from apps.users.models import User


# Create your models here.
class Post(models.Model):
   # 작성자
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
   photo = models.ImageField(blank=True, upload_to='posts/%Y%m%d')
   content = models.TextField()
   like = models.ManyToManyField(User, related_name='like_posts', blank=True)

class Comment(models.Model):
   # 작성자
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
   text = models.CharField(max_length=50)