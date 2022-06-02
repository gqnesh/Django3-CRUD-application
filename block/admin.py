from django.contrib import admin
from block import models

# Register your models here.

@admin.register(models.Post)
class ModelPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'user_id']
