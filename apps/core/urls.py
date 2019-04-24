from django.urls import path

from apps.core.views import home

urlpatterns = (
    path('', home, name = 'home'),

)