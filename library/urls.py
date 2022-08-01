from django.urls import path
from library import views

urlpatterns = [
  path('', views.homeView, name='home'),
  path('dashboard/', views.dashboardView, name='dashboard'),
]