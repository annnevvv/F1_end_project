from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
                  path('', views.index, name='events'),
                  path('<slug:event_slug>/success', views.confirm_registration,
                       name='confirm-registration'),
                  path('<slug:event_slug>', views.event_details,
                       name='event-detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
