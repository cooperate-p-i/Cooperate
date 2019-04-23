from django.contrib import admin

from .models import Rebanho, Cultura, Propriedade

admin.site.register(Rebanho)
admin.site.register(Cultura)
admin.site.register(Propriedade)
