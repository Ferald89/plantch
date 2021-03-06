"""Main Urls module."""

# Django 
from django.contrib import admin
from django.urls import include, path
from django.conf import settings


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include(('plantch.users.urls', 'users'), namespace = "users")),
]
