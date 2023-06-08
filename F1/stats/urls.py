from django.contrib import admin
from django.urls import path
from stats.views import constructors, circuits, drivers, driver_results, driver_standings,upcoming_races_view, constructor_standings


urlpatterns = [
    path('', driver_results, name='driver-results-list'),
    path('constructors/', constructors, name='constructors'),
    path('circuits/', circuits, name='circuits'),
    path('drivers/', drivers, name="driver-list"),
    path('driver_results/', driver_results, name='driver-results-list'),
    path('driver_standings/', driver_standings, name='driver_standings'),
    path('constructor_standings/', constructor_standings, name='constructor_standings'),
    path('upcoming_races/', upcoming_races_view, name='upcoming_races')

]