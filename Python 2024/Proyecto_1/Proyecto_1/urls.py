"""
URL configuration for Proyecto_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Proyecto_1.views import pagina, paginaDatosPersonales, operacionesBasicas, formularios, captura, informacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paginaIncio/', pagina),
    path('paginaEmpleado/', paginaDatosPersonales),
    path('operacionesBasicas/', operacionesBasicas),
    path('formularios/', formularios),
    path('captura/', captura, name='captura'),
    path('informacion/', informacion, name='informacion'),
    path('', paginaDatosPersonales),
]
