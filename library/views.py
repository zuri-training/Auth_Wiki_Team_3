from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from .models import AuthCode, Notification

# Create your views here.


def index(request):
    return render(request, 'library/index.html')


def index(request):
    return render(request, 'library/index.html')


def documentation(request):
    return render(request, 'library/documentation.html')


def resources(request):
    return render(request, 'library/resources.html')


def company(request):
    return render(request, 'library/company.html')


def help(request):
    return render(request, 'library/help.html')


def login(request):
    return render(request, 'library/login.html')


def signup(request):
    return render(request, 'library/signup.html')


def unauth_dash(request):
    return render(request, 'library/unauth_dash.html')


def search_results(request):
    if request.method == 'POST':
        res = None
        query = request.POST.get('query')
        qs = AuthCode.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        if len(qs) > 0 and len(query) > 0:
            data = []
            for pos in qs:
                item = {
                    'pk': pos.id,
                    'name': pos.name,
                    'desc': pos.description,
                }
                data.append(item)
            res = data
        else:
            res = 'No Authentication Code found...'

        return JsonResponse({'data': res})
    return JsonResponse({})


def auth_code(request, pk):
    code = AuthCode.objects.get(id=pk)

    ctx = {'code': code}
    return render(request, 'library/dashboard.html', ctx)


def notify(request):
    def genAlert(type):
        if type == 'welcome':
            notific = 'Welcome to Auth Wiki'
        elif type == 'new_upload':
            notific = 'New Authenticode Uploaded'
        elif type == 'profile_update':
            notific = 'Your profile have been updated'
        elif type == 'password_reset':
            notific = 'Password reset successful'
        else:
            notific = None

        if type is not None and notific is not None:
            pass
