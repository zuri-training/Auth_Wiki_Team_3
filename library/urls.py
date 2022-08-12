from django.urls import path
from library import views

urlpatterns = [
    path('', views.index, name='index'),
    path('documentation/', views.documentation, name='documentation'),
    path('resources/', views.resources, name='resources'),
    path('company/', views.company, name='company'),
    path('help/', views.help, name='help'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('search/', views.search_results, name='search'),
    path('auth-code/<str:pk>/', views.auth_code, name='auth-code'),
    path('notify/', views.notify, name='notify'),
]
