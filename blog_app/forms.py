from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class PostForm((forms.ModelForm)):
    class Meta:
        # We tell this form to use the Post model as its blueprint
        model = Post
        # We specify which fields from the Post model we want to show on the form
        fields = ['title', 'content']