from django.shortcuts import render
from django.http import HttpResponse
from .models import NormalUser, Medium

def isValid(register, information):
    if register.objects.get(username=information):
        return False
    elif register.objects.get(email=information):
        return False
    return True

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if request.POST.get('1') == '个人':
            #result = NormalUser.objects.get_or_create(username=username, password=password, email=email)

            return HttpResponse(isValid(NormalUser, username))
        elif request.POST.get('1') == '公司':
            pass

    return render(request, 'register.html')
