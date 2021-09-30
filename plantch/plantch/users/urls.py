"""Users URls."""
# Django
from django.urls import path, include
# Django REST 
from rest_framework import routers

# Local
from .views import users as user_view

router = routers.DefaultRouter()
router.register(r'users', user_view.UserViewSet)

urlpatterns = [
    path('', include(router.urls), name="sinup")
]