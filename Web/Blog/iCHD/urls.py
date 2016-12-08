from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^regist', views.regist, name="regist"),
    url(r'^login', views.login, name='login'),
    url(r'^main', views.main, name='main'),
    #url(r'^user', views.user, name='user'),
    url(r'^wel', views.wel, name='wel'),
    #url(r'^blog/blog_add', views.blog_add, name="blog_add"),
    url(r'^blog/add', views.add, name="add"),
    url(r'^blog/(?P<title>\w*)/detail', views.detail, name='detail'),
    url(r'^blog/\w*/delete', views.delete, name='delete'),
    url(r'^blog/post', views.post, name='update'),
    url(r'^blog/\w*k/update_blog', views.add, name='add'),
    url(r'^blog/all', views.all, name='all'),
    url(r'^blog/(?P<title>\w*)/comment', views.comment, name='comment'),
    url(r'^blog/(?P<title>\w*)/fuck', views.comment_add, name='comment'),
    #url(r'^blog/(\d*\w*)', views.test, name="indexs"),
    url(r'^blog/(?P<id>\d*$)', views.detail, name="detail"),
    url(r'^blog/photos', views.photos, name='photos'),
    ]
