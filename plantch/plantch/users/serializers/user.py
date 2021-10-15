"""User serializers."""


# Django REST framework
from rest_framework import serializers

# Model
from ..models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email', 
            'phone_number',
            'first_name'
            ]
