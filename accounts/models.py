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

from django.db import models
from django.contrib.auth.models import User
from social_links_field.models import SocialLinksField
from tinymce import models as tinymce_models

class InviteCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'Invite Code: {self.code}'
    
    def is_valid(self):
        return self.is_active
    
class UserProfile(models.Model):
    '''
    User profile model to extend user data.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    name = models.CharField(max_length=50, blank=True, null=True)
    pronouns = models.CharField(max_length=50, blank=True, null=True)
    bio = tinymce_models.HTMLField()
    pfp = models.ImageField(blank=True)
    social_links = SocialLinksField()