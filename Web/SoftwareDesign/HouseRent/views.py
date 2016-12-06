from django.shortcuts import render
from django.http import HttpResponse
from .models import NormalUser, Medium

def isValid(register, information):
    try:
        if register.objects.get(username=information):
            return False
        elif register.objects.get(email=information):
            return False
    except Exception:
        pass
    return True

def index(request):
    isLogin = request.session.get('isLogin', False)
    if isLogin:
        username = request.session.get('userName', False)
        return render(request, 'index.html', {'loginStatus': request.session.get('userName')})
    return render(request, 'index.html', {'loginStatus': 'Login'})

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if request.POST.get('1') == '个人':
            user = NormalUser.objects.filter(username__exact=username, password__exact=password)
            if user:
                request.session['isLogin'] = True
                request.session['userName'] = username
                request.session['type'] = request.POST.get('1')
                return render(request, 'index.html', {'loginStatus': request.session.get('userName')})
            else:
                request.session['isLogin'] = False
        elif request.POST.get('1') == '公司':
            user = Medium.objects.filter(username__exact=username, password__exact=password)
            if user:
                request.session['isLogin'] = True
                request.session['userName'] = username
                request.session['type'] = request.POST.get('1')
                return render(request, 'index.html', {'loginStatus': request.session.get('userName')})
            else:
                request.session['isLogin'] = False
    return render(request, 'login.html', {'loginStatus': 'Login'})

def logout(request):
    request.session['isLogin'] = False
    return render(request, 'index.html', {'loginStatus': 'Login'})

def register(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if request.POST.get('1') == '个人':
            #result = NormalUser.objects.get_or_create(username=username, password=password, email=email)
            if isValid(NormalUser, username) and isValid(NormalUser, email):
                NormalUser.objects.create(username=username, password=password, email=email)
                return render(request, 'login.html', {'flag': "注册成功"})
            else:
                return render(request, 'register.html', {'flag': "该用户名或邮箱已被注册"})
        elif request.POST.get('1') == '公司':
            if isValid(Medium, username) and isValid(Medium, email):
                Medium.objects.create(username=username, password=password, email=email)
                return render(request, 'login.html', {'flag': "注册成功"})
            else:
                return render(request, 'register.html', {'flag': "该用户名或邮箱已被注册"})
    return render(request, 'register.html')
