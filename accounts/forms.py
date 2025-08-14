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

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import InviteCode, UserProfile
from tinymce.widgets import TinyMCE
import re

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        help_text='Letters, numbers, underscores ( _ ), and hyphens ( - ) only.'
    )
    invite_code = forms.CharField(
        label='Invite Code',
        max_length=20,
        help_text='Please enter a valid invite code.'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'invite_code']
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        # check if username is URL-safe (alphanumeric, underscores, hyphens only)
        if not re.match(r'^[a-zA-Z0-9_-]+$', username):
            raise forms.ValidationError(
                "Username can only contain letters, numbers, underscores (_), and hyphens (-)."
            )
        
        # reserved names
        reserved_usernames = [
            'admin', 'api', 'www', 'mail', 'ftp', 'localhost', 'root',
            'register', 'login', 'logout', 'profile', 'settings', 'about',
            'help', 'support', 'contact', 'terms', 'privacy', 'home',
            'accounts', 'account', 'user', 'users', 'static', 'media'
        ]
        
        if username.lower() in reserved_usernames:
            raise forms.ValidationError(
                "This username is reserved and cannot be used."
            )
        
        return username

    def clean_invite_code(self):
        invite_code = self.cleaned_data.get('invite_code')
        
        # check if invite code was entered
        if not invite_code:
            raise forms.ValidationError('Invite code is required.')
        
        # check if invite code is valid
        try:
            code_obj = InviteCode.objects.get(code=invite_code)
            if not code_obj.is_valid():
                raise forms.ValidationError('Invalid invite code.')
            return invite_code
        except InviteCode.DoesNotExist:
            raise forms.ValidationError('Invalid invite code.')


# form for editing user profile
class EditProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'pronouns', 'bio', 'pfp', 'social_links']

