from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class NicknameLoginForm(AuthenticationForm):

    username = forms.CharField(
        max_length=63, min_length=3, 
        widget=forms.TextInput(attrs = 
                               {'autofocus': True,
                                'class': 'nickname',
                                'placeholder': 'Nickname',}))
    
    password = forms.CharField(
        max_length=127, min_length=3, 
        widget=forms.PasswordInput(attrs = 
                                   {'autocomplete': 'current_password',
                                    'class': 'password',
                                    'placeholder': 'Password',}))

    class Meta:
        model = User
        fields = ['nickname', 'password']

class AccnameLoginForm(AuthenticationForm):
        nickname = forms.CharField(
        max_length=63, min_length=7, 
        widget=forms.TextInput(attrs = 
                               {'autofocus': True,
                                'class': 'number',
                                'placeholder': 'Account number',}))
    
        password = forms.CharField(
        max_length=127, min_length=7, 
        widget=forms.PasswordInput(attrs = 
                                   {'autocomplete': 'current_password',
                                    'class': 'code',
                                    'placeholder': 'Password',}))

class Registrations(AuthenticationForm):
    ...

