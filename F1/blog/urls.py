from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import BlogMainPageView, AllPostView, SinglePostView, create_post, PostCreatedConfirmationView

urlpatterns = [
                  path('', BlogMainPageView.as_view(), name='blog_main_page'),
                  path('posts', AllPostView.as_view(), name='posts_list'),
                  path("posts/<slug:slug>", SinglePostView.as_view(),
                       name='post-detail-page'),
                  path('create-post', create_post, name='create_post'),
                  path('create-post-confirm', PostCreatedConfirmationView.as_view(),
                       name='create_post_confirmation'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
