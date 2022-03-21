from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'real_name', 'phone_number', 'is_student', 'is_coach', 'is_competitor']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'real_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'is_student': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_coach': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_competitor': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }