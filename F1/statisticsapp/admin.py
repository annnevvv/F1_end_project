from django.contrib import admin

from statisticsapp.models import Constructor, Driver, Circuit, DriverResult, DriverStanding

admin.site.register(Constructor)
admin.site.register(Driver)
admin.site.register(Circuit)
admin.site.register(DriverResult)
admin.site.register(DriverStanding)