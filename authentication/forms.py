from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2']
