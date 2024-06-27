from django.contrib import admin
from .models import RandomNumber

@admin.register(RandomNumber)
class RandomNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'number')
   
