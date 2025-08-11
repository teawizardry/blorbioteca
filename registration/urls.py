from django.urls import path
from .views import SignUpView, login_redirect, user_profile, user_edit_profile

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login-redirect/', login_redirect, name='login-redirect'),
    path('<str:username>/', user_profile, name='user-profile'),
    path('profile/edit/', user_edit_profile, name='edit-profile'),
]
