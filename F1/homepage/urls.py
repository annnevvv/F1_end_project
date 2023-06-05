from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from homepage.views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)