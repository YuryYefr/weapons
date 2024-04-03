from django import forms
from .models import Weapon


class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = ['technical_name', 'ammo_capacity',
                  'rate_of_fire',  'video_link', 'weight', 'weapon_type', 'currently_in_use', 'entered_service_date',]
