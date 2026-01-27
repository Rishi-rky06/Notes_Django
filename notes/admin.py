from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "updated_at")
    list_filter = ("updated_at", "owner")
    search_fields = ("title", "body", "owner__username")
