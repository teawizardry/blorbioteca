from django.contrib import admin
from .models import CharacterSheet

@admin.register(CharacterSheet)
class CharacterSheetAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']
    search_fields = ['user__username', 'name']