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
from django.db import models
from tinymce.widgets import TinyMCE
from .models import CharacterSheet

class CharacterSheetForm(forms.ModelForm):
    class Meta:
        model = CharacterSheet
        fields = ['name', 'bio', 'sidebar']
        
class CharacterDeleteForm(forms.Form):
    def __init__(self,name,*args,**kwargs):
        super(CharacterDeleteForm,self).__init__(*args,**kwargs)
        self.fields['delete_confirmation'] = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'placeholder': f"Type 'DELETE' to PERMANENTLY delete {name}."}), help_text = f"Type 'DELETE' to PERMANENTLY delete {name}.")

    delete_confirmation = forms.CharField()