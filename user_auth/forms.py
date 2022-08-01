from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_auth.models import OurUser

class UserSignupForm(UserCreationForm):
  class Meta:
    model = OurUser
    fields = ('username', 'email', 'password1', 'password2', 'tos')

class UserLoginForm(forms.ModelForm):
  password = forms.CharField(label='password', widget=forms.PasswordInput)

  class Meta:
    model = OurUser
    fields = ('email', 'password')