from django.contrib import admin
from .models import Perosn

@admin.register(Perosn)
class PersonAdmin(admin.ModelAdmin):
    pass