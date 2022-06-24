import json
from src.models import *
from django.contrib import admin

from src.models import UserProfile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ['user']}),
        ('Personal Info', {'fields': ['bio', 'phone', 'picture']}),
    )


admin.site.register(UserProfile, ProfileAdmin)


# admin.site.register(UserProfile)
admin.site.register(Posts)


# register the moving details
class MovingDetailsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ['user']}),
        ('Moving Details', {'fields': ['address', 'destination', 'luggage_size']}),
    )

admin.site.register(MovingDetails, MovingDetailsAdmin)

