"""Profile Models."""

# Django
from django.db import models

# Models
from plantch.utils.models import PlantchModel

class Profile(PlantchModel):
    """Profile model.
     A profile holds a user's public data like biography, picture,
    and statistics.
    """
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)
 
    def __str__(self):
        """Return user's str representation."""
        return str(self.user)