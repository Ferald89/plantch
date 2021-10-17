"""Users views."""

# Django REST Framework
from rest_framework import mixins,status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from plantch.users.serializers import UserModelSerializer, UserSignUpSerializer

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

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        # import ipdb; ipdb.set_trace()
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data 
        return(Response(data, status=status.HTTP_201_CREATED))
