"""cooperate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.templatetags.static import static
from django.urls import path, include

from cooperate import settings

urlpatterns = [
    path('jet/', include('jet.urls')),  # GRAPELLU
    path('admin/', admin.site.urls),
    path('membros/', include('apps.pessoal.urls')),
    path('familias/', include('apps.pessoal.urls')),
    path('producao/', include('apps.ambiental.urls')),
    path('culturas/', include('apps.ambiental.urls')),
    path('propriedades/', include('apps.ambiental.urls')),
    path('ambiental/', include('apps.ambiental.urls')),
    path('orcamento/', include('apps.financeiro.urls')),
    path('rentabilidade/', include('apps.financeiro.urls')),
    path('clientes/', include('apps.clientes.urls')),
    path('', include('apps.core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
