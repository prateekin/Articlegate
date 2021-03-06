# Generated by Django 3.2.7 on 2021-12-16 02:18

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('article', '0009_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='about',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
