"""User serializers."""


# Django REST framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

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

class UserSignUpSerializer(serializers.Serializer):
    """User SignUp serializer.
    Handle sign up data validation and user/profile creation
    """

    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())] 
    )

    def create(self, data):
        user = User.objects.create_user(**data)
        return user