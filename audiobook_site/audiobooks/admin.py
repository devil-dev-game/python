from django.contrib import admin
from .models import Audiobook

@admin.register(Audiobook)
class AudiobookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
