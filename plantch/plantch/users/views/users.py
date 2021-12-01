"""Users views."""

# Django REST Framework
from rest_framework import mixins,status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from plantch.users.serializers import (
                                UserModelSerializer, 
                                UserSignUpSerializer,
                                UserLoginSerializer,
                                ProfileModelSerializer
                                )

# Models
from plantch.users.models import User

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet  
                                            ):
    """User view set.
    handle sign up, login and account verification.
    """
    serializer_class = UserModelSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=["post"])
    def login(self, request):
        """User log in."""
        serializers = UserLoginSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user, token = serializers.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data 
        return(Response(data, status=status.HTTP_201_CREATED))

    @action(detail=False, methods=['put', 'patch'])
    def profile(self, request, *args, **kwargs):
        """Update profile data."""
        user = self.get_object()
        profile = user.profile
        partial = request.method == 'PATCH'
        serializer = ProfileModelSerializer(
            profile,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()   
        data = UserModelSerializer(user).data
        return Response(data)
        