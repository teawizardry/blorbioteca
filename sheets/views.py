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

from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.contrib.auth import get_user_model
from .forms import CharacterSheetForm
from .models import CharacterSheet

@login_required
def new_character(request):
    user = request.user
    character = CharacterSheet.objects.create(user=user)
    return redirect('edit-character', character.pk)

def character_sheet(request, pk):
    user = request.user
    try:
        character = CharacterSheet.objects.get(pk=pk)
    except:
        character = None
    return render(request, 'sheets/character_sheet.html', {'character': character, 'user': user})

@login_required
def edit_character(request, pk):
    user = request.user
    character = CharacterSheet.objects.get(pk=pk, user=user)
    if user.id != character.user.id:
        return render(request, 'sheets/edit_profile.html', {'form': None})
    
    if request.method == 'POST':
        form = CharacterSheetForm(request.POST, request.FILES, instance=character)
        if form.is_valid():
            form.save()
            return redirect('character-sheet', character.pk)
    else:
        form = CharacterSheetForm(instance=character)
    return render(request, 'sheets/edit_character.html', {'form': form})