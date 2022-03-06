from django import forms
from django.contrib.auth.forms import UserCreationForm
from learning.models import Student
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=70, help_text='Required valid emial address')

    class Meta:
        model = User
        fields = ("email",
                  "username", "password1","password2")

