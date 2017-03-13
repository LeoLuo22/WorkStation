from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^pro', views.process, name="process"),
    url(r'^sa', views.index, name="r_index"),
    ]
