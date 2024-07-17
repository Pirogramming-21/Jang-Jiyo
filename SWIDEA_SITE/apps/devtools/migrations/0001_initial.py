# Generated by Django 4.2.14 on 2024-07-17 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='개발툴 이름')),
                ('kind', models.CharField(max_length=24, verbose_name='종류')),
                ('content', models.TextField(verbose_name='설명')),
            ],
        ),
    ]
