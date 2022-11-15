from django.urls import path
from .views import index, acercade, base, secion

# Para nuestras direcciones.
urlpatterns = [
    path('', index, name = "inicio"),
    path('about/', acercade, name = "about"),
    path('secion/', secion, name = "secion"),
    path('base/', base)
]

 



