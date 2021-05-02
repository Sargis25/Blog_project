from .models import CommentBlog
from django.forms import ModelForm,TextInput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm





class BlogApp(ModelForm):
    class Meta:
        model = CommentBlog
        fields = ['name', 'surname', 'email', 'subject', 'text']







