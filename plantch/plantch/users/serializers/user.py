"""User serializers."""

# Django
from django.contrib.auth import password_validation, authenticate

# Django REST framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

# Model
from plantch.users.models import User
from plantch.users.models import Profile

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
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())] 
    )

    password = serializers.CharField(min_length=8, max_length=30)
    password_confirmation = serializers.CharField(min_length=8, max_length=30)

    def validate(self, data):
        """Verify pass"""
        password = data['password']
        password_conf = data['password_confirmation']
        if password != password_conf:
            raise serializers.ValidationError("Password doesn't match")
        password_validation.validate_password(password)
        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        Profile.objects.create(user=user)
        return user

class UserLoginSerializer(serializers.Serializer):
    """User Login serializer.
    Handle the login request
    """
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token,created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
