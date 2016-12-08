from django.shortcuts import render
from django.http import HttpResponse
from .models import User, House
from PIL import Image
from django.utils import timezone
import os
import random
from django.http import HttpResponseRedirect

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
    houses = House.objects.all()
    if len(houses) > 3:
        houses = houses[0:3]
    #isLogin = request.session.get('isLogin', False)
    #if isLogin:
    if request.session['isLogin'] == False:
        return render(request, 'index.html', {'loginStatus': 'Login', 'houses': houses})

    username = request.session.get('userName', False)
    return render(request, 'index.html', {'loginStatus': request.session.get('userName'), 'houses': houses,
                      'isMedium': request.session['isMedium']})

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username__exact=username, password__exact=password)
        if user:
            request.session['isLogin'] = True
            request.session['userName'] = username
            request.session['isMedium'] = False
            return HttpResponseRedirect('/HouseRent')
        else:
            request.session['isLogin'] = False
    return render(request, 'login.html', {'loginStatus': 'Login'})

def logout(request):
    request.session['isLogin'] = False
    return HttpResponseRedirect('/HouseRent')

def register(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if request.POST.get('1') == '个人':
            if isValid(User, username) and isValid(User, email):
                User.objects.create(username=username, password=password, email=email, isMedium=False)
                return render(request, 'login.html', {'flag': "注册成功"})
            else:
                return render(request, 'register.html', {'flag': "该用户名或邮箱已被注册"})
        elif request.POST.get('1') == '公司':
            if isValid(User, username) and isValid(User, email):
                User.objects.create(username=username, password=password, email=email, isMedium=True)
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
            filename = filepath + str(random.randint(100, 9999)) + ".jpg"
            with open(filename, "wb") as fh:
                for content in request.FILES.get('picFile'):
                    fh.write(content)
            try:
                NormalHouse.objects.create(location=location, money=money,
                                      name=name, phone=phone, area=area,
                                      description=description,
                                      picpath=filename, time=time,
                                      username=username)
            except ValueError as err:
                return HttpResponse("<p>你的输入有误，请返回上一级</p>")
            return HttpResponseRedirect('/HouseRent')
        elif request.session['isMedium'] == True:
            try:
                os.chdir('HouseRent')
            except FileNotFoundError as err:
                pass
            filepath = "static/users/medium/" + username + "/"
            try:
                if not os._exists(filepath):
                    os.makedirs(filepath)
            except FileExistsError as err:
                pass
            filename = filepath + str(random.randint(100, 9999)) + ".jpg"
            with open(filename, "wb") as fh:
                for content in request.FILES.get('picFile'):
                    fh.write(content)
            MediumHouse.objects.create(location=location, money=money,
                                      name=name, phone=phone, area=area,
                                      description=description,
                                      picpath=filename, time=time,
                                      username=username, isCheck=False)
            return render(request, 'index.html', {'loginStatus': request.session['userName']})
    return HttpResponse("An error occured")

def detail(request, ID):
    return render(request, 'detail.html', {'house': House.objects.get(id=ID)})
