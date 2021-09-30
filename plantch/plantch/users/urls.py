"""Users URls."""
# Django
from django.urls import path

# Local
from .views import users as user_view

urlpatterns = [
    path('', user_view.MyView, name="sinup")
]