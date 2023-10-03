from django.contrib import admin
from service.models import Service



class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_tiltle']
    
admin.site.register(Service,ServiceAdmin)

# Register your models here.

