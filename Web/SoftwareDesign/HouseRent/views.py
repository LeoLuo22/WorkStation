from django.shortcuts import render
from django.http import HttpResponse
from .models import NormalUser, Medium, NormlHouse
from PIL import Image
from django.utils import timezone
import os
import random

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
                request.session['isMedium'] = False
                return render(request, 'index.html', {'loginStatus': request.session.get('userName')})
            else:
                request.session['isLogin'] = False
        elif request.POST.get('1') == '公司':
            user = Medium.objects.filter(username__exact=username, password__exact=password)
            if user:
                request.session['isLogin'] = True
                request.session['userName'] = username
                request.session['isMedium'] = True
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

def release(request, what):
    if request.session['isLogin'] == False:
        return HttpResponse("<p> 您尚未登陆，请返回上一级页面 </p>")
    return render(request, 'release.html', {'username': request.session['userName']})

def add(request, what):
    if request.POST:
        time = timezone.now()
        location = request.POST.get('location')
        name = request.POST.get('name')
        money = request.POST.get('money')
        phone = request.POST.get('phone')
        area = request.POST.get("area")
        description = request.POST.get("description")
        username = request.session['userName']
        #picname = request.POST.get('picFile')
        if request.session['isMedium'] == False:
            try:
                os.chdir('HouseRent')
            except FileNotFoundError as err:
                pass
            filepath = "static/users/normal/" + username + "/"
            try:
                if not os._exists(filepath):
                    os.makedirs(filepath)
            except FileExistsError as err:
                pass
            filename = filepath + str(random.randint(0, 100)) + ".jpg"
            with open(filename, "wb") as fh:
                for content in request.FILES.get('picFile'):
                    fh.write(content)
            NormlHouse.objects.create(location=location, money=money,
                                      name=name, phone=phone, area=area,
                                      description=description,
                                      picpath=filename, time=time,
                                      username=username)




    return HttpResponse(request.POST['location'])
