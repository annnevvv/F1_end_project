from django.urls import path, include

from blog.views import BlogMainPageView, AllPostView, SinglePostView

urlpatterns = [
    path('', BlogMainPageView.as_view(), name='blog_main_page'),
    path('posts', AllPostView.as_view(), name='posts_list'),
    path("posts/<slug:slug>", SinglePostView.as_view(),
         name='single_post_page'),

]