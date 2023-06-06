from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'user_name': 'Your Name',
            'user_email': 'Your Email',
            'txt': 'Your Comment'
        }
        # fields = ['user_name', 'user_email', 'txt', 'post']


class PostCreatedForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'txt', 'slug']
        # prepopulated = ['slug']
