from django.db import models
from apps.devtools.models import DevTool

# Create your models here.
class Idea(models.Model):
   title = models.CharField('아이디어명', max_length=24)
   # 이미지
   photo = models.ImageField('이미지', blank=True, upload_to='ideas/%Y%m%d')
   content = models.TextField('아이디어 설명')
   interest = models.IntegerField('아이디어 관심도', default=0)
   devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE, verbose_name='예상 개발툴')

   def __str__(self):
      return self.title