from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from aboutpage.views import about

urlpatterns = [
    path('', about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)