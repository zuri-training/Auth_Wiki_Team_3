from django import forms
from django.contrib.auth.forms import UserCreationForm, 
from django.contrib.auth import authenticate
from user_auth.models import OurUser


class UserSignupForm(UserCreationForm):
    class Meta:
        model = OurUser
        fields = ('username', 'email', 'password1', 'password2', 'tos')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = OurUser.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email '{email}' is already in use.")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = OurUser.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Username is already in use.")

    def clean_tos(self):
        tos = self.cleaned_data['tos']
        if tos is False:
            raise forms.ValidationError(
                f"Please ACCEPT our Terms of Service and Privacy Policy")
        else:
            return tos


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
                raise forms.ValidationError('Invalid Email or Password')

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = OurUser
        fields = ('username', 'email')
