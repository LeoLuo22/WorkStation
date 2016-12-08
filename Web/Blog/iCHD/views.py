from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.db.utils import IntegrityError
from django.utils import timezone
#from .models import User
from django.contrib.auth.models import User
from .models import Blog, Comment
# Create your views here.
def index(request):
    return render(request, 'iCHD/index.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        return HttpResponse('Success')
    else:
        return render(request, 'iCHD/regist.html')

def regist(request):
    return render(request, 'iCHD/regist.html')

def main(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        u = User.objects.create_user(username, password)
    except IntegrityError as err:
        return render(request, 'iCHD/regist.html', {'error_message': '该用户名已被注册'})
    u.save
    return HttpResponse("Ok")

def add(request):
    title = request.POST.get('title')
    body = request.POST.get('content')
    time = timezone.now()
    b = Blog(id=1, title=title, body=body, time=time)
    b.save()
    return HttpResponse("<h1>" + title + "</h1>" + "<h2>" + body + "</h2>")

def wel(request):
    return render(request, 'iCHD/wel.html')

def post(request):
    return render(request, 'iCHD/post.html')

def delete(request):
    b = get_object_or_404(Blog, id=1)
    b.delete()
    return HttpResponse("删除成功")

def all(request):
    Blogs = Blog.objects.all()
    blogs = Blog.objects.all()
    contents = []
    for blog in Blogs:
        if len(blog.body) > 100:
            blog.body = blog.body[0:100]
            contents.append(blog.body)
        else:
            contents.append(blog.body)

    return render(request, 'iCHD/all.html', {'blogs':blogs})#, 'contents':contents})#, {'contents':contents})

def detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    comments = blog.comment_set.all()
    try:
        if len(request.GET.get('username')) != 0 and len(request.GET.get('textarea')) != 0:
            username = request.GET.get('username')
            textarea = request.GET.get('textarea')
            blog.comment_set.create(username=username, content = textarea, datetime=timezone.now())
    except TypeError as err:
        pass
    error_message = "文章不存在"
    return render(request, 'iCHD/detail.html', {'blog': blog, 'error_message':error_message, 'comments':comments})

def comment(request, title):
    blog = Blog.objects.get(title=title)
    comments = blog.comment_set.all()


def comment_add(request, title):
    b = Blog.objects.get(title=title)
    comment = request.POST['content']
    b.comment_set.create(comment=comment)
    return HttpResponseRedirect('../all.html')

def test(request, id):#$, textarea):
    user = request.GET.get('username')
    textarea = request.GET.get('textarea')
    return HttpResponse(textarea)

def photos(request):
    return render(request, 'iCHD/photos.html')
