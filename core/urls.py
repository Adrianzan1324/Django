from django.contrib import admin
from django.urls import path
from .views import saludo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', saludo, name='saludo'),  # La ruta vacía '' representa la página de inicio
]