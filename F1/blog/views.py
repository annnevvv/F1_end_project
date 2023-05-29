from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import Post

# Create your views here.

all_posts = Post.objects.all().order_by('-date')


class BlogMainPageView(ListView):
    template_name = "blog/blog_main.html"
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'
