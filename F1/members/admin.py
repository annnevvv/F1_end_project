from django.contrib import admin
from stats.models import (
    Circuits, Constructors,  DriverStandings, ConstructorStandings, Drivers, DriversResults)

admin.site.register(Circuits)
admin.site.register(Constructors)
admin.site.register(DriverStandings),
admin.site.register(ConstructorStandings),
admin.site.register(Drivers),
admin.site.register(DriversResults),
