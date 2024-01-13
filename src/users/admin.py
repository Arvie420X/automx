from django.contrib import admin

from .models import Profiles, Location

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass
class LocationAdmin(admin.ModelAdmin):
    pass

# register function registered the model for the admin panel so it doesn't display it
admin.site.register(Profiles, ProfileAdmin)
admin.site.register(Location, LocationAdmin)