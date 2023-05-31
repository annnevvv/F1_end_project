from django.urls import path, include

from F1.blog.migrations import views

urlpatterns = [
    path('', views.BlogMainPageView.as_view(), name='blog_main_page'),
    path('posts', views.AllPostView.as_view(), name='posts_list'),
    path("posts/<slug:slug>", views.SinglePostView.as_view(),
         name='single_post_page'),

]