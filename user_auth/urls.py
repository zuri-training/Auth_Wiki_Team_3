from django.urls import path
from user_auth import views

urlpatterns = [
  path('', views.authHomeView, name='auth'),
  path('signin/', views.signinView, name='signin'),
  path('signup/', views.signupView, name='signup'),
  path('signout/', views.signoutView, name='signout'),
  path('forgot-password/', views.forgotPasswordView, name='forgot-password'),
]