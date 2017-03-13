from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Profile
from django.utils.timezone import datetime
from .main import get_plate_num
import os
import time
# Create your views here.
def index(request):
    return render(request, "index.html")
def process(request):
    profile = Profile()
    """
    to-do:
    ****获取exif的拍摄时间，gps信息
    ****调用地图api反向解析数据
    """
    file = request.FILES['UpLoadFile']
    content = file.read()
    with open("Server/static/pictures/" + file.name, 'wb') as fh:
        fh.write(content)
    plate_num = get_plate_num("Server/static/pictures/"  + file.name)
    time= datetime.now()
    #绑定图片和路径
    file_path = "Server/static/pictures/"  + file.name
    profile.num = plate_num
    profile.path = file_path
    profile.time = time
    profile.save()
    return render(request, "index.html", {'time': time, 'path': file_path, 'num': plate_num})
