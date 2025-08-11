from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import InviteCode

class UserRegistrationForm(UserCreationForm):
    invite_code = forms.CharField(label="Invite Code")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'invite_code']

    def clean_invite_code(self):
        invite_code = self.cleaned_data.get('invite_code')
        if InviteCode.objects.filter(code=invite_code).exists():
            return invite_code
        raise forms.ValidationError("Invalid invite code.")


# Form for editing user profile
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

