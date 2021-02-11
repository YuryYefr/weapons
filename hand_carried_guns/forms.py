from django import forms
from .models import Weapon


class DateInput(forms.DateInput):
    input_type = 'date'


class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = ['technical_name', 'creation_date', 'weight',
                  'rate_of_fire', 'ammo_capacity', 'currently_in_use', 'video_link']
        widgets = {
            'creation_date': DateInput
        }
