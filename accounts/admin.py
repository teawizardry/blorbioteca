'''
    Blorbioteca is a free and open source character and world repository.
    Copyright (C) 2025 Hannah Kirkland

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from django.contrib import admin
from .models import InviteCode, UserProfile

@admin.register(InviteCode)
class InviteCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'is_active']
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    actions = ['deactivate_codes', 'activate_codes']

    def deactivate_codes(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, f'{queryset.count()} invite code(s) have been deactivated.')
    deactivate_codes.short_description = 'Deactivate selected invite code(s)'

    def activate_codes(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, f'{queryset.count()} invite code(s) have been activated.')
    activate_codes.short_description = 'Activate selected invite code(s)'


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'pronouns']
    search_fields = ['user__username', 'name']