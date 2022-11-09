from django.urls import path
from .views import index, acercade


urlpatterns = [
    path('', index),
    path('about/', acercade)
]