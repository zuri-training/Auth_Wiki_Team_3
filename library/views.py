from django.shortcuts import render, redirect

# Create your views here.
def homeView(request):
  return render(request, 'library/home.html')

def dashboardView(request):
  return render(request, 'library/dashboard.html')

