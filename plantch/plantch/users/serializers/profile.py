"""Profile serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from plantch.users.models import Profile

class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer."""

    model = Profile
    fields = (
        'picture',
        'biography'
    )