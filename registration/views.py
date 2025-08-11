from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.contrib.auth import get_user_model
from .forms import UserEditForm
import re

@login_required
def login_redirect(request):
    user = request.user
    # check if 2fa is enabled
    has_2fa = TOTPDevice.objects.filter(user=user, confirmed=True).exists()
    if has_2fa:
        return redirect('user-profile', username=user.username)
    else:
        return redirect('two_factor:setup')


class SignUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('two_factor:login')
    template_name = 'registration/registration.html'
    

def user_profile(request, username):
    # Sanitize username: allow only alphanumeric, underscore, hyphen, and dot
    if not re.fullmatch(r'[\w.-]+', username):
        return render(request, 'registration/profile.html', {'profile_user': None, 'invalid_username': True})
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    return render(request, 'registration/profile.html', {'profile_user': user, 'invalid_username': False})


@login_required
def user_edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', username=user.username)
    else:
        form = UserEditForm(instance=user)
    return render(request, 'registration/edit_profile.html', {'form': form})
