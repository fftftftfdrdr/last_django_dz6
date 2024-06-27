from django.urls import path
from .views import random_number_view

urlpatterns = [
    path('', random_number_view, name='random_number'),
]