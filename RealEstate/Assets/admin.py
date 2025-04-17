from django.contrib import admin
from .models import Client,House



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display=['id','fullname','phone1']
    list_filter = ['clientType']
    
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'rooms', 'location']
    list_filter=['location']
