from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    about = models.CharField(default="",max_length=200)
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    tags  = models.CharField(default="",max_length=150)
    # tags  = TaggableManager()
    def __str__(self):
        if len(self.title) > 50:
            return self.title[:50]+"..."
        return self.title

class Tag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.CharField(max_length=25)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    visitor = models.IntegerField(default=None)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(default="",max_length=25)
    image_url = models.CharField(default="",max_length=100)
    comment = models.TextField()
    likes = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if len(self.comment) > 50:
            return self.comment[:50]+"..."
        return self.comment
