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
      
      
      # user = authenticate(request, email=email, password=password)

      # if user is not None:
      #   login(request, user)
      #   return redirect('dashboard')
      # else:
      #   messages.error(request, 'Your email or password is incorrect')
        # ctx['login_form'] = form
  
    return render(request, 'user_auth/signin.html', ctx)


def signupView(request):
    ctx = {}
    if request.method == 'POST':
      username = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password')
      confirm_password = request.POST.get('confirm-password')
      tos = request.POST.get('tos')

      if password != confirm_password:
        messages.error(request, 'Your password does not match!')
        form = UserSignupForm()
        ctx['signup_form'] = form
      else:
        try:
          user = User.objects.get(email=email)
          messages.error(request, 'User already signed up!')
          form = UserSignupForm()
          ctx['signup_form'] = form
        except:
          form = UserSignupForm(request.POST)
          if form.is_valid():
            form.save()
            return redirect('signin')
          else:
            messages.error(request, 'An error occurred during registration!')
            form = UserSignupForm()
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
