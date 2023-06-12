from django.conf import settings
from django.urls import path
from stats.views import constructors, circuits, drivers, driver_results, driver_standings, upcoming_races_view, \
    constructor_standings, stats, driver_standings_chart
from django.conf.urls.static import static

urlpatterns = [
    path('', stats, name='stats'),
    path('constructors/', constructors, name='constructors'),
    path('circuits/', circuits, name='circuits'),
    path('drivers/', drivers, name="driver-list"),
    path('driver_standings/', driver_standings, name='driver_standings'),
    path('constructor_standings/', constructor_standings, name='constructor_standings'),
    path('upcoming_races/', upcoming_races_view, name='upcoming_races'),
    path('driver_results/<str:circuitid>/<str:circuit_name>/', driver_results, name='driver_results'),
    path('chart/', driver_standings_chart, name='driver_standings_chart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)