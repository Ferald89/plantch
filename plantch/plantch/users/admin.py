"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from plantch.users.models import User

admin.site.register(User, UserAdmin)