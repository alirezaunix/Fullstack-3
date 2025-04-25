from django.contrib import admin
from .models import Family,IOMoney
# Register your models here.

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    pass

@admin.register(IOMoney)
class IOMoneyAdmin(admin.ModelAdmin):
    pass