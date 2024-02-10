from django.contrib import admin

from .models import Blog

@admin.register(Blog)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_datetime', 'status']
