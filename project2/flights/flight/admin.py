from django.contrib import admin

from . import models

# Register your models here.
class flightadmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination', 'duration')

admin.site.register(models.Flights,flightadmin)
admin.site.register(models.Airport)
admin.site.register(models.Passenger)