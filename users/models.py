from django.db import models
from django.contrib.auth.forms import UserCreationForm


# Create your models here.

class UserCreate(UserCreationForm):
    first_name = models.CharField(max_length=12, default='')
    last_name = models.CharField(max_length=12, default='')
    email = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=12, default='')

    def __str__(self):
        return f'{self.first_name, self.last_name}'
