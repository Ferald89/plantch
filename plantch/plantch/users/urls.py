"""Users URls."""

# Django
from django.urls import path, include

# Django REST 
from rest_framework.routers import DefaultRouter

# Local
from .views import users as user_view

router = DefaultRouter()
router.register(r'users', user_view.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]