from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class Weapon(models.Model):
    technical_name = models.CharField(max_length=200)
    creation_date = models.DateField('Entered service')
    weight = models.FloatField()
    rate_of_fire = models.IntegerField()
    ammo_capacity = models.IntegerField()
    currently_in_use = models.BooleanField()
    video_link = models.URLField(blank=True)
    slug = models.SlugField(default='', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.technical_name)
        super(Weapon, self).save()

    def __str__(self):
        return self.technical_name

    def get_absolute_url(self):
        return reverse('hand_carried_guns: weapons_detail', kwargs=({'pk': self.pk}))
