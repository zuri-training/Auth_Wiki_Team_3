from django.shortcuts import render, redirect
from django.contrib .auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import OurUser
from .forms import UserSignupForm, UserLoginForm
# from account.forms import UserSignupForm

# Create your views here.


def authHomeView(request):
    return redirect('signin')

def signinView(request):
    ctx = {}
    if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')

      try:
        user = OurUser.objects.get(email=email)
        ctx['user'] = user
      except:
        messages.error(request, 'User has not signed up!')  
      
      user = authenticate(request, email=email, password=password)

      if user is not None:
        login(request, user)
        return redirect('dashboard')
      else:
        messages.error(request, 'Your email or password is incorrect')
  
    return render(request, 'user_auth/signin.html', ctx)


def signupView(request):
  user = request.user
  if user.is_authenticated:
    messages.error(request, 'You have already signed in.')
    return redirect('dashboard')
  ctx = {}

  if request.POST:
    form = UserSignupForm(request.POST)

    if form.is_valid():
      form.save()
      email = form.cleaned_data.get('email').lower()
      raw_password = form.cleaned_data.get('password1')
      messages.success(request, 'Signed up successfully, Sign In.')
      return redirect('signin')
    else:
      ctx['signup_form'] = form

  else:
    form = UserSignupForm()
    ctx['signup_form'] = form
  
  return render(request, 'user_auth/signup.html', ctx)

def signoutView(request):
  logout(request)
  return redirect('signin')

def forgotPasswordView(request):
    return render(request, 'user_auth/forgot-password.html')
