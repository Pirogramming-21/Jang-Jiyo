# Generated by Django 4.2.14 on 2024-07-12 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='direcor',
            new_name='director',
        ),
    ]
