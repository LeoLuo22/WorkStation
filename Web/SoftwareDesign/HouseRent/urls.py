from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    #url(r'^register/status/$', views.status, name='status'),
    url(r'^rent/$', views.rent, name='rent'),
    url(r'^want/$', views.want, name='want'),
    url(r'^index', views.index, name='index1'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^\w*/logout', views.logout, name='lout'),
    url(r'^(\w)*/release', views.release, name='release'),
    url(r'^(\w)*/add', views.add, name="add"),
    url(r'houses/(?P<ID>\d*)', views.detail, name="detail"),
    url(r'^search/(?P<category>\w*)/', views.search, name='search'),
    url(r'admin/$', views.admin, name='admin'),
    url(r'^admin/check/(?P<username>\w*)', views.check, name='check'),
    url(r'^admin/analysis/(?P<username>\w*)', views.analysis, name='analysis'),
]
