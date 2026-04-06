from django.contrib import admin
from .models import Mensaje

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin): # <-- Solo un ".admin"
    list_display = ('emisor', 'receptor', 'fecha')