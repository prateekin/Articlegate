# Generated by Django 3.2.7 on 2021-11-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='', max_length=25),
        ),
    ]
