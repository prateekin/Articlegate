from django import forms
from django.db import models
from django.db.models import fields
from .models import Post

class CustomForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','about','content','tags']
        labels = {
            'title' : "Title",
            'about' : "Short Description",
            'content' : "Content",
            'tags' : "Tags",
        }