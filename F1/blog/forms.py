from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'user_name': 'Your Name',
            'user_email': 'Your Email',
            'txt': 'Your Comment'
        }


class PostCreatedForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'txt', 'slug']
