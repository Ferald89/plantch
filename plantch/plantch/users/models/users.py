"""User Models."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Models
from plantch.utils.models import PlantchModel

class User(PlantchModel, AbstractUser):
    
    phone_regex = RegexValidator(
         regex=r'\+?1?\d{9,15}$',
         message="Phone number must be entered in the format: +9999999. up to 15 digits allowed."
         )
    
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def ___str__(self):
        return self.username

    def get_short_name(self):
        return self.username