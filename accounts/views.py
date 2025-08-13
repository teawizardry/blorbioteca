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

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.contrib.auth import get_user_model
from .forms import EditProfile
from .models import UserProfile
import re

class Registration(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('two_factor:login')
    template_name = 'registration/registration.html'
    
    
@login_required
def login_redirect(request):
    # redirects to 2fa setup on login if not enabled, profile page otherwise.
    user = request.user
    if TOTPDevice.objects.filter(user=user, confirmed=True).exists():
        return redirect('user-profile', username=user.username)
    else:
        return redirect('two_factor:setup')
    

def user_profile(request, username):
    # allow only alphanumeric, underscore, hyphen, and dot in username for url safety
    if not re.fullmatch(r'[\w.-]+', username):
        return render(request, 'registration/profile.html', {'profile_user': None, 'invalid_username': True})
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    try:
        user_profile = UserProfile.objects.get(user=user)
    except:
        user_profile = None
    return render(request, 'registration/profile.html', {'profile_user': user_profile, 'invalid_username': False})


@login_required
def edit_profile(request):
    user = request.user
    # get UserProfile for the user, create one if it doesn't exist
    profile, created = UserProfile.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user-profile', username=user.username)
    else:
        form = EditProfile(instance=profile)
    return render(request, 'registration/edit_profile.html', {'form': form})
