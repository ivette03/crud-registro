
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudiantes/',include("estudiantes.urls")),
    path('inicio/',views.inicio,name='inicio'),
    
]
