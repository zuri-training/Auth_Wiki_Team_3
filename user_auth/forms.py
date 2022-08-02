from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from user_auth.models import OurUser

class UserSignupForm(UserCreationForm):
  class Meta:
    model = OurUser
    fields = ('username', 'email', 'password1', 'password2', 'tos')

class UserLoginForm(forms.ModelForm):
  password = forms.CharField(label='Password', widget=forms.PasswordInput)

  class Meta:
    model = OurUser
    fields = ('email', 'password')
  
  def clean(self):
    if self.is_valid():
      email = self.cleaned_data['email']
      password = self.cleaned_data['password']

      if not authenticate(email=email, password=password):
        raise forms.ValidationError('Invalid Credentials')
    
