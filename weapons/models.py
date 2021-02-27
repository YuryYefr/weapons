from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from datetime import date

# Create your models here.

WEAPON_TYPE = [
    ('hand_carried_gun', 'Hand Carried'),
    ('vehicle', 'Vehicle')
]
YEAR_CHOICES = [(d, d) for d in range(1960, date.today().year)]


class Weapon(models.Model):
    technical_name = models.CharField(max_length=200)
    entered_service_date = models.IntegerField('Entered service', choices=YEAR_CHOICES)
    weight = models.FloatField()
    rate_of_fire = models.IntegerField()
    ammo_capacity = models.IntegerField()
    currently_in_use = models.BooleanField()
    video_link = models.URLField(blank=True)
    slug = models.SlugField(default='', blank=True)
    weapon_type = models.CharField(max_length=40, choices=WEAPON_TYPE, default='hand_carried_gun')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.technical_name)
        super(Weapon, self).save()

    def __str__(self):
        return self.technical_name

    def get_absolute_url(self):
        return reverse('weapons: detail', kwargs=({'pk': self.pk}))
