# Generated by Django 3.2.7 on 2021-11-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20211123_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='github',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.CharField(default='', max_length=100),
        ),
    ]
