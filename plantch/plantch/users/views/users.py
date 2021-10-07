"""Users views."""

from django.http import HttpResponse
from django.views import View

from rest_framework import serializers, viewsets

# Models
from plantch.users.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
