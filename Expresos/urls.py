from django.contrib import admin
from django.urls import path
from horariosApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('horarios/', views.horarios_views, name='horarios'),
    path('contacto/', views.contacto, name='contacto'),
]
