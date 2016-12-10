from django.shortcuts import render
from django.http import HttpResponse
from .models import User, House
from PIL import Image
from django.utils import timezone
import os
import random
from django.http import HttpResponseRedirect
from datetime import datetime

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
    #*****出租
    rhouses = House.objects.filter(isWanted__exact=False)
    whouses = House.objects.filter(isWanted__exact=True)
    #isLogin = request.session.get('isLogin', False)
    #if isLogin:
    #return HttpResponse(rhouses.money)
    if request.session.get('isLogin') != True:
        return render(request, 'index.html', {'loginStatus': 'Login', 'rhouses': rhouses, 'whouses': whouses})

    username = request.session.get('userName', False)
    return render(request, 'index.html', {'loginStatus': request.session.get('userName'), 'rhouses': rhouses,
                  'whouses': whouses})

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username__exact=username, password__exact=password)
        if user.isChecked == False:
            return HttpResponse("<p>你的信息还在审核</p>")
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
        owner = request.POST.get('owner')
        paper = request.POST.get('paper')
        taxpaper = request.POST.get('taxpaper')

        if request.POST.get('1') == '个人':
            if isValid(User, username) and isValid(User, email):
                User.objects.create(username=username, password=password, email=email, isMedium=False)
                return render(request, 'login.html', {'flag': "注册成功"})
            else:
                return render(request, 'register.html', {'flag': "该用户名或邮箱已被注册"})
        elif request.POST.get('1') == '公司':
            if isValid(User, username) and isValid(User, email):
                #assert(True, request.FILES)
                if request.FILES:
                    #return HttpResponse("OK")
                    try:
                        os.chdir('HouseRent')
                    except FileNotFoundError as err:
                        pass
                    filepath = "static/users/" + username + "/"
                    try:
                        if not os._exists(filepath):
                            os.makedirs(filepath)
                    except FileExistsError as err:
                        pass
                    paperpic = filepath + "paperpic" + ".jpg"
                    idpic = filepath + "idpic" + ".jpg"
                    with open(paperpic, 'wb') as fh:
                        for content in request.FILES.get('paperpic'):
                            fh.write(content)
                    with open(idpic, 'wb') as fp:
                        for content in request.FILES.get('idpic'):
                            fp.write(content)
                    User.objects.create(username=username, password=password, email=email, isMedium=True, isChecked=False, owner=owner, paper=paper, taxpaper=taxpaper,
                                        paperpic=paperpic, idpic=idpic)
                    return render(request, 'login.html', {'flag': "请等待管理员审核"})
            else:
                return render(request, 'register.html', {'flag': "该用户名或邮箱已被注册"})
    return render(request, 'register.html')

def release(request, what):
    if request.session['isLogin'] == False:
        #return HttpResponse("<p> 您尚未登陆，请返回上一级页面 </p>")
        return HttpResponseRedirect('/HouseRent')
    return render(request, 'release.html', {'username': request.session['userName'], 'loginStatus': request.session.get('userName')})

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
        filename = "fakepath"
        if request.FILES:
            try:
                os.chdir('HouseRent')
            except FileNotFoundError as err:
                pass
            filepath = "static/users/" + username + "/"
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
            if User.objects.get(username__exact=username).isMedium == False: #普通用户
                if request.POST.get('1') == '出租':
                    House.objects.create(location=location, money=money,
                                      name=name, phone=phone, area=area,
                                      description=description,
                                      picpath=filename, time=time,
                                      username=username, isWanted=False, isMedium=False)
                elif request.POST.get('1') == '求租':
                    House.objects.create(location=location, money=money,
                                      name=name, phone=phone, area=area,
                                      description=description,
                                      picpath=filename, time=time,
                                      username=username, isWanted=True, isMedium=False)
            else:
                if request.POST.get('1') == '出租':
                    House.objects.create(location=location, money=money,
                                      name=name, phone=phone, area=area,
                                      description=description,
                                      picpath=filename, time=time,
                                      username=username, isWanted=False, isMedium=True)
                elif request.POST.get('1') == '求租':
                    House.objects.create(location=location, money=money,
                                      name=name, phone=phone, area=area,
                                      description=description,
                                      picpath=filename, time=time,
                                      username=username, isWanted=True, isMedium=True)
        except Exception as err:
            return HttpResponse("<p>你的输入有误，请返回上一级</p>")
    return HttpResponseRedirect('/HouseRent')

    return HttpResponse("An error occured")

def detail(request, ID):
    return render(request, 'detail.html', {'house': House.objects.get(id=ID)})

def search(request, category):
    if request.POST:
        location = request.POST.get('location')
        moneyTop = int(request.POST.get('moneyTop'))
        moneyLow = int(request.POST.get('moneyLow'))
        areaTop = float(request.POST.get('areaTop'))
        areaLow = float(request.POST.get('areaLow'))

        if category == "all":
            houses = House.objects.filter(location__icontains=location)
            houses = houses.filter(money__gte=moneyLow)
            houses = houses.filter(money__lte=moneyTop)
            houses = houses.filter(area__gte=areaLow)
            houses = houses.filter(area__lte=areaTop)
            return render(request, 'search.html', {'houses': houses})

        if category == "rent":
            houses = House.objects.filter(isWanted__exact=False)
            houses = House.objects.filter(location__icontains=location)
            houses = houses.filter(money__gte=moneyLow)
            houses = houses.filter(money__lte=moneyTop)
            houses = houses.filter(area__gte=areaLow)
            houses = houses.filter(area__lte=areaTop)
            return render(request, 'search.html', {'houses': houses})

        if category == "want":
            houses = House.objects.filter(isWanted__exact=True)
            houses = House.objects.filter(location__icontains=location)
            houses = houses.filter(money__gte=moneyLow)
            houses = houses.filter(money__lte=moneyTop)
            houses = houses.filter(area__gte=areaLow)
            houses = houses.filter(area__lte=areaTop)
            return render(request, 'search.html', {'houses': houses})
    return HttpResponseRedirect('/HouseRent')

def admin(request):
    normalUsers = User.objects.filter(isMedium__exact=False, isChecked__exact=True)
    mediums = User.objects.filter(isMedium__exact=True, isChecked__exact=True)
    illegals = User.objects.filter(isChecked__exact=False)
    return render(request, 'admin.html', {'normalUsers': normalUsers, 'mediums': mediums, 'illegals': illegals})

def check(request, category, username):
    if request.POST:
        houses = House.objects.filter(username__exact=username)
        begin_time_row = (request.POST.get('begin_time')).replace("T", "")
        begin_time = datetime.strptime(begin_time_row, "%Y-%m-%d%H:%M")
        end_time_row = (request.POST.get('end_time')).replace("T", "")
        end_time = datetime.strptime(end_time_row, "%Y-%m-%d%H:%M")
        houses = houses.filter(time__gte=begin_time)
        houses = houses.filter(time__lte=end_time)
        return HttpResponse(len(houses))
    if category == 'check':
        user = User.objects.get(username__exact=username)
        return render(request, 'check.html', {'user': user})
    elif category == 'analysis':
        return render(request, 'analysis.html')
