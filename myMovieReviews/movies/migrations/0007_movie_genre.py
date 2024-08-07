# Generated by Django 4.2.14 on 2024-07-12 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_remove_movie_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('action', '액션'), ('adventure', '모험'), ('animation', '애니메이션'), ('comedy', '코미디'), ('crime', '범죄'), ('documentary', '다큐멘터리'), ('drama', '드라마'), ('family', '가족'), ('fantasy', '판타지'), ('noir', '느와르'), ('history', '역사'), ('musical', '뮤지컬'), ('horror', '공포'), ('romance', '로맨스'), ('sf', '공상과학')], default='action', max_length=15),
        ),
    ]
