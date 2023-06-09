from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from blog.views import BlogMainPageView, AllPostView, SinglePostView, \
    createPost, postCreatedConfirmation

urlpatterns = [
                  path('', BlogMainPageView.as_view(), name='blog_main_page'),
                  path('posts', AllPostView.as_view(), name='posts_list'),
                  path("posts/<slug:slug>", SinglePostView.as_view(),
                       name='post-detail-page'),
                  path('create-post', createPost, name='create_post'),
                  path('create-post-confirm', postCreatedConfirmation,
                       name='create_post_confirmation'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
