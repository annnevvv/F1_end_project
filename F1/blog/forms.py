from django import forms

from .models import Comment,Post


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

        # def clean_slug(self):
        #     slug = self.cleaned_data['slug']
        #     if not slug:
        #         title = self.cleaned_data['title']
        #         slug = slugify(title)
        #     return slug
        #
        # fields = ['title', 'excerpt', 'txt', 'slug']

