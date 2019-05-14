from django.contrib import admin

from .models import Producao, Cultura, Propriedade

admin.site.register(Producao)
admin.site.register(Cultura)
admin.site.register(Propriedade)
