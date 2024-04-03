from django.contrib import admin
from .models import Weapon


# Register your models here.

class WeaponAdminPanel(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['technical_name', 'weapon_type', 'entered_service_date', 'video_link']}),
        ('Model info', {'fields': ['weight', 'rate_of_fire', 'ammo_capacity', 'currently_in_use'], 'classes': [
            'collapse']}),
    ]
    list_filter = ['entered_service_date']
    search_fields = ['technical_name']


admin.site.register(Weapon, WeaponAdminPanel)
