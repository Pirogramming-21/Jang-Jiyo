from django.db import models

# Create your models here.
class Movie(models.Model):
   title = models.CharField(max_length = 20)
   release = models.IntegerField(default = 0)
   director = models.CharField(max_length = 15)
   leadrole = models.CharField(max_length = 50)
   genre_choices = (
      ('action', '액션'), ('adventure', '모험'), ('animation', '애니메이션'),
      ('comedy', '코미디'), ('crime', '범죄'), ('documentary', '다큐멘터리'),
      ('drama', '드라마'), ('family', '가족'), ('fantasy', '판타지'),
      ('noir', '느와르'), ('history', '역사'), ('musical', '뮤지컬'),
      ('horror', '공포'), ('romance', '로맨스'), ('sf', '공상과학'),
   )
   genre = models.CharField(max_length = 15, choices = genre_choices, default = 'action')
   evaluation = models.DecimalField(max_digits = 2, decimal_places = 1)
   runningtime = models.IntegerField(default = 0)
   review = models.TextField()