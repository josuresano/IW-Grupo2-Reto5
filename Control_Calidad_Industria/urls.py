"""
URL configuration for Control_Calidad_Industria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Gestion_NC import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('nc/', views.lista_nc, name='lista_nc'),
    path('acciones/', views.lista_acciones, name='lista_acciones'),
    path('responsables/', views.lista_responsables, name='lista_responsables'),
    path('detalle/<int:id_nc>/', views.detalle_nc, name='detalle_nc'),
    path('nc/alta/', views.alta_nc, name='alta_nc'),
    path('nc/editar/<int:id_nc>/', views.editar_nc, name='editar_nc'),
    path('nc/borrar/<int:id_nc>/', views.borrar_nc, name='borrar_nc'),
    path('acciones/alta/', views.alta_accion, name='alta_accion'),
    path('acciones/editar/<int:id_ac>/', views.editar_accion, name='editar_accion'),
    path('acciones/borrar/<int:id_ac>/', views.borrar_accion, name='borrar_accion'),
]
