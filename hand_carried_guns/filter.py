"""here we create search form"""
import django_filters
from .models import Weapon


class WeaponsFilter(django_filters.FilterSet):
    IN_USE = (
        ('1', 'Yes'),
        ('0', 'No')
    )

    currently_in_use = django_filters.ChoiceFilter(choices=IN_USE, label='active')

    class Meta:
        model = Weapon
        fields = {'weight': ['lt', 'gt'], 'rate_of_fire': ['lt', 'gt'], 'ammo_capacity': ['lt', 'gt'],
                  'currently_in_use': []}
